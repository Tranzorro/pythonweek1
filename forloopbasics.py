# for loops basics
"""
write for loops that can do some basic functions:
loop1: print all int from 0 to 150
loop2: print all the multiples of 5 from 5 to 1000
loop3: print integers 1 to 100, if divisible by 5, print 'coding' instead. if divisible by 10, print 'coding dojo'
loop4: add odd ints from 0 to 500,000 and print the final sum
loop5: print positive numbers starting at 2018, counting down by fours
loop6: set 3 vars lowNum, highNum, mult. iterate in range from low to high printing only multiples of mult.
"""

num1 = 150
num2 = 1000
num3 = 100
num4 = 500000
num5 = 2018
lowNum = 2
highNum = 50
mult = 5
total = 0

for x in range(0,num1+1): #loop 1 print int from 0 to 150
        print(x)

for y in range(5,num2+1): #loop 2 print all multiples of 5 between 5 and 1k
    if y % 5 ==0:
        print(y)

for z in range(1,num3+1): #loop 3 print ints from 1 to 100, if multiple of 5, print coding, else if multiple of 10, print coding dojo
    result = z
    if z % 5 == 0:
        result = "coding"
    if z % 10 == 0:
        result += " dojo"
    print(result)

for a in range(0,num4+1): #loop 4 add odd ints from 0 to 500k and print final sum 
    if not a % 2:
        total += a
print(total) # give me the total result of what the last loop calculated


while num5 >=0: #loop 5 print positive numbers only, counting down by 4 starting at 2018
    print(num5)
    num5-= 4
    if num5 <= 0:
        break

for c in range(lowNum, highNum +1): #loop 6
    if c % mult == 0:
        print(c)