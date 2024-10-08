#This code will have a list inputted to them of anything such as fruit and if multiple of the same fruit are found it will 
#Count up the frequency of the words and print out how much of each was found in the list 
import operator as op
test_str = 'apple banana apple orange banana apple'
print("The original list is : " + str(test_str))
listString = test_str.split()
res = {key: op.countOf(listString, key) for key in listString}
print("the word frequencies are : " + str(res))