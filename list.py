thislist = ["apple","banana","orange"]
print (thislist)
print (len(thislist))
print (thislist[2:])
print (thislist[-4:-1])
if "apple" in thislist:
  print ("yes")
  thislist[1]="banana"
  thislist.append("grapes")
  thislist.insert(3,"kiwi")
  list1 = [1,2,3]
  thislist.extend(list1)
  thislist.remove("kiwi")
  del thislist[0]
  thislist.clear()
  for x in thislist:
    print (x)
