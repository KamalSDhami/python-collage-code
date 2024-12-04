import pyfiglet

def pifi(text ):
    print(pyfiglet.figlet_format(text))
#python "sep" parameter in print()

a = 9 
b = 'Aug'
c = 2022
print(a,b,c,sep='-')

#type casting 
num = input("Enter the num : ")
num2 = input("Enter otehr number : ")
pifi(f"Before :  {num + num2}" )
num,num2 = int(num), int(num2)
pifi(f"After : {num + num2 }")
pifi("Hello Bhawesh")
pifi("ayush")