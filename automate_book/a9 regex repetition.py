import re
batRegex = re.compile((r'Bat(wo)*man'))
mo = batRegex.search('ez a Batwowoman itt')
if not mo == None:
    print(mo.group())
else:
    print('nincs')
