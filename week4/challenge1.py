 '''

لديكم هذه القائمة تحتوي على عناصر 
my_list = ['HKU3K','KJI8TE','IIUH1I','I7YUI','OPRE9','5JGU','ER4TB','HY0OH']

المطلوب ترتيب هذه القائمة تصاعديًا 
ليكون المخرج كالتالي 

['HY0OH','IIUH1I','HKU3K','ER4TB','5JGU','I7YUI','KJI8TE','OPRE9']

'''
#------------------ @start:zaid------------------------------

L = ['HKU3K','KJI8TE','IIUH1I','I7YUI','OPRE9','5JGU','ER4TB','HY0OH']
S=[]
C=[]
for i in L:
  for z in i:
    if z.isdigit():
      S.append(z)
S.sort()
for x in S:
  for y in L:
    if x in y:
      C.append(y)
print("L=",C)

#-------------------- @end:zaid------------------------------



#------------------ @start:hadeel------------------------------












#-------------------- @end:hadeel------------------------------




#------------------ @start:khalid------------------------------












#-------------------- @end:khalid------------------------------



#------------------ @start:عبدالرحمن------------------------------











#-------------------- @end:عبدالرحمن------------------------------


#------------------ @start:ممدوح------------------------------
my_list = ['HKU3K', 'KJI8TE', 'IIUH1I',
           'I7YUI', 'OPRE9', '5JGU', 'ER4TB', 'HY0OH']
x = 0
d={}
while x < len(my_list):
    letter = my_list[x]
    for p in letter:
        if p.isnumeric() == True:
            d[p]=d.get(p,letter)
    x += 1
sortd=sorted(d.items(),reverse=False)
mysorted_list=[]
for i in sortd:
	mysorted_list.append(i[1])
print(mysorted_list)

#-------------------- @end:ممدوح------------------------------

#------------------ @start:العنود------------------------------










#-------------------- @end:العنود------------------------------

#------------------ @start:أحمد------------------------------










#-------------------- @end:أحمد------------------------------
