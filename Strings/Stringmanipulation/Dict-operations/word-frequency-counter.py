import operator as op
test_str = 'apple banana apple orange banana apple'
print("The original list is : " + str(test_str))
listString = test_str.split()
res = {key: op.countOf(listString, key) for key in listString}
print("the word frequencies are : " + str(res))