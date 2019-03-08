'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: Eddie H. Agic
1. Write a Python program that will use a FOR loop to print your name
     10 times, and then the word Done at the end.
 '''

'''
  2. Write a Python program that will use a FOR loop to print Blue
     and then White 20 times. (Blue White Blue White Blue White... all on separate lines.
     Don't use \n.)
'''
for i in range(10):
    print("Blue")
    print("White")
'''
  3. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(2,101):
    if i%2==0:
        print(i)
'''
  4. Write a Python program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
while True:
    print("10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nBlast off!")
    break
'''
  5. There are three things wrong with this program. List each.

     print("This program takes three numbers and returns the sum.")
     total = 0
     for i in range(3):
         x = input("Enter a number: ")
         total = total + i
     print("The total is:", x)
'''
#input INTEGER; total + x, not i; print total, not x
'''
  6. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
print(random.randrange(1,11))
'''
  7. Write a program that prints a random floating point number somewhere between
     1 and 10 (inclusive). Do not make the mistake of generating a random number from
     0 to 10 instead of 1 to 10.
'''
print(float(random.randrange(1,11)))
'''
  8. Write a Python program that will:

     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the number entries equal to zero,
     and the number of negative entries. Use an if, elif, else chain, not just three
     if statements.

'''
total = 0
for i in range(7):
    x = int(input("Give me a number: "))
    total = total + x
print(total)

