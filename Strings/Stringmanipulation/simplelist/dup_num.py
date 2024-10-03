test_list = [1, 2, 2, 3, 4, 4, 5]
print("the list with duplicates is :"
      +str(test_list))
res = []
[res.append(x) for x in test_list if x not in res]
print("the list without duplicates : "
      + str(res))
