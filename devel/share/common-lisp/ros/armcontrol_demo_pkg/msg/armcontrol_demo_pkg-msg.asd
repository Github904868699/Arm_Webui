
(cl:in-package :asdf)

(defsystem "armcontrol_demo_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "hdrarm_msg" :depends-on ("_package_hdrarm_msg"))
    (:file "_package_hdrarm_msg" :depends-on ("_package"))
  ))