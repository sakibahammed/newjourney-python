first_number = input('Enter the first value : ')
second_number = input('Enter second value : ')
third_number = input('Enter third value P : ')

if first_number > second_number and first_number>third_number:
    print(first_number ,' is the largest number')
elif second_number > first_number and second_number>third_number:
    print(second_number,' is the largest number')    
else:
    print(third_number,' is the largest number')    