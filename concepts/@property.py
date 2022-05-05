# ------------------------------------------------------------------------------------------------
#                                @property decorator
# ------------------------------------------------------------------------------------------------
# POINTS:
    # @property: Declares the method as a property.
    # @<property-name>.setter: Specifies the setter method for a property that sets the value to a property.
    # @<property-name>.deleter: Specifies the delete method as a property that deletes a property.

# Make 
class Myclass:

    def bio_info(self,name,age):
        self.name = name
        self.age = age
        
    @property
    def full_info(self):
        print(f"Full Bio = Name:{self.name} - Age:{self.age}")

# a= Myclass()
# a.bio_info('Rahul',23)
# a.full_info() # calling without @property 
# a.full_info   # calling with @property




# Property Setter @ Deleter
class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name=value
    
    @name.deleter   #property-name.deleter decorator
    def name(self):
        print('Deleting..')
        del self.__name


s = Student('Rahul')
print(s.name)
s.name = 'Mehul'
print(s.name)
del s.name
try:
    print(s.name)
except:
    print('----------- Name was deleted -------------')