#This code will ask for an amount of number to be inputeed and then will print the biggest number by using the range 
list1 = []
num = int(input("enter how many numbers are being used"))
for i in range(1, num + 1):
     ele = int(input("enter a number: ")) 
     list1.append(ele)
print("the maxiumum number is ", max(list1))