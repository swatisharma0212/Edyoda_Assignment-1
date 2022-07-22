'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

numbers = list(map(int,input().split(",")))
 
even_count, odd_count = 0, 0
 
# iterating each number in list
for num in numbers:
     
    # checking condition
    if num % 2 == 0:
        even_count += 1
 
    else:
        odd_count += 1
         
print("Number of even numbers: ", even_count)
print("Number of odd numbers: ", odd_count)