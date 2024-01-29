# num=[1,2,3,4,5]
# print(num[3:5])

# 
# num=[1,2,3,4,5]
# num.append (' Next')
# print (num)

# num=[1,2,3,4,5]
# a=[6,7,8,9]
# num.extend(a)
# print (num)

# num=[1,2,3,4,5]
# a=[6,7,8,9]
# c=num.extend(a)
# print (num)

# num=[1,2,3,4,5]
# a=[6,7,8,9]
# a[4]=100
# print (a)

# num=[1,2,3,4,5]
# #del num[1:3] # 
# num.remove (3)
# print (num)

#split()
#str.split(sp,maxsp)
# sp символ, по которой происходит разделение
# spmax - максимальное кол-во разделений

# text = 'hello world'
# print(text.split())

# data = 'hello world -text'
# print(data.split(' -',) )


# text='i like cat cat cat'
# print(text.replace('cat','aples',1))

# def a(s):
#     return s[::-1]
# print(a('hello'))

# text = 'Hello Timur Denis Sergey'
# print(text.split(' ', 1) )

#Домашнее задание 1
# Написать функцию, которая умножает все элементы в произвольном списке .

def multiply(list):
    product = 1
    for element in list:
        product *= element
    print(product)
    
multiply([100,11,22,444,55])

#Домашнее задание 2
#Написать функцию для удаления всех дубликатов в произвольном массиве.
def remove_duplicates(array):
    print (list(set(array)))

remove_duplicates([1,3,6,6,6,8,9,0,4])

#Написать функцию, которая берет 2 списка сравнивает их и если у них есть хотя бы один общей компонент, то выводит надпись TRUE.
def compare_lists(list1, list2):
    for element in list1:
        if element in list2:
            print("TRUE")
            return
    print("FALSE")

compare_lists([1,2,3,4,5,6], [1,2,3,4,5,6])
compare_lists([8,9,10], [1,2,3,4,5,7])