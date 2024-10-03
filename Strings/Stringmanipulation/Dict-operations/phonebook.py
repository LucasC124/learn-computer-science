names = []
phone_numbers = []
num = 2
for i in range(num):
    name = input("Name: ")
    phone_number = input("phone number: ")
    names.append(name)
    phone_numbers.append(phone_number)
print("\nName\t\t\tPhone Number\n")
for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))
search_term = input("\nenter search term: ")
print("search results:")
if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    print("name: {}, phone number: {}".format(search_term, phone_number))
else:
    print("name and number not found")

