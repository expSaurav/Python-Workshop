print("snake")

y=5
print(y)

print(type(y))
x="hey its python"

'''check palindrome'''

print(x)

print(type(x))


if(x==y):
    print("x nd y are equal")
else:
    print("both are not equal")
    

print(5 is 6)

for i in range(0,10,1):
    print(i+1)

while(i<20):
    i=i+1
    print(i)

'''code to check odd or even'''

x=int(input("Enter no. to check odd or even"))
if(x%2==0):
    print( x, " is even number")
else: print(x, " is odd number")

'''program to reverse a string'''
def reverseString(y):
    strlen=len(y)
    for i in range(strlen-1,-1,-1):
        print(y[i],end="")
        
y="hellogc"
reverseString(y)



    
