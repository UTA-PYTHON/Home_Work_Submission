#!/usr/bin/env python
# coding: utf-8

# ## Homework 6: Object-oriented programming (OOP)

# ### 1. Design a class hierarchy to represent different types of vehicles in a transportation system. Start with a base class called Vehicle with the following attributes and methods:
# 
# **Attributes:**
# 
# - make (string)
# - model (string)
# - year (integer)
# - fuel (float)
# 
# **Methods:**
# 
# - __init__(self, make, model, year, fuel): Initialize the attributes.
# - info(self): Print basic information about the vehicle, including make, model, year, and fuel efficiency.
# 
# Next, create two subclasses that inherit from Vehicle:

# In[2]:


class vehicle:
    def __init__(self, make, model, year, fuel):
        self.make=make
        self.model=model
        self.year=year
        self.fuel=fuel
        
    def info(self):
        return f"The vehicle is a {self.year} {self.make} {self.model} with {self.fuel} fuel capabilities"
        
class value(vehicle):
    def __init__(self, initial, final):
        self.initial=initial
        self.final=final
    def total(self):
        return f"The {self.initial} initial value of the vehicle has changed to {self.final} since it was made in 2015"
        
class speed(vehicle):
    def __init__(self, speed):
        self.speed=speed 
    def top(self):
        return f"The top speed of the 918 Spyder is {self.speed} mph."


# In[3]:


vehicle1=vehicle("Porsche", "918 Spyder", 2015, 12.4)

vehicle1.info()


# In[4]:


vehicle2=value(845000, 1800000)

vehicle2.total()


# In[5]:


vehicle3=speed(214)

vehicle3.top()


# ---

# ### 2. Create a subclass called Car with the following additional attributes and methods:
# 
# **Attributes:**
# 
# - num_doors (integer)
# - is_sedan (boolean)
# 
# 
# **Methods:**
# 
# - __init__(self, make, model, year, fuel, num_doors, is_sedan): Initialize the attributes.
# - display_car_info(self): Print detailed information about the car, including the number of doors and whether it's a sedan.

# In[19]:


class car(vehicle):
    def __init__(self, make, model, year, fuel, num_doors, is_sedan):
        super().__init__(make, model, year, fuel)
        self.num_doors=num_doors
        self.is_sedan=is_sedan
        if is_sedan=='yes':
            print("This car is a sedan")
        elif is_sedan=='not':
            print("This car is not a sedan")
        
    def display_car_info(self):
        return f"The vehicle is a {self.year} {self.make} {self.model} with {self.fuel} fuel capabilities and {self.num_doors}, meaning {self.is_sedan} a sedan"


# In[21]:


vehicle4=car("Porsche", "918 Spyder", 2015, 12.4, 4, 'not')


# In[22]:


vehicle4.display_car_info()


# ---

# ### 3. Create a subclass called Motorcycle with the following additional attributes and methods:
# 
# **Attributes:**
# 
# - top_speed (integer)
# - engine_size (float)
# 
# 
# **Methods:**
# 
# - __init__(self, make, model, year, fuel, top_speed, engine_size): Initialize the attributes.
# - display_motorcycle_info(self): Print detailed information about the motorcycle, including top speed and engine size.
# 
# 
# Finally, create instances of both Car and Motorcycle classes and demonstrate the use of their methods to display information about each vehicle.

# In[30]:


class motorcycle(vehicle):
    def __init__(self, make, model, year, fuel, top_speed, engine_size):
        super().__init__(make, model, year, fuel)
        self.top_speed=top_speed
        self.engine_size=engine_size
        
    def display_motorcycle_info(self):
        return f"The motorcycle is a {self.year} {self.make} {self.model} with {self.fuel} fuel style, a top-speed of {self.top_speed} and {self.engine_size}"
        


# In[31]:


vehicle5=motorcycle('Harley-Davidson', 'Nightster', 2023, 'Electronic Sequential Port Fuel Injection (ESPFI)', '107 mph', 'Revolution Max 975T')

vehicle5.display_motorcycle_info()


# In[ ]:




