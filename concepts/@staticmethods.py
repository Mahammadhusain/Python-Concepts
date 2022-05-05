# ------------------------------------------------------------------------------------------------
#                                @staticmethod decorator
# ------------------------------------------------------------------------------------------------

# POINTS:
    # Declares a static method in the class.
    # It cannot have cls or self parameter.
    # The static method cannot access the class attributes or the instance attributes.
    # The static method can be called using ClassName.MethodName() and also using object.MethodName().
    # It can return an object of the class.


# Make @staticmethod
class Student:
    name = 'unknown' # class attribute
    
    def __init__(self):
        self.age = 20  # instance attribute

    @staticmethod
    def tostring():
        print('Student Class')

# Student.tostring() # calling using class name
# std = Student()
# std.tostring() # calling using object of class

# @staticmethod can't access class attributes or instance attributes
class Student:
    name = 'unknown' # class attribute
    
    def __init__(self):
        self.age = 20  # instance attribute

    # @staticmethod
    def tostring():
        print('name=',self.name,'age=',self.age)

Student.tostring()