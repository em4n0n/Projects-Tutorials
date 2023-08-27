import matplotlib.pyplot as plt

def fibonacci(n):
  fib = [0, 1]

  for i in range(2, n):
    fib.append(fib[i - 1] + fib[i - 2])

  return fib

# Plot the first 10 numbers in the Fibonacci sequence
fib = fibonacci(10)

# Use the matplotlib.pyplot.plot() function to plot the numbers in the Fibonacci sequence
plt.plot(fib)

# Show the plot
plt.show()