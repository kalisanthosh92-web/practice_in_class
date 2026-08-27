import random as rd

passwd_length = int(input('Enter the password length: '))

lower = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper = [ i.upper()  for i in lower ]
numbers = [1,2,3,4,5,6,7,8,9,0]

def passwd_gen():
    include_upper = input('Include Uppercase (yes/no): ').lower()
    include_lower = input('Include lowercase (yes/no): ').lower()
    include_numbers = input('Include numbers (yes/no): ').lower()

   @ passwd = rd.choice(lower)+ rd.choice(upper) + rd.choice(numbers)

   for i in passwd_length 