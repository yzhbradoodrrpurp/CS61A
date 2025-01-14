(define (ascending? s)
  (if (or (null? s) (null? (cdr s)))
    #t
    (if (> (car s) (car (cdr s)))
      #f
      (ascending? (cdr s))
      )
    )
  )

(define (my-filter pred s)
  (if (null? s)
    s
    (if (pred (car s))
        (cons (car s) (my-filter pred (cdr s)))
        (my-filter pred (cdr s))
      )
    )
  )

(define (interleave lst1 lst2)
  (define (f lst1 lst2 times)
    (cond
      ((null? lst1) lst2)
      ((null? lst2) lst1)
      ((= (modulo times 2) 0) (cons (car lst1) (f (cdr lst1) lst2 (+ times 1))))
      ((= (modulo times 2) 1) (cons (car lst2) (f lst1 (cdr lst2) (+ times 1))))
      )
    )
  (f lst1 lst2 0)
  )

(define (in element s)
  (if (null? s)
    #f
    (if (= element (car s))
      #t
      (in element (cdr s))
      )
    )
  )

(define (no-repeats s)
  (define (f t s)
    (if (null? s)
      t
      (if (in (car s) t)
        (f t (cdr s))
        (f (append t (list (car s))) (cdr s))
        )
      )
    )
  (f (list) s)
  )
