#1 countdown-Create a function that accepts a number as an input. Return a new list that counts down by one,
# from the number (as the 0th element) down to 0 (as the last element).
def countdown(num):
    newList=[]
    for i in range(num,-1,-1):
        newList.append(i)
    return newList
print(countdown(10))

#2 print and return-Create a function that will receive a list with two numbers. Print the first value and 
# return the second.
def prPairs(list):
    print(list[0])
    return list[1]
print(prPairs([5,33]))
print(prPairs([0,35]))

#3 first plus length-Create a function that accepts a list and returns the sum of the first value in the list 
# plus the list's length.
sum=0
def fpl(list):
    val1=(list[0])
    sum=val1+len(list)
    return sum
print(fpl([1,3,5,7,9]))

#4 values greater than the second-Write a function that accepts a list and creates a new list containing only 
# the values from the original list that are greater than its 2nd value. Print how many values this is and then
# return the new list. If the list has less than 2 elements, have the function return False
newList=[]
def valg2(list):
    if len(list)<2:
        return False
    for i in list:
        if i>list[1]:
            newList.append(i)
    print(len(newList))
    return newList

print(valg2([36,31,27,9,3]))
print(valg2([3,9,31,39,27]))
print(valg2([3]))


#5 this length, that value-Write a function that accepts two integers as parameters: size and value. The function 
# should create and return a list whose length is equal to the given size, and whose values are all the given value.
def lv(size='',value=''):
    lvlist=[]
    for i in range(size):
        lvlist.append(value)
    return lvlist

print(lv(3,5))
print(lv(2,7))