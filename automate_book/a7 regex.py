import re

szoveg = r'ez itt a telefonszámom: (36)-(36)-20-1234567. jó mi?'
telszamRegex = re.compile('(\((\d\d)\)-)*(\d\d)-(\d\d\d\d\d\d\d)')
mo = telszamRegex.search(szoveg)
if not mo == None:
    print(mo)
    print(mo.groups())
    print(mo.group())
    print(mo.group(1))
    print(mo.group(2))
    print(mo.group(3))
    print(mo.group(4))
else:
    print('sajna nincs')
