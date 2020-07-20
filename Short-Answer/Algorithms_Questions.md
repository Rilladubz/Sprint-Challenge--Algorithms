# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

The run time of a is O(n). Since the while loop is a loop the size
of n will dictate the number of operations proportional to the size of the input.

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

The runtime of b is polynomial aka O(n^c) in this instance O(n^2)
Since the size n has to run through the loop twice in the for & while loop the space/time complexity will grow faster than the size of n. This is not optimal.

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

The run time of c is O(n) in this case since the recursive call only is recurssing and taking 1 away from bunnies if it were used in fibonacci it would be O(2^n) but this is simply returning 2 minus the size of n in a fashion similar to a loop.

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
