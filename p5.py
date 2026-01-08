marks = [90, 45, 76, 88, 59]
print(marks)
print(len(marks))
#len() means number of elements in the list basically length of the list. len() is a function returns no. of elements in the list.

for m in marks:
    print(m)
#we used index to print the value at each index of the list.

total = 0
for m in marks:
    total = total + m

average = total / len(marks)
print(average)

#we need to first define total variable because it is inside the loop. I don't know the reason. But according to the way it behaved first we have to define a variable then
#use it inside the loop. total = total + m. Is a function which helps us retain the sum of the elements in the list. Can't recall the precise jargan for this. But
# it keeps the sum for all the value basically each time loop iterates we add new alment to the previous element sum.

passed = 0
for m in marks:
    if m >= 60:
        passed = passed + 1

print("student passed = ", passed) 

#here we calculate how many students have passed by iterating through the last if the element is equal or greater than 60 candidate has passed each time a candidate is passed
#we add 1 to the passed variable and each time loop iterates and fulfill the condition 60 or above we add 1.

# Day 4 Reflection:
# 1) What confused me?
# It was easy nothing too confusing.
# 2) What part felt easy?
# the logic was pretty easy.
# 3) Did I rush anywhere?
# No i didn't rushed.