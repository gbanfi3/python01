import re

szoveg = r'nevem james bond. nem rossz.'
regexa = re.compile('james (smith|bond|clarke)')
mo = regexa.search(szoveg)
if not mo == None:
    print(mo)
    print(mo.group(0))
    print(mo.group())
    print(mo.groups())
    print(mo.group(1))
else:
    print('xxxxx')