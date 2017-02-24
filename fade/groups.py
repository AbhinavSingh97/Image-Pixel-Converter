def groups_of_3(list1):
   new_list = []
   
   for i in range(0, len(list1), 3):
      groups = []
      groups.append(list1[i])
     
      if i+1 < len(list1):
      	groups.append(list1[i+1])
     
      if i+2 < len(list1):
      	groups.append(list1[i+2])
      new_list.append(groups)
   
   return new_list
