#assignment-2 on conditional statement,datasets,function and so on 
#########################################################################
# 1.conditional statement:

n=int(input("enter number:"))
if n%2==0:
    print("even")
else:
    print("odd")  


#########################################################################      
#2.largest of three numbers:

a=10
b=62
c=52

if a<b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)
##########################################################################
#3.leap year:
 
year=int(input("enter the year:"))
if year % 400 ==0:
    print("leap year")
else:
    print("not leap year") 

###########################################################################
#4.grade calculator:

marks=int(input("enter the marks:"))
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>70:
    print("Grade C")
elif marks>=60:
    print("Grade D")
else:
    print("Fail")     

############################################################################
#5.positive,negative,or zero

n=int(input("enter the number:"))
if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("zero")        

############################################################################
#6.sum of array elements:

arr=[10,20,30,40,50,60,70,80,90,100]
print("sum:",sum(arr))

############################################################################
#7.maximum or minimum
arr=[10,20,30,40,50]
print("maximum:", max(arr))
print("minimum:",min(arr))

#############################################################################
#8.count even or odd numbers
arr=[1,2,3,4,5,6]
even=0
odd=0

for n in arr:
    if n%2==0:
        even+=1
    else:
        odd+=1
print("even:",even)
print("odd:",odd)            
   
###########################################################################
#9.reverse an array

arr=[32,52,41,87,95,65,44,]
for i in range(len(arr)-6,-4,-2):
    print(arr[i],end=" ") 

##########################################################################
#10.second largest element

arr=[10,20,50,60,80]
unique =list(set(arr))
unique.sort()
print("second largest:",unique[-2])

###########################################################################
#11.factorial using function

def factorial(n):
    result = 1 
    for i in range (1,n+1):
        result *=i
        return result
    print(factorial(5))

###############################################################################
#12.palindrome using function
def palindrome(n):
    return str(n)==str(n)[::-1]
print(palindrome(121))

################################################################################
#13.fibonacci series using function

def fibonacci (n):
    a,b=0,1

    for i in range(n):
        print(a,end="")
        a,b=b,a+b
fibonacci(7)        
################################################################################
#14.GDC using function



