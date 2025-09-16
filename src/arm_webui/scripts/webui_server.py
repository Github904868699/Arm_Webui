#!/usr/bin/env python3
"""ROS node that exposes a Flask powered Web UI to control the arm via /joy."""

import threading
from typing import Dict

import rospy
from flask import Flask, jsonify, render_template_string, request
from sensor_msgs.msg import Joy

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang=\"zh\">
<head>
  <meta charset=\"UTF-8\" />
  <title>机械臂 Web 控制台</title>
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <style>
    :root {
      color-scheme: light dark;
      --bg-color: #0f172a;
      --card-color: rgba(15, 23, 42, 0.75);
      --accent: #38bdf8;
      --accent-strong: #0ea5e9;
      --text-color: #f8fafc;
      --muted: #94a3b8;
      --success: #34d399;
      --danger: #fb7185;
      font-family: \"Inter\", \"PingFang SC\", \"Microsoft YaHei\", sans-serif;
    }

    body {
      margin: 0;
      min-height: 100vh;
      background: radial-gradient(circle at top, rgba(56, 189, 248, 0.25), transparent 55%),
                  radial-gradient(circle at bottom, rgba(147, 197, 253, 0.25), transparent 60%),
                  var(--bg-color);
      color: var(--text-color);
    }

    .page {
      max-width: 1100px;
      margin: 0 auto;
      padding: 40px 24px 80px;
      display: flex;
      flex-direction: column;
      gap: 28px;
    }

    header {
      text-align: center;
      padding: 12px 16px 24px;
    }

    header h1 {
      margin: 0;
      font-size: clamp(1.8rem, 3vw, 2.4rem);
      letter-spacing: 0.05em;
    }

    header p {
      margin: 12px auto 0;
      max-width: 720px;
      color: var(--muted);
      line-height: 1.6;
    }

    .card {
      background: var(--card-color);
      border-radius: 20px;
      padding: 24px;
      box-shadow: 0 24px 45px rgba(15, 23, 42, 0.35);
      backdrop-filter: blur(18px);
      border: 1px solid rgba(255, 255, 255, 0.05);
    }

    .card h2 {
      margin-top: 0;
      font-size: 1.35rem;
      letter-spacing: 0.04em;
    }

    .description {
      margin: 4px 0 20px;
      color: var(--muted);
      font-size: 0.95rem;
    }

    .joint-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 18px;
    }

    .joint-card {
      background: rgba(15, 23, 42, 0.55);
      border-radius: 16px;
      padding: 18px;
      border: 1px solid rgba(148, 163, 184, 0.25);
      display: flex;
      flex-direction: column;
      gap: 12px;
      transition: transform 0.2s ease, border 0.2s ease;
    }

    .joint-card:hover {
      transform: translateY(-4px);
      border-color: rgba(56, 189, 248, 0.6);
    }

    .joint-card h3 {
      margin: 0;
      font-weight: 600;
      letter-spacing: 0.06em;
    }

    .joint-actions {
      display: flex;
      gap: 12px;
    }

    .joint-actions button,
    .cartesian-grid button {
      flex: 1;
      padding: 12px 16px;
      border-radius: 12px;
      border: 1px solid rgba(148, 163, 184, 0.2);
      background: linear-gradient(135deg, rgba(56, 189, 248, 0.25), rgba(14, 165, 233, 0.4));
      color: var(--text-color);
      font-size: 1rem;
      font-weight: 600;
      cursor: pointer;
      transition: transform 0.15s ease, box-shadow 0.15s ease, border 0.15s ease;
    }

    .joint-actions button:hover,
    .cartesian-grid button:hover {
      transform: translateY(-2px);
      border-color: rgba(56, 189, 248, 0.75);
      box-shadow: 0 12px 25px rgba(14, 165, 233, 0.25);
    }

    .joint-actions button:active,
    .cartesian-grid button:active {
      transform: translateY(0);
      box-shadow: inset 0 4px 12px rgba(15, 23, 42, 0.35);
    }

    .joint-actions button.negative {
      background: linear-gradient(135deg, rgba(251, 113, 133, 0.35), rgba(244, 63, 94, 0.45));
    }

    .joint-actions button.positive {
      background: linear-gradient(135deg, rgba(52, 211, 153, 0.35), rgba(16, 185, 129, 0.45));
    }

    .step-control {
      margin-top: 16px;
      display: flex;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
      color: var(--muted);
    }

    .step-control input[type=\"range\"] {
      width: min(320px, 100%);
    }

    .cartesian-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
      gap: 16px;
    }

    .status {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    #statusLog {
      min-height: 60px;
      padding: 14px 18px;
      border-radius: 12px;
      background: rgba(15, 23, 42, 0.55);
      border: 1px solid rgba(148, 163, 184, 0.2);
      color: var(--muted);
      line-height: 1.5;
      white-space: pre-wrap;
    }

    @media (max-width: 640px) {
      .joint-actions {
        flex-direction: column;
      }
    }
  </style>
