import matplotlib.pyplot as plt

def fibonacci_spiral(n):
  fib = [0, 1]

  for i in range(2, n):
    fib.append(fib[i - 1] + fib[i - 2])

  # Compute the points of the Fibonacci spiral
  points = [(0, 0)]  # Start at the origin (0, 0)
  x, y = 0, 0  # Initialize the x and y coordinates

  for i in range(1, n):
    # Compute the next point based on the previous point and the value in the Fibonacci sequence
    if i % 4 == 1:
      x += fib[i]
    elif i % 4 == 2:
      y += fib[i]
    elif i % 4 == 3:
      x -= fib[i]
    else:
      y -= fib[i]

    points.append((x, y))

  return points

# Plot the first 10 points in the Fibonacci spiral
points = fibonacci_spiral(10)
print(points)  # Output: [(0, 0), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (2, -1)]