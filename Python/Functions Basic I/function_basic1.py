
#1
def a():
    return 5
print(a()) 
#prediction (5)

#2
def a():
    return 5
print(a()+a())
#prediction (10)

#3
def a():
    return 5
    return 10
print(a())
#prediction (15) I thought it will give return twice but it turned out that the first return is the one will work. the correct answer is (5)

#4
def a():
    return 5
    print(10)
print(a())
#prediction (5) Because: - print(10) is inside the function and it won't work, - it already got return, the print function is the one outside it will work.
 
#5
def a():
    print(5)
x = a()
print(x)
#prediction (5) I thought it will take the two print since x = a(), So it's None is the correct answer. Why ? the second print cancels the first one and since x has no value it will output (None).

#6
#def a(b,c):
#   print(b+c)
#print(a(1,2) + a(2,3))
#prediction (None)  But it gave an output of (3)(5)... the print(b+c) worked but it gave an error after because it gave null

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#prediction (7)  #The output is (25) because the integers treated as a str so it will be ("2" + "5") = (25)

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
#prediction (10)  because b = 100 and b < 10 (less than 10) so if its true return (5) and it's False so it return (10) so print(a()) will output (10).

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3)) #1
print(a(5,3))  #2
print(a(2,3) + a(5,3))  #3
#prediction1 (7) Because total is less than (7) so it will return (7)
#prediction2 (14)  Because total is greater than (7) so it will return (14)
#prediction3 (21)  Because (7) + (14) 

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
#prediction (8) Because it has return and total of b+c with the givin integers it will output (8)

#11
b = 100
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
#prediction 100, 100, 300, 100 

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
#prediction 500, 500, 300, 500

#13
b = 500 
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
#prediction 500, 500, 300, 300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
#prediction 1, 3, 2

#15 
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
#prediction 1, 3, 5, 10