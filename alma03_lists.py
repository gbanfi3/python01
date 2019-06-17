# ipAddress = input("ip address: ")
# print("ennyi pont van benne: {}".format(ipAddress.count(".")))
# keres = input("ezt keresem: ")
# ipAddress = "1.2.3.4.5.6.7.8.9.0"
#
# print("hányadik helyen van?: {}".format(ipAddress.index(keres)))

# parrot_list = ["egy", "ketto", "harom", "negy"]
# parrot_list.append("öt")
#
# for i in parrot_list:
#     print("ez a madár {}".format(i))
#     print("ez a madár " + i)


# even = [2,4, 6, 8]
# odd = [1,2,3, 4]
#
# all = even + odd
# all_sorted = sorted(all)
# all.sort()
# print(all)
# print(all_sorted)


# list_1 = []
# list_2 = list()
# print("list 1: {}".format(list_1))
# print("list 2: {}".format((list_2)))
# a = list("hello world")
# a.sort(reverse=True)
# print(a)

# even = [2, 4, 6, 8]

# even2 = list(even)
# print(even == even2)
# odd = [1,3,5,7,9]
# numbers = [even, odd]
# for number_set in numbers:
#     print(number_set)
#
#     for i in number_set:
#         print(i)

# menu = []
# menu.append(["a", "b", "c"])
# menu.append(["a", "b", "d"])
# menu.append(["a", "e", "c"])
# menu.append(["w", "b", "c"])
#
# for meal in menu:
#     if not "a" in meal:
#         print(meal)
#         for i in meal:
#             print(i)

# string = "1234567890"
# for i in string:
#     print(i)

# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# for i in string:
#     print(i)
#
# for i in iter(string):
#     print(i)

# a = list(string)
# a_iter = iter(a)
# for i in range(len(a)):
#     print(next(a_iter))

# print(list(range(10)))
# even = list(range(0,10,2))
# odd = list(range(1,10,2))
# print(even)

# aa = "qwertzujhgfdsa"
# print(aa[6])
# print(aa.index("u"))

# sevens = range(7, 1000000, 7)
# i = int(input("he?: "))
# if i in sevens:
#     print("osztható")

a = range(0, 100)
myrange = a[3:40:3]
print(myrange)

for i in myrange:
    print(i)

print('=' * 40)
