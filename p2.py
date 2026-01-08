# What happened?
#print function prints Hello Pulkit in the output console.
print("Hello Pulkit")

x = 6
y = 9
z =x + y
print(z)
# Why did this work?
# x and y both are int type vars. and there sum is stored in z and print function prints sum of x and y stored in z var.

temp = 30

if temp > 29.99:
    print("cool weather")
else:
    print("hot weather")

# it checks for temperature is lower than 30 it is hot and if above 30 it is cool.

for i in range(6):
    print(i)

#it prints numbers from 0 to 5 because range is from 0 to 6-1=5. prints numbers till 5.

for i in range(20):
    if i%2==0:
        print("Even")
    else:
        print("Odd")
#this program prints number in a loop till 19. i divide it by 2 and if remainder is 0. It is an even number if not 0 it is an odd number.