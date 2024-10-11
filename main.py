some_list = [1, "one", [1,3,True], 25, False,"two"]

print(some_list[-1])
print(some_list[:2])

if "one" in some_list:
    print("It is right!")

some_list.append("two")
some_list[2]="four"
some_list[:2] = [10, "TEN"]
some_list.insert(4, True)
print(some_list)
some_list.remove("two")
pop_list=some_list.pop(0)
print(pop_list)

del some_list[-1]

print(some_list)

for i in some_list:
    print(i)

for i in range(len(some_list)):
    print(i)
    print(i,some_list[i])

[print(i) for i in some_list]

list_fruits = ["lemon", "orange", "apple","kiwi"]
# for i in list_fruits:
#     if 'kiwi' == i:
#         list_fruits.append("mango")
#
# print(list_fruits)

[list_fruits.append("mango") for i in list_fruits if i == "kiwi"]
print(list_fruits)

new_list = [{x**2:x+20} for x in range(15) if x > 6]
print(new_list)

list_fruits.sort(reverse=True)
print(list_fruits)
all_lists = list_fruits+some_list
print(all_lists)
print(len(all_lists))


some_dict = {
    1:"Hello",
    2:"Bay",
    3:some_list,
}

