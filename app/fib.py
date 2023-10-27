"""
Fibonacci number generator
When given a position, the function returns the fibonacci at that position in the sequence.
The zeroth number in the fibonacci sequence is 0. The first number is 1
Negative numbers should return None
"""
def fibonacci(position):
  if(position < 0):
    raise ValueError("Invalid input")
  if(position == 0 or position == 1):
    return position
  return fibonacci(position - 1) + fibonacci(position - 2)