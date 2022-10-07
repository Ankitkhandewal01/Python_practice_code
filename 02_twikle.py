# print('hello world')
# first_name='ankit'
# last_name='khadelwal'
# full_name=first_name.upper()
# print(full_name)

# full_name=first_name.capitalize()+' '+last_name.capitalize()
# print(full_name)

# full_name=first_name.lower()
# print(full_name.count('a'))

# lst=[1,2,3,4,'hekon',1,3,3,3,2]
# print(lst[4][3])

# s='khandelwal'
# ls=list(s)
# ls.sort()
# print(ls)

# a=[1,3,3,3,2,1,3,3,3,2]
# a.append('b')
# print(a)

# map_ = {
#     'full_name':'4',
#     'last_name':'khandelwal'
# }
# print(map_['full_name'])
# print(map_.get('company','not found'))

# lst=[1,2,3,4,5,6,7,8,9,10]
# for i in lst[:2] :
#     for i in ['a','b','c'] :
#         for j in ['1','2','3']:
#             print(j,i)

# #prime
# # num=7
# # for i in range(2,num):
# #     if num%i==0:
# #         print("not prime")
# #     break
# # else:
# # #         print("prime")

# # wap add a no. by add 4 54 3 
# n=int(input("enter the number : "))
# for i in range(n):
#     op_list=input("enter the case of op :")
#     op_list=op_list.split()
#     if op_list[0]=="add":
#         first_number=int(op_list[1])
#         second_number=int(op_list[2])
#         print(first_number + second_number)
#     # elif op_list[0]=="sub":
#         first_number=int(op_list[1])
#         second_number=int(op_list[2])
#         print(first_number - second_number)
#     elif op_list[0]=="mul":
#          first_number=int(op_list[1])
#          second_number=int(op_list[2])
#          print(first_number * second_number)
# n=input("enter the no.:")
# op_list=n.split()
# # if op_list[0]=='add':
# add_=0
# for i in range(0,len(op_list)):
#         add_=add_+int(op_list[i])
# print(add_)

# # #palindrom
# r = "naman"
# s = "naman"
# if r[::-1]==s:
#     print("the number is palandrom")
# else:
#     print("not palandrom")

#2 lst=input('enter')
# list=lst[::-1]
# if list==lst:
# print('the given string is palindrom')
# else:
# print("not")

#wrt to count a word in file handling python
# f=open('abhi','r')
# data=f.read()
# cnt=0
# w=data.split()
# for ch in w:
#     cnt+=1
# f.close()
# print("the no. of words",cnt)

# file handeling
# f=open('abhi','r')
# data=f.read()
# cnt=0
# for ch in data:                            
#     if ch.isupper():
#         cnt+=1
# f.close()
# # print("the no. of words",cnt)

# n=5
# for i in range(n):
#     op_list=input("enter the case of op :")
#     op_list=op_list.split()
# if op_list[0]=='4':
#         pass
# elif op_list[0]=='73':
#         a=op_list[0]+2
#         print(a)
# elif op_list=="67":
#         pass
# elif op_list=="38":
#         op_list=38+2
# elif op_list=="33":
#         pass

# map_ ={
#     '4':'4','73':'75','67':'67','38':'40','33':'33',
#     }
# n=5
# for i in range(n):
#     print(map_.get(input()))

##*if a user give a input to create a folder
# name of test in same loction
# user=input("enter the input:")
# if user==1:
#     file=open('test','w')
#     file=file.write('ajay')
# elif user=="a":
#     print('input is wrong')

# #*input thanf a user give the output will be print IP adresses
# from ipaddress import ip_address
# import socket
# host_name=socket.gethostname()
# ip_address=socket.gethostbyname(host_name)
# print("enter the host name ",host_name)
# print("enter the id adders",ip_address)

# *if a user give a put an input 4 so 
# you open a browser and search regex
# import webbrowser
# webbrowser.open("https://www.regexsoftware.com/")

# *if a user give a input 5 than open
#  a whatsapp and message to sir
# import pywhatkit
# pywhatkit.sendwhatmsg('+919602970369','happey birthday',17,26)
# from turtle import color


# class Phone():
#     def set_color(self,color):
#         self.color=color
#     def set_cost(self,cost):
#         self.cost=cost
#     def show_color(self):
#         return self.color
#     def show_cost(self):
#         return self.cost 
#     def make_call(self):
#         print("calling") 
#     def playing_game(self):
#         print("playing games")  
# p1 = Phone()
# p1.set_color("blue")
# p1.set_cost(500)
# p1.show_color()



# from lib2to3.pgen2.driver import Driver


# class Driver:
#     def __init__(self,id,name,email):
#         self.id=id
#         self.name=name
        # self.email=email
#     def infoPrint(self):
#         print("hello")
# class Customer(Driver):
#     def _init_(self,id,name,email):
#         super().__init__(id,name,email)

# d1=Driver("id","name","email")
# d1.infoPrint()

# car query in class
# class Vechile:
#     year=1000

# class TataMotors(Vechile):
#     car_name="harrier"

# v1=Vechile()
# print(v1.car_name)

# tuple of vowels
# vowels = ('a', 'e', 'i', 'o', 'u')

# fSet = frozenset(vowels)
# print('The frozen set is:', fSet)
# print('The empty frozen set is:', frozenset())

# # frozensets are immutable
# fSet.add('v')n
# n=int(input("enter the number :"))
# b=int(input("enter the number :"))
# k=n*b
# print(k)

# wap patterm hollow tringle
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==i or i==n or j==1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
        
#     print()