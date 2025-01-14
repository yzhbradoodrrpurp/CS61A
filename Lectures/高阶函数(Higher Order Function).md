# 高阶函数(Higher Order Function)

高阶函数是一种能够接受其它函数为变量，或者返回一个函数变量的函数。

## 接收函数的情况

````python
def summation(num, function):
	"""
	>>> summation(3, square) // 1^2 + 2^2 + 3^2
	14
	>>> summation(2, cube) // 1^3 + 2^3
	9
	>>> summation(3, increment) // 1+1 + 2+1 + 3+1
	9
	"""
  assert num > 0, 'num must be positive'
  
  summary = 0
  
  for i in range(1, num + 1):
    summary += function(i)

 	return summary

def square(x):
  return x ** 2

def cube(x):
  return x ** 3

def increment(x):
  return x + 1
````

## 返回函数的情况

````python
def make_adder(x):
	"""
	>>> add_5 = make_adder(5)
	>>> add_5(6)
	11
	>>> make_adder(6)(10)
	16
	"""
  return lambda y: x + y

````

## 接收并返回函数的情况

````python
def memory(function):
  cache = {}
  
  def memoryVersion(x):
    if x not in cache.keys():
      value = function(x)
      cache[x] = value

    return cache[x]
  
  return memoryVersion

def fibonacci(x):
	assert x > 0, 'Input must be positive.'
  if x == 1:
    return 1
  if x == 2:
    return 1
  else:
    return fibonacci(x - 1) + fibonacci(x - 2)
  
fibonacci = memory(fibonacci)
````

