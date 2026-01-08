import numpy as np

marks = np.array([90,88,30, 78, 66, 49])

print(marks)
print(len(marks))
print(type(marks))
print(marks+2)
print(marks - 4)

#when we print it normally print(marks) it prints alike. But when we add 2 or subtract 4 from the list in np it add and substracts the number from each 
# value. But in case of list it tries to concatenate the number to the list. Also please give me a name for this difference if there is any. 
# The number adds or substract because the array function of an np might already have a loop init.

average = np.mean(marks)
print ("average= ", average)
# difference between using the np.mean func and creating my own function is that the o/p depends on the type of variable we have defined it gives us only 1 decimal value
# but in np.mean case itr gives us a an accurate value down to last decimal.

passed = marks >= 60
print(passed)

print(np.sum(passed))

# It counted the number of true values in the passed variable.

# Day 2 Reflection:
# 1) What felt new or strange?
# Rather than using or creating my own loop and function numpy made the work more easy and conveinient.
# 2) What did numpy make easier?
# Because it has more curated and easy to use function.
# 3) What still confuses me?
# np.sum usage and dept dive in numpy.