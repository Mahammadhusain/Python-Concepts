string = '["a,b", "b,c"]'
def strList_to_list(list_name):
    list_name = list(map(str.strip, list_name.strip('][').replace('\"', '').split(',')))
    return list_name

string1 = "['a,b', 'b,c']"
def str1List_to_list(list_name):
    list_name = list(map(str.strip, list_name.strip('][').replace("\'", '').split(',')))
    return list_name

lst = strList_to_list(string)
lst1 = str1List_to_list(string1)
print(lst)
print(lst1)