</head>
<body>
  <div class=\"page\">
    <header>
      <h1>机械臂实时 Web 控制台</h1>
      <p>通过局域网访问的 WebUI，向 /joy 话题发送虚拟手柄消息，实现对 6 个关节轴以及 XYZ 笛卡尔坐标的精细调节。</p>
    </header>

    <section class=\"card\">
      <h2>关节轴调节</h2>
      <p class=\"description\">单独调节 6 个关节轴，每次点击按当前动作幅度缩放发布一个增量命令。</p>
      <div class=\"joint-grid\">
        <div class=\"joint-card\">
          <h3>J1</h3>
          <div class=\"joint-actions\">
            <button data-action=\"joint\" data-axis=\"0\" data-direction=\"-1\" class=\"negative\">逆时针</button>
            <button data-action=\"joint\" data-axis=\"0\" data-direction=\"1\" class=\"positive\">顺时针</button>
          </div>
        </div>
        <div class=\"joint-card\">
          <h3>J2</h3>
          <div class=\"joint-actions\">
            <button data-action=\"joint\" data-axis=\"1\" data-direction=\"-1\" class=\"negative\">负向</button>
            <button data-action=\"joint\" data-axis=\"1\" data-direction=\"1\" class=\"positive\">正向</button>
          </div>
        </div>
        <div class=\"joint-card\">
          <h3>J3</h3>
          <div class=\"joint-actions\">
            <button data-action=\"joint\" data-axis=\"2\" data-direction=\"-1\" class=\"negative\">负向</button>
            <button data-action=\"joint\" data-axis=\"2\" data-direction=\"1\" class=\"positive\">正向</button>
          </div>
        </div>
        <div class=\"joint-card\">
          <h3>J4</h3>
          <div class=\"joint-actions\">
            <button data-action=\"joint\" data-axis=\"3\" data-direction=\"-1\" class=\"negative\">负向</button>
            <button data-action=\"joint\" data-axis=\"3\" data-direction=\"1\" class=\"positive\">正向</button>
          </div>
        </div>
        <div class=\"joint-card\">
          <h3>J5</h3>
          <div class=\"joint-actions\">
            <button data-action=\"joint\" data-axis=\"4\" data-direction=\"-1\" class=\"negative\">负向</button>
            <button data-action=\"joint\" data-axis=\"4\" data-direction=\"1\" class=\"positive\">正向</button>
          </div>
        </div>
        <div class=\"joint-card\">
          <h3>J6</h3>
          <div class=\"joint-actions\">
            <button data-action=\"joint\" data-axis=\"5\" data-direction=\"-1\" class=\"negative\">负向</button>
            <button data-action=\"joint\" data-axis=\"5\" data-direction=\"1\" class=\"positive\">正向</button>
          </div>
        </div>
      </div>

      <div class=\"step-control\">
        <label for=\"jointStep\">动作幅度：</label>
        <input id=\"jointStep\" type=\"range\" min=\"1\" max=\"5\" value=\"1\" step=\"1\" />
        <span id=\"jointStepLabel\">×1</span>
      </div>
    </section>

    <section class=\"card\">
      <h2>笛卡尔坐标调节</h2>
      <p class=\"description\">六个方向按钮提供 XYZ 正负方向的末端位姿微调。</p>
      <div class=\"cartesian-grid\">
        <button data-action=\"cartesian\" data-axis=\"x\" data-direction=\"1\">X+</button>
        <button data-action=\"cartesian\" data-axis=\"x\" data-direction=\"-1\">X-</button>
        <button data-action=\"cartesian\" data-axis=\"y\" data-direction=\"1\">Y+</button>
        <button data-action=\"cartesian\" data-axis=\"y\" data-direction=\"-1\">Y-</button>
        <button data-action=\"cartesian\" data-axis=\"z\" data-direction=\"1\">Z+</button>
        <button data-action=\"cartesian\" data-axis=\"z\" data-direction=\"-1\">Z-</button>
      </div>
    </section>

    <section class=\"card status\">
      <h2>状态</h2>
      <div id=\"statusLog\">Web UI 已就绪，点击按钮即可发送控制指令。</div>
    </section>
  </div>

  <script>
    const statusLog = document.getElementById('statusLog');
    const jointStep = document.getElementById('jointStep');
    const jointStepLabel = document.getElementById('jointStepLabel');

    jointStep.addEventListener('input', () => {
      jointStepLabel.textContent = `×${jointStep.value}`;
    });

    function logMessage(message, isError = false) {
      const time = new Date().toLocaleTimeString();
      statusLog.textContent = `[${time}] ${message}`;
      statusLog.style.color = isError ? 'var(--danger)' : 'var(--muted)';
    }

    async function postJSON(url, payload) {
      const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
      const data = await response.json().catch(() => ({ success: false, error: '服务器无响应' }));
      if (!response.ok || !data.success) {
        throw new Error(data.error || '执行失败');
      }
      return data;
    }

    function handleJointClick(event) {
      const axis = parseInt(event.currentTarget.dataset.axis, 10);
      const direction = parseInt(event.currentTarget.dataset.direction, 10);
      const scale = parseInt(jointStep.value, 10);
      const value = direction * scale;

      postJSON('/api/joint', { index: axis, value })
        .then(() => {
          const orientation = direction > 0 ? '正向' : '负向';
          logMessage(`已发送关节 J${axis + 1} ${orientation} 调节 ×${scale}`);
        })
        .catch((error) => {
          logMessage(`关节 J${axis + 1} 调节失败：${error.message}`, true);
        });
    }

    function handleCartesianClick(event) {
      const axis = event.currentTarget.dataset.axis;
      const direction = parseInt(event.currentTarget.dataset.direction, 10);

      postJSON('/api/cartesian', { axis, direction })
        .then(() => {
          const orientation = direction > 0 ? '+' : '-';
          logMessage(`已发送 ${axis.toUpperCase()}${orientation} 方向微调指令`);
        })
        .catch((error) => {
          logMessage(`笛卡尔调节失败：${error.message}`, true);
        });
    }

    document.querySelectorAll('[data-action="joint"]').forEach((button) => {
      button.addEventListener('click', handleJointClick);
    });

    document.querySelectorAll('[data-action="cartesian"]').forEach((button) => {
      button.addEventListener('click', handleCartesianClick);
    });
  </script>
