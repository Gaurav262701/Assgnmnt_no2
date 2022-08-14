#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Answer no.1
#program converting kilometers into miles
kilometers = float(input("Enter value in kilometers:"))
#conversion
Conv_fac = 0.621371  #its a value of 1 kilometer in miles
miles = kilometers*Conv_fac   
print("%0.2f kilometers is equal to %0.2f miles"%(kilometers,miles))


# In[1]:


#Answer no.2
celsius_1 = float(input("Enter the tempreture :"))
#given formula
fahrenheit_1 = (celsius_1*1.8) + 32
print("The %.2f degree celsius : %.2f fahrenheit"%(celsius_1,fahrenheit_1))


# In[2]:


#Answer no.3
import calendar
year = int(input("Enter the year:"))
months = int(input("Enter the month:"))
print(calendar.month(year , months))


# In[3]:


#Answer no.4 
import math
def Equa_roots(a,b,c):
    dis = b*b-4*a*c
    sqrt_val = math.sqrt(abs(dis))
#checking for condition disciminant  
    if dis > 0:
        print("real and diffrent roots")
        print((-b + sqrt_val)/(2*a))
        print((-b - sqrt_val)/(2*a))
    elif dis == 0:
        print("real and diffrent roots")
        print(-b/(2*a))
        
    else:
        print("complex roots")
        print(-b / (2*a),"+i",sqrt_val)
        print(-b /(2*a),"-i",sqrt_val)
        
a = 1
b = 10
c = -20

if a == 0:
    print("Enter correct equation")
    
else:
    Equa_roots(a,b,c)


# In[4]:


#Answer no.5
#program to swap variable without using temp
a = 10
b =5

#creating 3 variable for swapping
c = a
a = b
b = c
print("value of a after swapping: {}".format(a))
print("value of b after swapping: {}".format(b))


# In[ ]:




