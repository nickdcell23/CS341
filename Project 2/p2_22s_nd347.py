# Nicholas Digioia-Celentano
# nd347
# CS341-452, Spring '22, Project 2, Professor Nakayama

# import fileinput 


# using a stack to remember inputs
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
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def pdacheck(string):
    s = Stack()  # initialize the stack
    sym = '+-*/'  # our set of valid symbols
    state = 1  # initial state is  q1
    accept_state = 7  # define our accepting state for easier access
    print('\nInitial State = q{}'.format(state))  # specify what our initial state is

    for i in string:

        # first character MUST be &, check if it is then push onto stack. go state 2
        if i == '&' and state == 1:
            s.push('&')
            state = 2
            print('{}, Ɛ -> &: Current state = q{}'.format(i, state))  # this will make formatting way easier

        # every ( must have a ). remember this ( by pushing it onto stack
        elif i == '(' and state == 2:
            s.push('(')
            state = 2
            print('{}, Ɛ -> (: Current state = q{}'.format(i, state))

        # if a number at state 2, we move to state 3
        elif i.isdigit() and state == 2:
            state = 3
            print('{}, Ɛ -> Ɛ: Current state = q{}'.format(i, state))

        # if a dot at state 2, we move to state 4
        elif i == '.' and state == 2:
            state = 4
            print('{}, Ɛ -> Ɛ: Current state = q{}'.format(i, state))

        # if a number at state 3, we stay at state 3
        elif i.isdigit() and state == 3:
            state = 3
            print('{}, Ɛ -> Ɛ: Current state = q{}'.format(i, state))

        # if a . at state 3, we move to state 5
        elif i == '.' and state == 3:
            state = 5
            print('{}, Ɛ -> Ɛ: Current state = q{}'.format(i, state))

        # if a digit at state 4, we move to state 5
        elif i.isdigit() and state == 4:
            state = 5
            print('{}, Ɛ -> Ɛ: Current state = q{}'.format(i, state))

        # if a digit at state 5, we stay at state 5
        elif i.isdigit() and state == 5:
            state = 5
            print('{}, Ɛ -> Ɛ: Current state = q{}'.format(i, state))

        # if a & at state 5, check if the & is at the top of the stack (beginning of string)
        elif i == '&' and state == 5:
            if s.peek() == '&':
                s.pop()
                state = accept_state  # if it is, accept it. otherwise, crash
            else:
                break
            print('{}, & -> Ɛ: Current state = q{}'.format(i, state))

        # if a symbol at state 5, go back to state 2
        elif i in sym and state == 5:
            state = 2
            print('{}, Ɛ -> Ɛ: Current state = q{}'.format(i, state))

        # if a ) at state 5, check for a ( at top of stack, move to state 6. if not, break
        elif i == ')' and state == 5:
            if s.peek() == '(':
                s.pop()
                state = 6
            else:
                break
            print('{}, ( -> Ɛ: Current state = q{}'.format(i, state))

        # if a ) at state 6, check for a ( at top of stack, stay in state 6. if not, break
        elif i == ')' and state == 6:
            if s.peek() == '(':
                s.pop()
                state = 6
            else:
                break
            print('{}, ( -> Ɛ: Current state = q{}'.format(i, state))

        # if a symbol at state 6, go back to state 2
        elif i in sym and state == 6:
            state = 2
            print('{}, Ɛ -> Ɛ: Current state = q{}'.format(i, state))

        # if a & at state 6, check if & is at top of stack (beginning of string)
        elif i == '&' and state == 6:
            if s.peek() == '&':
                s.pop()
                state = accept_state  # if it is, accept it. otherwise, crash
            else:
                break
            print('{}, & -> Ɛ: Current state = q{}'.format(i, state))

        # any invalid symbols, letters, etc? "Crash"
        else:
            break

    # acceptance state. if state is not 7, something went wrong. tell them it crashed
    if state == 7:
        print("String", string, "is accepted! \n")
    else:
        print("Program crashed at state {} due to invalid character {}".format(state, i))
        print("String", string, "is denied! \n")


# basic i/o for string analyzing
def main():
    while True:
        yesno = input("Would you like to enter a string to analyze? (y/n) ")
        if yesno.lower() == 'n':
            print("Thank you, and goodbye!")
            break
        elif yesno.lower() == 'y':
            string = input("Enter string to analyze: ")
            pdacheck(string)
        else:
            print("Please enter a valid command! (y/n)")

# note to Professor Nakayama
# when writing console output to a .txt file, for some reason the character Ɛ is converted to ?
# when reading my output, assume all ?'s with arrows on either side are the character Ɛ.
# i apologize for the inconvenience


if __name__ == "__main__":
    main()
