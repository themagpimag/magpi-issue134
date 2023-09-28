# This program prints the numbers from 1 to 100, but replaces multiples of 3 with "Fizz"
# and multiples of 5 with "Buzz".

for i in range(1, 101):
  # Check if the current number is divisible by both 3 and 5.
  if i % 3 == 0 and i % 5 == 0:
    # If so, print "FizzBuzz".
    print("FizzBuzz")
    # A number that is divisible by both 3 and 5 is called a "FizzBuzz" number.

  # Otherwise, check if the current number is divisible by 3.
  elif i % 3 == 0:
    # If so, print "Fizz".
    print("Fizz")
    # A number that is divisible by 3 is called a "Fizz" number.

  # Otherwise, check if the current number is divisible by 5.
  elif i % 5 == 0:
    # If so, print "Buzz".
    print("Buzz")
    # A number that is divisible by 5 is called a "Buzz" number.

  # Otherwise, print the current number.
  else:
    print(i)
    # This is the default case. It prints the number if it is not divisible by 3 or 5.
