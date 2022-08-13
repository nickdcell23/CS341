# Nicholas Digioia-Celentano
# nd347
# CS341-452 Project 1 

import sys
from queue import Queue

# A stack seems like an easy way to make this program work
# We can make functions for each state in the DFA and do stack.pop on each call
class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def main():

    # Information requested by instructor
    print("Project 1 for CS 341 \n Section number: 452 \n Semester: Spring 2022 \n Written by: Nicholas Digioia-Celentano, nd347 \n Instructor: Marvin Nakayama, marvin@njit.edu")

    # Have user select if they want to enter a string, analyze it if yes
    yesno = input("Would you like to enter a string for analyzing? (y/n): ")
    while (yesno != 'y' and yesno != 'n'):
        print("Invalid. Please write y or n")
        yesno = input("Would you like to enter a string for analyzing? (y/n): ")

    while yesno == 'y':
        user_input = input("Please enter your string: ")
        stack = Stack()
        print(f"{user_input}")

        # Push the string backward so first in first out can be achieve using stack
        for i in user_input[::-1]:
            stack.push(i)
            result = True;

        result = startState(stack)
        if result:
            print("String is valid!\n")
        else:
            print("String is invalid!\n")

        # Ask user if they want to enter another string
        yesno = input("Would you like to enter the string? (y/n): ")
        while (yesno != 'y' and yesno != 'n'):
            print("Invalid. Please write y or n")
            yesno = input("Would you like to enter a string for analyzing? (y/n): ")

        # EMPTY THE STACK!!!
        emptyStack(stack)

# And here's our starting state, q0
def startState(stack):

    print("Start state: q0")

    # Empty check
    if (stack.isEmpty()):
        return False
    nextchar = stack.peek().lower()

    if (nextchar.isalpha()):
        return q1(stack)

    return trapState(stack)

# State q1
def q1(stack):

    print(f"{stack.pop()} --- State: q1")

    # Empty check
    if (stack.isEmpty()):
        return False
    nextchar = stack.peek().lower()

    if (nextchar.isalpha()):
        return q1(stack)

    elif (nextchar == '.'):
       return q2(stack)

    elif (nextchar == '@'):
        return q3(stack)

    return trapState(stack)

# State q2
def q2(stack):

    print(f"{stack.pop()} --- State: q2")

    # Empty check
    if (stack.isEmpty()):
        return False
    nextchar = stack.peek().lower()

    if (nextchar.isalpha()):
        return q1(stack)

    return trapState(stack)


# State q3
def q3(stack):

    print(f"{stack.pop()} --- State: q3")

    # Empty check
    if (stack.isEmpty()):
        return False
    nextchar = stack.peek().lower()

    if (nextchar.isalpha()):
        return q4(stack)

    return trapState(stack)

# State q4
def q4(stack):

    print(f"{stack.pop()} --- State: q4")

    # Empty check
    if (stack.isEmpty()):
        return False
    nextchar = stack.peek().lower()

    if (nextchar.isalpha()):
        return q4(stack)

    elif (nextchar == '.'):
        return q5(stack)

    return trapState(stack)

# State q5
def q5(stack):

    print(f"{stack.pop()} --- State: q5")

    # Empty check
    if (stack.isEmpty()):
        return False
    nextchar = stack.peek().lower()

    if (nextchar == 'o'):
        return q6(stack)

    elif (nextchar.isalpha()):
        return q3(stack)

    return trapState(stack)

# State q6
def q6(stack):

    print(f"{stack.pop()} --- State: q6")

    # Empty check
    if (stack.isEmpty()):
        return False
    nextchar = stack.peek().lower()

    if (nextchar == 'r'):
        return q7(stack)

    elif (nextchar == '.'):
        return q5(stack)

    elif (nextchar.isalpha()):
        return q4(stack)

    return trapState(stack)

# State q7
def q7(stack):

    print(f"{stack.pop()} --- State: q7")

    # Empty check
    if (stack.isEmpty()):
        return False
    nextchar = stack.peek().lower()

    if (nextchar == 'g'):
        return q8(stack)

    elif (nextchar == '.'):
        return q5(stack)

    if (nextchar.isalpha()):
        return q4(stack)

    return trapState(stack)

# State q8
def q8(stack):

    print(f"{stack.pop()} --- State: q8")

    # Empty check
    if (stack.isEmpty()):
        return True
    nextchar = stack.peek().lower()

    if (nextchar == '.'):
        return q5(stack)

    elif (nextchar.isalpha()):
        return q4(stack)

    return trapState(stack)

# Function used to empty stack
def emptyStack(stack):

    while (not stack.isEmpty()):

        stack.pop()

# Our trap state, aka q9
def trapState(stack):

    print("Trap State!")

    while not stack.isEmpty():
        print(f"{stack.pop()} --- Trap State: q9")

    return False

if __name__ == "__main__":
    main()
