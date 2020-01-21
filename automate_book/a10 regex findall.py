import re, pprint

szoveg = '''
 j lkjf ljsafk léjfl sdufiosp dfjksldé jfskdl fudli fjkl dfjdkls fjk ldéjfkdal sfjslkda ziosduzt rpo578 pe ui 
 sdjfkasp87op irasj5k 123-456-7890 ashtki asdufoipsadkfj asdhfjk lsadhfjkasluz3i rhask jfhjsdakl fhsdajk fhkjl
 j lkjf ljsafk léjfl sdufiosp dfjksldé jfskdl fudli fjkl dfjdkls fjk ldéjfkdal sfjslkda ziosduzt rpo578 pe ui 
 sdjfkasp87op irasj5k ashtki 1234756-6654 asdufoipsadkfj asdhfjk lsadhfjkasluz3i rhask jfhjsdakl fhsdajk fhkjl
 j lkjf ljsafk léjfl sdufiosp dfjksldé jfskdl 456-789-1234 fudli fjkl dfjdkls fjk ldéjfkdal sfjslkda ziosduzt rpo578 pe ui 
 sdjfkasp87op irasj5k ashtki asdufoipsadkfj asdhfjk lsadhfj 55555555555 kasluz3i rhask jfhjsdakl fhsdajk fhkjl
 j lkjf ljsafk léjfl sdufiosp dfjksldé jfskdl fudli fjkl dfjdkls99999789-456-1234  fjk ldéjfkdal sfjslkda ziosduzt rpo578 pe ui 
 sdjfkasp87op irasj5k ashtki asdufoipsadkfj asdhfjk lsadhfjkasluz3i rhask jfhjsdakl fhsdajk fhkjl
'''

aRegex = re.compile(r'(\d(\d\d))-(\d\d\d)-(\d\d\d\d)')
mo = aRegex.findall(szoveg) # a findall nem match objectet ad vissza, hanem egy list-et
print(mo)

# \d \D szám
# \w \W szám, betü, _
# \s \S space tab, newline

#=================================================================

aa = '''
12 drummers drumming
11 pipers piping
10 lords a leaping
9 ladies dancing
8 maids a milking
7 swans a swimming
6 geese a laying
5 gold rings, badam-pam-pam
4 calling birds
3 French henss
2 turtlee doves
And 1 partridge in a pear tree
'''

aRegex = re.compile(r'(\d+) (\D+)\n')
lista = aRegex.findall(aa)
pprint.pprint(lista)

#=================================================================

maganhangzo = re.compile(r'[^aeioúőóüöűáéaA-Z]{2}') #tagadás
lista = maganhangzo.findall(aa)
pprint.pprint(lista)

#=================================================================
