import re
# batRegex = re.compile((r'Bat(wo)*man'))
# mo = batRegex.search('ez a Batwowoman itt')
# if not mo == None:
#     print(mo.group())
# else:
#     print('nincs')

szoveg = 'HahaHaHaHahahu'
haRegex = re.compile(r'(Ha){2,5}')
mo = haRegex.search(szoveg)
print(mo)

#greedy, largest possible
digitRegex = re.compile(r'(\d){1,5}')
mo = digitRegex.search('1a234567890')
print(mo)

#not greedy, smallest possible
digitRegex = re.compile(r'(\d){2,5}?')
mo = digitRegex.search('1a234567890')
print(mo)
