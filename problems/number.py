from re import I


number = float(input('Enter marks : '))
if number > 90 : 
    print('A')
elif number > 80 and  number<=89:
    print('B')  
elif number >=60 and number <=79:
    print('C')    
else:
    print('D')    