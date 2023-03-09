


from ast import Num


color = ['red' , 'blue','green']

#print(color[-20])


# organising or a box of python

box = ['python' , 3.1241,933,'sakib']
# print(type(box[0]))
# print(type(box[1]))
# print(type(box[2]))
# print(type(box[3]))


# append means adding array element


color.append('tomato')
#print(color)
color.append('light-Blue')
# print(color)




#extend means adding a very new element to the existing array



color.extend(box)
# print(color)
# print(len(color))


# removing items from array or list(in python array is called list)

# color.remove('tomato')
# color.remove('sakib')
# color.remove(933)
# color.remove('python')
# color.remove('red')
# print(color)


# array theke kono kichu bad deyar somoi jodi remove use kori tahole array er element er name use korte hobe.

# del use korle array element er index jante hbe
# del color[0]
# del color[-1]
# del color[-3]
# print(color)

# del color[1:4]
# print(color)


#note 

# del color(2:4) evabe likhle list er 2,3,4 index e thaka item gula muche jaabe just 4 index e thka element ta muchbe na


# list theke item ber kore ota k use korar jnne pop mathod use kora hoi.

# poped = color.pop(2)
# print(poped)


# print(color)


# poped = color.pop()
# print(poped)

# print(color)





# Sorting in list

# .short() is like sorting in assending order

# choto theke boro

# number = [4,2,6,7,8,20,190,23,191]
# number.sort()

# print(number)

# # for sorting in decending order 

# # boro theke choto ==== simply short function e parameter hesebe ===== (reverse = True) likhte hoi
# number.sort(reverse=True)
# print(number)


# sonkhar pashapashi word o sort kora jaai , string o sort kora jai

alphabet = ['e','a' ,'i','u','o']
# alphabet.sort();
# print(alphabet)


friend = ['shuvo','tuhin','tanvir','dipu','siyam']
# friend.sort()
# print(friend)

# # ekhane mainly first word ta k aim kore sort kora hoeyeche



# # ulta kore sorting korar jnne reverse = true use kora hoi

# friend.sort(reverse=True)
# print(friend)

# list theke shob item muche felar jnne clear use kora hoi


# friend.clear()
# print(friend)




# array k ultanor jnne reverse() use kora hoi

# friend.reverse()
# print(friend)



 # to create a more  list together



friend = ['shuvo','tuhin','tanvir','dipu','siyam']

alphabet = ['e','a' ,'i','u','o']

new_list = friend + alphabet
print(new_list)