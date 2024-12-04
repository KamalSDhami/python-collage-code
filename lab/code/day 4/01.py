#Write a python program to generate a fibonacci series when the serries will start from 0 and 1 and should be less than n consider n =22
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        list_fib = [0, 1]
        while list_fib[-1] + list_fib[-2] < n:
            next_fib = list_fib[-1] + list_fib[-2]
            list_fib.append(next_fib)
        return list_fib   
n = int(input("Enter the number : "))
print (fibonacci_sequence(n))