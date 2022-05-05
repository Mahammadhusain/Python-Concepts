import os

# Know current working directory
# print(os.getcwd())
'C:\\Python37'

# Make new directory
import os
# os.getcwd()
# os.mkdir(f"MyPythonProject")

# Change Current working directory
# os.chdir("C:\\MyPythonProject")
# os.getcwd()
# 'C:\\MyPythonProject'
# os.chdir("..")
# os.getcwd()
# 'C:\\'


# Remove Directory
import os
# os.rmdir("C:\\MyPythonProject")


# Permission error (when directory alredy in working)
import os
# os.getcwd()
'C:\\MyPythonProject'
# os.rmdir("C:\\MyPythonProject")
# PermissionError: [WinError 32] The process cannot access the file because it is being used by another process: 'd:\\MyPythonProject'
# os.chdir("..")
# os.rmdir("MyPythonProject")

# list of all files and directory of parent folder
import os
# print(os.listdir("c:\\xampp")) # list of specific directory path
print(os.listdir()) # list current working directory