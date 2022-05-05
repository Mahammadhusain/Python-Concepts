# ------------------------------------------------------------------------------------------------
#                                @classmethod decorator
# ------------------------------------------------------------------------------------------------

# POINTS:
    # Declares a class method.
    # The first parameter must be cls, which can be used to access class attributes.
    # The class method can only access the class attributes but not the instance attributes.
    # The class method can be called using ClassName.MethodName() and also using object.
    # It can return an object of the class.

# Make Class Method (only access class property not instance property)
class Student:
    name = 'unknown' # class attribute
    def __init__(self):
        self.age = 20  # instance attribute

    @classmethod
    def tostring(cls):
        print('Student Class Attributes: name=',cls.name)

# Student.tostring() # Call class method using (Name of class)
# s= Student 
# s.tostring() # Call class method using 

# @classmethod can not access instance property
class Student:
    name = 'unknown' # class attribute
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age    # instance attribute 

    @classmethod
    def tostring(cls):
        print('Student Class Attributes: name=',cls.name)

# Student.tostring() 
Student.tostring() 
print(Student.name)
