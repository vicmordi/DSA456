#Function1


def function1(number):

	total = 0                 #1
	
	for i in range(number):   #n
	
		x = i + 1             #2n
		
		total += x * x        #3n   
 
	return total              #1

T(n) = 1 + n + 2n + 3n + 1

T(n) is O(n)


#Function2

def function2(number):

	return (number * (number + 1) * (2 * number + 1)) // 6     #6

T(n)= 6

T(n) is O(1)


#Function3

def function3(list):

	n = len(list)                    #1
	
	for i in range(n - 1):           #n-1
	
		for j in range(n - 1 - i):   #(n-1) + (n-2) + ....... + 1
		
			if list[j] > list[j+1]:  #2 * (n-1) + (n-2) + ....... + 1
			
				tmp = list[j]        #(n-1) + (n-2) + ....... + 1
				
				list[j] = list[j+1]  #(n-1) + (n-2) + ....... + 1
				
				list[j + 1] = tmp    #(n-1) + (n-2) + ....... + 1

T(n) = 1 + n -1 + n-1 + n-2 + ....... + 1 + 2 * n-1 + n-2 + ....... + 1 + n-1 + n-2 + ....... + 1 + n-1 + n-2 + ....... + 1

T(n) is O(n^2)

#Function4

def function4(number):

	total = 1                      #1
	
	for i in range(1, number):     #n
	
		total *= i + 1             #3n
		
	return total                   #1

T(n) = 1 + n + 3n + 1

T(n) is O(n)



| Team member        | Timing for fibonacci (s)       | Timing for sum_to_goal       |
| ------------------ | -----------------------------: | ---------------------------: |
| Victor Mordi (Me)  |        0.000005600042641162872 |          0.28291020006872714 |




| function        |             fastest (s) |             slowest (s) | difference (s) |
| --------------- | ----------------------: | ----------------------: | -------------: |
| fibonacci       | 0.000005600042641162872 | 0.000005600042641162872 |            0.0 |
| sum_to_goal     |     0.28291020006872714 |     0.28291020006872714 |            0.0 |





Reflection

1. What differences did you see between the fastest and slowest versions?
For the fibonacci function, the fastest solutions were the iterative ones (like the version above), which build the sequence step by step. The slowest solutions were usually recursive, since recursion recalculates the same values many times. For the sum_to_goal function, the version that used a double loop (like above) was slower on long lists, while versions that used a dictionary or set to check complements ran faster because they avoided nested loops.

2. Was there a difference in terms of the usage of space resources?
Yes. Recursive Fibonacci uses more memory because each function call is placed on the call stack, while the iterative version only needs two variables (a and b). For sum_to_goal, the double-loop version used almost no extra memory, while the dictionary-based version needed extra space to store values, but in return it gained speed.

3. What sort of conclusions can you draw based on your observations?
The main conclusion is that efficiency depends on the approach, not just the correctness of the code. Iterative Fibonacci is much more efficient than recursive Fibonacci, and for sum_to_goal, trading memory for speed with a dictionary can make the function faster. This shows that when writing programs, it is important to consider both time complexity (speed) and space complexity (memory usage) to pick the most suitable solution.

