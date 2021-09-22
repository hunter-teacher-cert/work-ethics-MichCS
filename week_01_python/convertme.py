#no library or public class/void needed

#define function (factorial)
#initialize product 
#create while loop. For this problem, a for loop cannot start from from a larger to smaller number
#return product outside of loop to see answer
def factorial(n):
   prod = 1
   while n > 1:
       prod = prod * n
       n = n - 1
   return prod

#check to see if the condition is true and then return it. Otherwise, return fib. sequence.
def fib(n):
   if (n < 2):
       return 1;
   else:
       return fib(n - 1) + fib(n - 2);

print("Good News Everyone!")
print(f"7! = {factorial(7)}" )
print(f”fib(7) = {fib(7)}”_)
