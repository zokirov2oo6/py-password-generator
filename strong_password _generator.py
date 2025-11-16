import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','+']

print("Welcome to the PyPassword Generator !")
nr_letters = int(input("How many letters would you like to generate? \n "))
nr_numbers = int(input("How many numbers would you like to generate? \n "))
nr_symbols = int(input("How many symbols would you like to generate? \n "))

password_list=[]
for char in range (0,nr_letters):
    password_list+=random.choice(letters)

for char in range (0,nr_numbers):
    password_list+=random.choice(numbers)

for char in range (0,nr_symbols):
    password_list+=random.choice(symbols)
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for char in password_list:
    password += char
print(f"Your password is: {password}")