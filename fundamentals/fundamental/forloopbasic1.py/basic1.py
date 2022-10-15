#1 print all integers from 0 to 150
for i in range(0,151):
    print(i)

#2 print all multiples of 5 from 5 to 1000
for i in range(1,1001):
   if i%5==0:
        print(i)

#3 print integers 1 to 100. if divisible by 5, print coding instead. if divisible by 10, print coding dojo
for i in range(1,101):
    if i%10==0:
        print("Coding Dojo")
    elif i%5==0:
        print("Coding")
    else:
        print(i)

#4 add odd integers from 0 to 500,000 and print the final sum
sum=0
for i in range(0,500000):
    if i%2!=0:
        sum+=i
print(sum)

#5 print positive numbers starting at 2018, counting by fours
for i in range(2018,0,-4):
    if i%2==0:
        print(i)

#6 Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers 
# that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum=2
highNum=600
mult=3
for i in range(2,601):
    if i%3==0:
        print(i)
