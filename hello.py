# assignment: programming assignment 1
# author: Yazmyn Sims
# date: 10/5/2022
# file: hello.py is a program that asks the user to enter user's name,
#       age, and favorite movie and outputs a greeting message that
#       include the information about the user
# input: string data
# output: string data

# use input statements to make prompts (ask questions)
# use a variable age as an integer data type (you should use integer casting)

# use print statements to output user data

# use f-strings or string formatting methods
# use string concatenation and string casting

#get input
print("Hello! What's your name?")
name = input()

age = int (input("What's your age?\n"))

print("What's your favorite movie?")
movie = input()

#increase age
age = age+1

#get output
print (f'Nice to meet you {name}.')
print (f'You will be {age} next year and your favorite movie is {movie}.')
