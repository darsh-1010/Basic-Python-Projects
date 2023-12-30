#coin note analysis
# Take in put from the user

notes=int(input(" Enter the currency amount:"))
# Specifing the condition for getting the coin note analysis

a=notes//2000
notes%=2000
b=notes//500
notes%=500
c=notes//200
notes%=200
d=notes//100
notes%=100
e=notes//50
notes%=50
f=notes//20
notes%=20
g=notes//10
notes%=10
h=notes//5
notes%=5
i=notes//2
notes%=2
j=notes//1
notes%=1

# printing the out put

print ("No. of RS.2000 notes=",a)
print ("No. of RS.500 notes=",b)
print ("No. of RS.200 notes=",c)
print ("No. of RS.100 notes=",d)
print ("No. of RS.50 notes=",e)
print ("No. of RS.20 notes=",f)
print ("No. of RS.10 notes / coins=",g)
print ("No. of RS.5 notes / coins=",h)
print ("No. of RS.2 notes / coins=",i)
print ("No. of RS.1 notes / coins=",j)




