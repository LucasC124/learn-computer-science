#In this code it will check a list of numbers and if any duplicates are found they will be removed and the new list will be printed out 
test_list = [1, 2, 2, 3, 4, 4, 5]
print("the list with duplicates is :"
      +str(test_list))
res = []
[res.append(x) for x in test_list if x not in res]
print("the list without duplicates : "
      + str(res))
