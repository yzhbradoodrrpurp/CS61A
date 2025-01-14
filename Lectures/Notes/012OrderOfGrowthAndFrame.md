# 时间复杂度

## $\Theta(n)$ & $O(n)$

$\Theta(n)$, $O(n)$都表示一个函数运行时的时间复杂度，但是存在一些区别。

- $\Theta(n)$表示这个函数时间复杂度的下限。
- $O(n)$表示这个函数时间复杂度的上限。

````python
def memo(f);
	cache = {}

  def memorize(x):
    if x not in cache:
      cache[x] = f(x)
  	return cache[x]

  return memorize


def fibonacci(x):
  if x == 0:
    return 1
  elif x == 1:
    return 1
  else:
    return fibonacci(x - 1) + fibonacci(x - 2)
````

- fibonacci函数的时间复杂度是$\Theta(e^n)$。
- memo(fibonacci)函数的时间复杂度是$\Theta(\lg{n})$。

# 活动帧 & 父帧

- 活动帧：当前正在执行的函数的栈帧，任何一个时刻的活动帧都是唯一的(对于单线程而言)。
- 父帧：活动帧的前一个帧，帧保存着调用当前函数时的执行信息，比如调用该函数时的返回地址和调用参数。

<!--举例而言，当执行fibonacci(2)时，会执行fibonacci(1)和fibonacci(0)。在执行fibonacci(1)时，该函数对应的栈帧就是活动帧，fibonacci(2)的栈帧就是父帧。-->