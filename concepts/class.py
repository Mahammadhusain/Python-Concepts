
# Access Private Variable or Method (1-way)
class Student:
    __schoolName = 'XYZ School' # private class attribute

    
    def __display(self):  # private method
	    print('This is private method.')

# a= Student()
# a._Student__display()

# Access Private Variable or Method (2-way)
class Student:
    __schoolName = 'XYZ School' # private class attribute

    def call_school(self):
        return self.__schoolName

    def __display(self):  # private method
        print('This is private method.')

    def call_display_method(self):
        return self.__display()

a= Student()
print(a.call_school())
a.call_display_method()