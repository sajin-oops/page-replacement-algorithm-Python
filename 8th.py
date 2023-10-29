print('Least Recently Used Page Replacement Algorithm')
print('**********************************************')
capacity = int(input('enter the no of free frames:'))
processList = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
s = []
pageFaults = 0
for i in processList:
 if i not in s:
  if (len(s) == capacity):
   s.remove(s[0])
   s.append(i)
  else:
   s.append(i)
 pageFaults += 1
else:
 s.remove(i)
 s.append(i)
print("Total no of Page faults = {}".format(pageFaults))
fault_ratio = pageFaults/len(processList) * 100
page_hit = len(processList) - pageFaults
hit_ratio = page_hit/len(processList) * 100
print('fault ratio=%0.2f' %fault_ratio)
print('hit ratio=%0.2f' %hit_ratio)
