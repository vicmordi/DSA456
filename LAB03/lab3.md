#Analysis
#Function1

def function1(value, number):
	if (number == 0):      #1
		return 1           #1
	elif (number == 1):    #1
		return value       #1
	else:
		return value * function1(value, number-1)     #2 + T(n-1)

#T(n) = 1 + 1 + 1 + 1 + 2 + T(n-1) = 6 + T(n-1)
#T(n-1) = 6 + T(n-2)
#T(n-2) = 6 + T(n-3)
...............
#T(1) = 2

#T(n) = 6 + T(n-1) = 6 + 6 + T(n-2) = 6 + 6 + 6 + T(n-3)....... T(1)
#T(n) = 6(n-1) + 2 = 6n - 6 + 2 = 6n - 4
#T(n) is O(n)

#Function2

def recursive_function2(mystring,a, b):
	if(a >= b ):                            #1
		return True                         #1
	else:
		if(mystring[a] != mystring[b]):     #1
			return False                    #1
		else:
			return recursive_function2(mystring,a+1,b-1)     #2 + T(n-1)
 
def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1) #6n -4 + 2 T(n) is O(n)

#T(n) = 1 + 1 + 1 + 1 + 2 + T(n-1) = 6 + T(n-1)
#T(n-1) = 6 + T(n-2)
#T(n-2) = 6 + T(n-3)
..........
#T(1) = 2

#T(n) = 6 + T(n-1) = 6 + 6 + T(n-2) = 6 + 6 + 6 + T(n-3).........T(1)
#T(n) = 6(n-1) + 2 = 6n - 6 + 2 = 6n -4
#T(n) is O(n)


#Function3

def function3(value, number):
    if (number == 0):             # 1
        return 1                  # 1
    elif (number == 1):           # 1
        return value              # 1
    else:
        half = number // 2        # 2
        result = function3(value, half)   # 1 + T(n/2)
        if (number % 2 == 0):     # 2
            return result * result        # 1
        else:
            return value * result * result   # 2


#T(n) = 1 + 1 + 1 + 1 + 2 + 1 + T(n/2) + 2 + 1 + 2 = 12 + T(n/2)
#T(n/2) = 12 + T(n/4)
#T(n/4) = 12 + T(n/8)

#T(n) = 12 + T(n/2) = 12 + 12 + T(n/4) = 12 + 12 + 12 + T(n/8).......
#T(n) is O(logn)



#Reflection

#1. How do I approach writing recursive functions?
#When I write a recursive function, the first thing I do is figure out the base case the simplest situation where I can return an answer directly without calling the function again. 
#After that, I think about how to break the bigger problem into a smaller version of the same problem. Each recursive call must move closer to the base case, 
#otherwise it will loop forever. I usually test it on small inputs first to make sure the function stops correctly and builds up the right answer.

#2. How do I analyze recursive functions?
#To analyze a recursive function, I write down how much work is done at each step and then set up a recurrence relation (for example, T(n) = T(n-1) + 5). 
#Then I expand it step by step until it reaches the base case. This shows me the total number of operations and helps me find the Big-O complexity.

#3. How is it different from analyzing non-recursive functions? How is it the same?
#The difference is that for recursive functions, I have to think in terms of a recurrence and expansions, while for non-recursive functions I usually just count loop operations directly. 
#The similarity is that in both cases, I’m still counting operations, summing them up, and then simplifying to Big-O notation. 
#The goal is the same: to measure efficiency in terms of time and space.