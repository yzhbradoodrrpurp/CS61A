# Scheme

Scheme是以Lisp为基础的编程语言，属于函数式编程语言。

## Scheme语言基础

Scheme语言的表达式有以下几种：

- Primitive Expressions: 2, 3.3, true, +, quotient, ...
- Combinations: (quotient 10, 2), (not true), ...

````scheme
// Scheme不关心缩进，也不关心换行，只是为了可读性。
(+ 
 (+ 2 4) 
 (* 3 5)
 )
````

除了数值表达之外，Scheme也可以判断类型：

````scheme
(number? 2)
#t
(number? +)
#f
(zero? 3)
#f
(zero? (+ 2 -2))
#t
(integer? 2.2)
#f
(integer? 7)
#t
````

## Scheme语言进阶

- __(if [predicate] [consequent] [alternative])__
  - predicate成立时，执行consequent；不成立时，执行alternative。

- __(and [a] [b] [c] ...)__

- __(or [a] [b] [c] ...)__

- __(define [symbol] [expression])__
  - 将expression的值定义为symbol。

````scheme
(define pi 3.1415926)
(* pi 2)
// 6.2831852
````

- __(define ([symbol] [formal parameters]) [body])__
  - 定义一个过程（其实就是函数，不过在Scheme中叫做过程），接收变量和返回变量。

````scheme
(define (abs x) 
  (if (< x 0) 
      (- x)
      (x)
    	)
  )

(abs -3)
// 3
````

- __(lambda [formal parameters] [body])__
  - __接收的参数(formal parameters)必须用括号括起来，尽管参数可能只有一个。__


````scheme
(define plus4 (lambda (x) (+ x 4))
````

- __(cond ([predicate]  [consequent]) ([predicate]  [consequent]) ...)__
  - 相当于多重的if-elif-elif-else语句。

````scheme
(cond
 ((> x 10) (print 'big))
 ((> x 5) (print 'medium))
 (else (print 'small))
 )
````

- __(begin ([expression] [expression] ...))__
  - begin可以同时执行括号内多个命令。

````scheme
(cond
 ((> x 10)
  begin((print 'big) (print 'guy))
  )
 ((> x 5)
	begin((print 'medium) (print 'size))
  )
 (else
  begin((print 'small) (print 'light))
  )
 )
````

- __(let (([symbol] [expression])) [body])__
  - let类似于define，但是只是一次性的将symbol和value绑定。
  - __注意let在将symbol和expression绑定时有两个括号。__

````scheme
(let (
      (x 5)
      (y 10)
     )
  (print x)
  (print y)
  (+ x y)
)
````

## Scheme的列表

### 基础使用

Scheme中的列表类似于Python中的链表，它的使用方法如下：

- __(cons [value] [rest])__
  - value表示链表这一个节点的值，rest表示其余的链表。

````scheme
// (2)
(cons 2 nil)
// (2 1)
(cons 2 (cons 1 nil))
// (2 1 3)
(cons 2 (cons 1 (cons 3)))
````

- __(car s)__
  - 返回列表s中的第一个节点的值。

- __(cdr s)__
  - 返回列表中第一个节点以后的节点。
- __nil__
  - 空列表。
- __(list [a] [b] [c] ...)__
  - 可以用list关键字直接构建一个列表，a, b, c, ...都是列表中的值。

同样可以判断一个变量是不是list类型：

````scheme
(define s (cons 2 nil))
(list? s)
#t
(list? (car s))
#f
(list? (cdr s))
#t
````

可以判断一个列表是不是空列表：

````scheme
(null? nil)
#t
(null? 3)
#f
````

### Built-In Functions

- __(append s t)__
  - 返回一个新列表，将t列表追加到s列表后面，不会修改s, t。

````scheme
(define s '(1 2 3 4))
(define t '(5 6 7 8))
(define v (append s t))
// (1 2 3 4 5 6 7 8)
````

- __(map f s)__
  - 对s中的每个元素应用f过程。

````scheme
(define s '(1 2 3 4))
(define t (map even? s))
// (#f #t #f #t)
````

- __(filter f s)__
  - 对s中的每个元素，应用f过程，保留取值为真的元素。

````scheme
(define s '(1 2 3 4))
(define t (filter even? s))
// (2 4)
````

- __(apply f s)__
  - 对s整体使用f过程。

````scheme
(define s '(1 2 3 4))
(apply + s)
10
(apply * s)
24
````

## Quote

在Scheme中，用quote过程(Procedure)表示符号本身。

````scheme
// (a b)
(list (quote a) (quote b))
````

- __(quote [a])__也可以简写为__'[a]__。

<!--注意只有左边有单引号，右边没有。-->

````scheme
// (a b)
(list 'a 'b)
````

- quote可以作用于一个复合表达式，用于创造一个列表。

````scheme
// a
(car '(a b c d))
// (b c d)
(cdr '(a b c d))
````
