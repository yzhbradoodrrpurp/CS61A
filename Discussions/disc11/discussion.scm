; -*- coding = utf-8 -*-
; @Time: 2025/1/16 14:46
; @Author: Zhihang Yi
; @File: discussion.py
; @Software: PyCharm

; The mystery-macro replaces all instances of an old symbol
; with a new expression before evaluating the expression expr.

(define-macro (mystery-macro expr old new)
    (mystery-helper expr old new))

(define (mystery-helper e o n)
  (if (pair? e)
      (cons (mystery-helper (car e) o n) (mystery-helper (cdr e) o n))
      (if (eq? e o) n e)))


; Implement the assign Scheme macro, which takes in two symbols
; sym1 and sym2 as well as two expressions expr1 and expr2.
; It should bind sym1 to the value of expr1 and sym2 to the value of
; expr2 in the environment from which the macro was called.

(define-macro (assign sym1 sym2 expr1 expr2)
  `(begin
     (define ,sym1 ,expr1)
     (define ,sym2 ,(eval expr2))
     )
  )

(assign x y (+ 1 1) 3)
(assign x y y x)
(expect x 3)
(expect y 2)


; Define the macro switch, which takes in an expression expr
; and a list of pairs called cases where the first element of
; the pair is some number and the second element is a single expression.
; switch will evaluate the expression contained in of cases that
; corresponds to the number that expr evaluates to.

(define-macro (switch expr cases)
    `(let ((val ,expr))
	  ,(cons
	    'YOUR-CODE-HERE
	    (map (lambda (case) (cons
	           'YOUR-CODE-HERE
		       (cdr case)))
		     cases))))
