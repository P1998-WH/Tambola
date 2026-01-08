def grade(num):
    if num >= 90:
        return "A"
    elif num >= 75:
        return "B"
    elif num >= 60:
        return "C"
    else:
        return "Fail"

print(grade(74))
print(grade(32))
print(grade(98))

#in grade function it takes a variable. Depending on the number it will check among different condition if it meets the condition it will return a string
#for each condition it will check if number is greater or equal to 90, 75, 60 it will return string(Grade). THEN it will print the string. I have learnt how to call
#a function and print the return valiue with this. It is a grading system via a function.

# 1) Why did 92 get "A"?
# Ans: Because got A because it fullfils the first condition the variable is greater than or equal to 90. 
# 2) Why did 70 get "C"?
# Ans: Because it fulfills the second condition greater than or equal to 60.
# 3) Why did 40 get "Fail"?
#ans: It doesn't fulfills the above three conditions.

def can_vote(age):
    if age >= 18 and age <=90 :
        print("can vote")
    elif age > 90:
        print("can't vote(too old) ")
    else:
        print("too young to vote")

can_vote(77)
can_vote(13)
can_vote(98)

# can vote function checks if the age is right to vote or he/she is young or old. and then it prints the correct message after checking the codition.
# What mistake I made:
# 1) Used & instead of and
# 2) Overlapping ranges
#Did you understand why & was wrong?
#Ans Yes because & is a the operator to perform AND logic between two variables. I mistook logic operator for bitwise operator.
#Did the range logic (ordering conditions) make sense?
#yes. But i wrote my own logic. My logic was correct for 1st line if we keep aside the operator mistake. 2nd line has a flaw i was using = in both which was incorrect
#this mistake will help me learn about being more attentive while writing the logic in the code.

def max_of_two(a,b):
    if(a>b):
        return a
    elif a==b:
        return 0
    else:
        return b

print(max_of_two(8,8))
print(max_of_two(9,8))
print(max_of_two(8,9))

#in this function max_of_two it will return the greater number out of 2 variables it is provided with. In case both variables are equal which is a possibility it will
# return 0. then i print the value which is greater using the print function. 

# Day 3 Reflection:
# 1) Which function was hardest and why?
#Ans: they were all easy but 2nd function can_vote made me think about my logical skills. As i wrote the logic i first used & as I use in C++. So it was a 
#mistake. 2nd i was check in both condition if age is = to 90. so that was also a mistake, Since I learned it i won't forget it.
# 2) Did I confuse return vs print at any point?
# No. Return doesn't print the value it returns the variable. Whereas print function priunts the value in console.
# 3) Where did I hesitate?
# I didn't hesitate it was an honest mistake.