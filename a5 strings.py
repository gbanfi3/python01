import pprint
a="hello world"
b=a.startswith("hello")
print(b)

b=a.endswith("hello")
print(b)

c=' - '.join(['aaa', 'bbb', 'ccc'])
print(c)

d='valami emberrel háromszor'.split('m')
pprint.pprint(d)

e='valami'.ljust(13,'.')
print('x' + e + 'x')

f='alma'.center(20,'.')
print(f)

g='     kjdfksjfkja  jfa fj afj  j  '
print('.' + g.strip() + '.')
print('.' + g.strip().strip('kjd') + '.')

print((g.replace('j', 'J')))
