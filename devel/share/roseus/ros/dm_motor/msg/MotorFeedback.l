;; Auto-generated. Do not edit!


(when (boundp 'dm_motor::MotorFeedback)
  (if (not (find-package "DM_MOTOR"))
    (make-package "DM_MOTOR"))
  (shadow 'MotorFeedback (find-package "DM_MOTOR")))
(unless (find-package "DM_MOTOR::MOTORFEEDBACK")
  (make-package "DM_MOTOR::MOTORFEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude MotorFeedback.msg.html


(defclass dm_motor::MotorFeedback
  :super ros::object
  :slots (_pos _vel _t ))

(defmethod dm_motor::MotorFeedback
  (:init
   (&key
    ((:pos __pos) 0.0)
    ((:vel __vel) 0.0)
    ((:t __t) 0.0)
    )
   (send-super :init)
   (setq _pos (float __pos))
   (setq _vel (float __vel))
   (setq _t (float __t))
   self)
  (:pos
   (&optional __pos)
   (if __pos (setq _pos __pos)) _pos)
  (:vel
   (&optional __vel)
   (if __vel (setq _vel __vel)) _vel)
  (:t
   (&optional __t)
   (if __t (setq _t __t)) _t)
  (:serialization-length
   ()
   (+
    ;; float32 _pos
    4
    ;; float32 _vel
    4
    ;; float32 _t
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _pos
       (sys::poke _pos (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _vel
       (sys::poke _vel (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _t
       (sys::poke _t (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _pos
     (setq _pos (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _vel
     (setq _vel (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _t
     (setq _t (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get dm_motor::MotorFeedback :md5sum-) "cd635028afaa0f6aed3ef11a40a1d7e5")
(setf (get dm_motor::MotorFeedback :datatype-) "dm_motor/MotorFeedback")
(setf (get dm_motor::MotorFeedback :definition-)
      "float32 pos
float32 vel
float32 t
")



(provide :dm_motor/MotorFeedback "cd635028afaa0f6aed3ef11a40a1d7e5")


