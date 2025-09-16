
(cl:in-package :asdf)

(defsystem "jdq_control-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "jdq_state" :depends-on ("_package_jdq_state"))
    (:file "_package_jdq_state" :depends-on ("_package"))
  ))