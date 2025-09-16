;; Auto-generated. Do not edit!


(when (boundp 'jdq_control::jdq_state)
  (if (not (find-package "JDQ_CONTROL"))
    (make-package "JDQ_CONTROL"))
  (shadow 'jdq_state (find-package "JDQ_CONTROL")))
(unless (find-package "JDQ_CONTROL::JDQ_STATE")
  (make-package "JDQ_CONTROL::JDQ_STATE"))

(in-package "ROS")
;;//! \htmlinclude jdq_state.msg.html


(defclass jdq_control::jdq_state
  :super ros::object
  :slots (_USB1 _USB2 _USB3 _USB4 _USB5 _USB6 _USB7 _USB8 ))

(defmethod jdq_control::jdq_state
  (:init
   (&key
    ((:USB1 __USB1) "")
    ((:USB2 __USB2) "")
    ((:USB3 __USB3) "")
    ((:USB4 __USB4) "")
    ((:USB5 __USB5) "")
    ((:USB6 __USB6) "")
    ((:USB7 __USB7) "")
    ((:USB8 __USB8) "")
    )
   (send-super :init)
   (setq _USB1 (string __USB1))
   (setq _USB2 (string __USB2))
   (setq _USB3 (string __USB3))
   (setq _USB4 (string __USB4))
   (setq _USB5 (string __USB5))
   (setq _USB6 (string __USB6))
   (setq _USB7 (string __USB7))
   (setq _USB8 (string __USB8))
   self)
  (:USB1
   (&optional __USB1)
   (if __USB1 (setq _USB1 __USB1)) _USB1)
  (:USB2
   (&optional __USB2)
   (if __USB2 (setq _USB2 __USB2)) _USB2)
  (:USB3
   (&optional __USB3)
   (if __USB3 (setq _USB3 __USB3)) _USB3)
  (:USB4
   (&optional __USB4)
   (if __USB4 (setq _USB4 __USB4)) _USB4)
  (:USB5
   (&optional __USB5)
   (if __USB5 (setq _USB5 __USB5)) _USB5)
  (:USB6
   (&optional __USB6)
   (if __USB6 (setq _USB6 __USB6)) _USB6)
  (:USB7
   (&optional __USB7)
   (if __USB7 (setq _USB7 __USB7)) _USB7)
  (:USB8
   (&optional __USB8)
   (if __USB8 (setq _USB8 __USB8)) _USB8)
  (:serialization-length
   ()
   (+
    ;; string _USB1
    4 (length _USB1)
    ;; string _USB2
    4 (length _USB2)
    ;; string _USB3
    4 (length _USB3)
    ;; string _USB4
    4 (length _USB4)
    ;; string _USB5
    4 (length _USB5)
    ;; string _USB6
    4 (length _USB6)
    ;; string _USB7
    4 (length _USB7)
    ;; string _USB8
    4 (length _USB8)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _USB1
       (write-long (length _USB1) s) (princ _USB1 s)
     ;; string _USB2
       (write-long (length _USB2) s) (princ _USB2 s)
     ;; string _USB3
       (write-long (length _USB3) s) (princ _USB3 s)
     ;; string _USB4
       (write-long (length _USB4) s) (princ _USB4 s)
     ;; string _USB5
       (write-long (length _USB5) s) (princ _USB5 s)
     ;; string _USB6
       (write-long (length _USB6) s) (princ _USB6 s)
     ;; string _USB7
       (write-long (length _USB7) s) (princ _USB7 s)
     ;; string _USB8
       (write-long (length _USB8) s) (princ _USB8 s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _USB1
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _USB1 (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _USB2
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _USB2 (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _USB3
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _USB3 (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _USB4
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _USB4 (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _USB5
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _USB5 (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _USB6
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _USB6 (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _USB7
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _USB7 (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _USB8
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _USB8 (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get jdq_control::jdq_state :md5sum-) "ce22d24026240afb77c18e56ea2ac5ba")
(setf (get jdq_control::jdq_state :datatype-) "jdq_control/jdq_state")
(setf (get jdq_control::jdq_state :definition-)
      "string USB1
string USB2
string USB3
string USB4
string USB5
string USB6
string USB7
string USB8

")



(provide :jdq_control/jdq_state "ce22d24026240afb77c18e56ea2ac5ba")


