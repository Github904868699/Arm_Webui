
(cl:in-package :asdf)

(defsystem "dm_motor-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "MotorFeedback" :depends-on ("_package_MotorFeedback"))
    (:file "_package_MotorFeedback" :depends-on ("_package"))
    (:file "hdrarm_msg" :depends-on ("_package_hdrarm_msg"))
    (:file "_package_hdrarm_msg" :depends-on ("_package"))
  ))