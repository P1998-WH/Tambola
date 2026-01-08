def add(x, y):
    return x+y

result = add(4,5)
print(result) 
#I created a function add with two variables as input and later returned the sum of the variables.
# then created another variable where i pass value in the add function and stoe the o/p in result variable.
#then print the output of result var in the console.

def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False

is_even(5)
is_even(8)

# I have created a function to check if the given variable is an even or an odd number. The logic says that we divide the given value with 2
#if the remainder is 0 then number is even else it is odd. In num first it check for 5 and then for 8. First it will return False
#and for second case i.e.8 it will return True.

def check_num(n):
    for i in range(n):
        if i%2 == 0:
            print(i, "is an Even number")
        else:
            print(i, "is an Odd number")

check_num(10)
#Below I have return the use of loop and if condition to check if the number is an Odd and even. I use modulus to check if a number divisible by 2 .
# leaves 0 as a remainder. If True it returns number along with the information if it is odd or even.


# Day 2 reflection:
# 1) What felt easy?
#Ans Whole excercise felt easy.
# 2) What confused me?
#Ans Nothing in excercise confused me.
# 3) Did I read my IF conditions correctly?
# ANs: Yes
# 4) Where did I make mistakes?
# Ans calling functions without printing the result. in is_even function.