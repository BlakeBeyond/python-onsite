'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound. Also, calculate the average of numbers.
	Print the results to the console.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
		The average is: 50.5
'''

lower = int(input("give me the lower range number: "))
upper = int(input("give me the upper range number: "))
list_=[]
for i in range(lower,upper):
    list_.append(i)
sum_list = sum(list_)
print(sum_list)
print(sum_list / len(list_))
