import re

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
mo = aRegex.findall(szoveg)
print(mo)