</body>
</html>
"""


class ArmWebUIServer:
    """Publishes Joy messages according to HTTP requests."""

    CARTESIAN_MAPPING: Dict[str, Dict[int, int]] = {
        "x": {1: 0, -1: 1},
        "y": {1: 2, -1: 3},
        "z": {1: 4, -1: 5},
    }

    def __init__(self) -> None:
        rospy.init_node("arm_webui_server", anonymous=False)
        self.publisher = rospy.Publisher("/joy", Joy, queue_size=10)
        self.frame_id = rospy.get_param("~frame_id", "arm_webui")
        self.host = rospy.get_param("~host", "0.0.0.0")
        self.port = int(rospy.get_param("~port", 5000))

        self.app = Flask(__name__)
        self._register_routes()

        rospy.loginfo(
            "Starting Arm WebUI server on http://%s:%d (frame_id=%s)",
            self.host,
            self.port,
            self.frame_id,
        )

        self._thread = threading.Thread(target=self._run_app, daemon=True)
        self._thread.start()

    def _run_app(self) -> None:
        """Run the Flask application."""
        self.app.run(host=self.host, port=self.port, threaded=True, use_reloader=False)

    def _register_routes(self) -> None:
        app = self.app

        @app.route("/")
        def index():
            return render_template_string(HTML_TEMPLATE)

        @app.route("/api/joint", methods=["POST"])
        def handle_joint():
            data = request.get_json(force=True, silent=True) or {}
            index = data.get("index")
            value = data.get("value")

            try:
                index = int(index)
                value = float(value)
            except (TypeError, ValueError):
                return jsonify(success=False, error="关节数据不合法"), 400

            if not 0 <= index < 6:
                return jsonify(success=False, error="关节索引越界"), 400

            self.publish_joint(index, value)
            return jsonify(success=True)

        @app.route("/api/cartesian", methods=["POST"])
        def handle_cartesian():
            data = request.get_json(force=True, silent=True) or {}
            axis = data.get("axis")
            direction = data.get("direction")

            if axis not in self.CARTESIAN_MAPPING:
                return jsonify(success=False, error="未知的轴向"), 400

            try:
                direction = int(direction)
            except (TypeError, ValueError):
                return jsonify(success=False, error="方向参数不合法"), 400

            if direction not in (-1, 1):
                return jsonify(success=False, error="方向参数必须为±1"), 400

            self.publish_cartesian(axis, direction)
            return jsonify(success=True)

    def publish_joint(self, index: int, value: float) -> None:
        """Publish a Joy message for a joint axis adjustment."""
        joy = Joy()
        joy.header.stamp = rospy.Time.now()
        joy.header.frame_id = self.frame_id
        joy.axes = [0.0] * 6
        joy.buttons = [0] * 6
        joy.axes[index] = value
        self.publisher.publish(joy)

    def publish_cartesian(self, axis: str, direction: int) -> None:
        joy = Joy()
        joy.header.stamp = rospy.Time.now()
        joy.header.frame_id = self.frame_id
        joy.axes = [0.0] * 6
        joy.buttons = [0] * 6
        button_index = self.CARTESIAN_MAPPING[axis][direction]
        joy.buttons[button_index] = 1
        self.publisher.publish(joy)


def main() -> None:
    server = ArmWebUIServer()
    rospy.loginfo("Arm WebUI server is ready to accept commands.")
    rospy.spin()


if __name__ == "__main__":
    main()
