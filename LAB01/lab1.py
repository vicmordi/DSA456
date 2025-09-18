
#Function1

def wins_rock_scissors_paper(player, opponent):
    # Convert both to lowercase so casing doesn't matter
    player = player.lower()
    opponent = opponent.lower()

    # Check winning conditions
    if (player == "rock" and opponent == "scissors") \
       or (player == "paper" and opponent == "rock") \
       or (player == "scissors" and opponent == "paper"):
        return True
    else:
        return False




#Function2


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


#Function3

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b



#Function4

def sum_to_goal(numbers, goal):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == goal:
                return numbers[i] * numbers[j]
    return 0


#UpCounter

class UpCounter:
    def __init__(self, step=1):
        self.value = 0
        self.step = step

    def count(self):
        return self.value

    def update(self):
        self.value += self.step


#DownCounter

class DownCounter(UpCounter):
    def update(self):
        self.value -= self.step



# Part B Reflection

# What I liked / did not like about Python:
# I liked that Python code is very simple and easy to read compared to other languages. 
# I did not have to write extra symbols like semicolons, and indentation made the structure clear. 
# I also liked that I could quickly test my functions without much setup. 
# However, one thing I did not like is that Python sometimes hides details in the background, which makes it feel less strict. 
# This can cause errors to show up only when the program is running, instead of being caught early.

# Anything that behaved differently than expected:
# One thing that behaved differently than I expected was how Python handles variables and data types. 
# In C or C++, I am required to declare the type of a variable before using it, but in Python I can just assign a value, 
# and the type is automatically decided. Also, I noticed that Python uses indentation instead of braces {} for blocks of code, 
# which was new to me but became natural after some practice.

# Similarities and differences between Python and C/C++:
# Python and C/C++ are similar in that they both use loops, conditionals, and functions to structure a program. 
# The logic of solving problems, like calculating factorials or Fibonacci numbers, is the same. 
# The difference is mostly in the syntax and strictness. In Python, the code is shorter and requires fewer lines, 
# while in C/C++ I need to declare variables, include headers, and use semicolons and braces. 
# This affects how I write programs because in Python I can focus more on the algorithm itself, 
# while in C/C++ I need to pay more attention to setup and syntax rules.

