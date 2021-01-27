
lst = list(input().split())
i1 = int(lst[0])
i2 = int(lst[1])
i3 = int(lst[2])

lst2 = []
lst2.append(i1);
lst2.append(i2);
lst2.append(i3);

i1 = min(lst2);
i3 = max(lst2)
lst2.remove(max(lst2))
lst2.remove(min(lst2))
i2 = min(lst2)

alp = input()
alp = alp.upper()
lst1 = list(alp)

if(lst1[0]=='A' and lst1[1] == 'B' and lst1[2] == 'C'):
  print(i1,i2,i3)
elif(lst1[0]=='A' and lst1[1] == 'C' and lst1[2] == 'B'):
  print(i1,i3,i2)
elif(lst1[0]=='B' and lst1[1] == 'A' and lst1[2] == 'C'):
  print(i2,i1,i3)
elif(lst1[0]=='B' and lst1[1] == 'C' and lst1[2] == 'A'):
  print(i2,i3,i1)
elif(lst1[0]=='C' and lst1[1] == 'A' and lst1[2] == 'B'):
  print(i3,i1,i2)
elif(lst1[0]=='C' and lst1[1] == 'B' and lst1[2] == 'A'):
  print(i3,i2,i1)
