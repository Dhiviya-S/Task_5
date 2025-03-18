##USE LAMBDA TO FILTER OUT PEOPLE UNDER 18##
details=[{"name":"Anne","age":18},
    {"name":"Frank","age":20},
    {"name":"Tom","age":13},
    {"name":"Alice","age":25},
    {"name":"Bob","age":16}] #List of dictionary with name and age keys
print("List of Dictionary:\n",details)
under_age=list(filter(lambda x:x["age"]<18,details)) #filter(function,iterable); filters the people under 18 and prints as list
print("Under 18:",under_age)
max_age=list(filter(lambda x:x["age"]>=18,details)) #filters people of age above 18
print("Above 18:",max_age)
print()

##PRODUCT OF NUMBERS IN LIST##
import functools #importing functools to use reduce(function,iterable)
list_num=[9,8,3,5,6,2]
product = functools.reduce(lambda x, y: x * y, list_num) #reduce() applies multiply function to all the elements in iterable(list)
print("Product of numbers in list:",product) #Prints product of all numbers
print()

##SQUARES OF EVEN NUMBERS IN A LIST##
list1=[3,4,8,2,9,12]
new_list=list(filter(lambda x:x%2==0,list1)) #lambda(arguments:expression) x%2==0 returns even numbers in list
print("List of even numbers:",new_list)
square=[num*num for num in new_list] #Performs square of numbers in list
print("Square of even numbers in list:",square)
print()

##TO CHECK IF GIVEN STRING IS A NUMBER##
a=input("Enter a string:") #input from user
#isnumeric returns "True" if the given string is a number and "False" if string is not a number
#Here it displays message as Given string contains number or not
new_string=lambda x:"Given string is a number" if x.isnumeric() else "Given string is not a number"
print(new_string(a)) #passing input 'n' to lambda function and prints the output
print()

##TO EXTRACT YEAR,MONTH AND DAY FROM DATETIME OBJECT##
from datetime import datetime #Importing datetime module
datetime_object = datetime.strptime("23AUG1987","%d%b%Y") ##datetime.strptime(date,format)
print("Year: ", datetime_object.year) #Extracts year from the given date (%Y-Year)
print("Month: ", datetime_object.month)#Extracts month from the given date(%b-Month)
print("Day: ", datetime_object.day)#Extracts day from the given date(%d-Day)
print()

##FIBONACCI SERIES UPTO n TERMS##
n = int(input("Enter a number to generate fibonacci series:")) #Input as integer
fibonacci=[0,1] #List contains 0,1 each fibonacci series starts with 0 and 1
##It adds the data in the list from last two positions using indexing -1 represents last value and -2 represents penultimate value.
##For 'n' terms of series the range of values starts from 2 to n since [0,1] is already considered
list(map(lambda i:fibonacci.append(fibonacci[-2]+fibonacci[-1]),range(2,n))) #map(function,iterable) provides the modified list by applying lambda function
print(fibonacci) ##Appended data gets printed as list

