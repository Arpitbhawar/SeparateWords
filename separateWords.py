import time
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
        
def SearchPossibleWords(var_Query):
    tempDictionary={}
    dictionaryElements=[]
    dictionaryElements.append(var_Query)
    initial=var_Query[0:1].lower()
    for x in dictionary:
        if x[0:1].lower()==initial:
           if x.lower() in var_Query.lower():
              if (var_Query.lower()).index(x.lower())==0:
                  dictionaryElements.append(x)
    return dictionaryElements


def find_all_paths(graph, start, end,temp_key, path=[]):
        path = path + [start]
        #print path
        if start == end:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        if len(graph[start])>1:
           for j in graph[start]:
               if j[0]==temp_key:
                  temp=j
                  break
        else:
             temp=graph[start][0]
        for node in temp[1:]:
            if temp[0].index(node)==0:
                if node in temp[0]:
                    if node not in path or len(graph[node])>1:
                        temp_key=temp[0][len(node):]
                        newpaths = find_all_paths(graph, node, end,temp_key, path)
                        for newpath in newpaths:
                            paths.append(newpath)
        return paths
    
start_time = time.time()
#Query='DaalBaatiChurmaDaalFryBhindiFryPastaPizzaAalooParathaDumbiriyaniCappuccino'
#Query='DaalBaatiChurmaDaalFryBhindiFryPastaPizzaAalooParathaDumbiriyaniCappuccinoPlainRiceHalfBotiMasalaNatiChickenNatiChickenGheeRoastChickenKabab'
Query='DaalBaatiChurmaDaalFryBhindiFryPastaPizzaAalooParathaDumbiriyaniCappuccinoPlainRiceHalfBotiMasalaNatiChickenNatiChickenGheeRoastChickenKababDaalBaatiChurmaDaalFryBhindiFryPastaPizzaAalooParathaDumbiriyaniCappuccinoPlainRiceHalfBotiMasalaNatiChickenNatiChickenGheeRoastChickenKababDaalBaatiChurmaDaalFryBhindiFryPastaPizzaAalooParathaDumbiriyaniCappuccinoPlainRiceHalfBotiMasalaNatiChickenNatiChickenGheeRoastChickenKababDaalBaatiChurmaDaalFryBhindiFryPastaPizzaAalooParathaDumbiriyaniCappuccinoPlainRiceHalfBotiMasalaNati'
dictionary='Daal Baati Churma DaalBaati DaalBaatiChurma Cappuccino Aaloo Paratha Fry Pasta Pizza Bhindi Dumbiriyani Plain Rice Half Boti Masala Nati Chicken Ghee Roast Kabab'.split(' ')
s1=Stack()
s2=Stack()
graph={}
graph['start']=[SearchPossibleWords(Query)]
s1.push(graph['start'][0])

while (s1.size()!=0 or s2.size()!=0):
       while s1.size()!=0:
             #print 'inside while of s1'
             a=s1.pop()
             #print a
             for x in a[1:]:
                 dontPushFlag=False
                 if x in graph:
                     #print x
                     if a[0][len(x):]!='' and x in a[0]:
                         # check if first element are same
                         key_present=0
                         #print "keypresent"
                         for i in graph[x]:
                             if i==SearchPossibleWords(a[0][len(x):]):
                                key_present=1
                                break
                         if key_present==0:
                            graph[x].append(SearchPossibleWords(a[0][len(x):]))
                     elif x in a[0] and a[0][len(x):]=='':
                         #print "last"
                         #if a[0]==x:
                         #print x
                         #print graph[x]
                         count=0
                         for i in graph[x]:
                              if i==['','']:
                                 count =1
                                 break
                         if count==0:
                            graph[x].append(['',''])
                         dontPushFlag=True
                     else:
                          dontPushFlag=True
                 else:
                     if x in a[0]: 
                          if a[0].index(x)==0:
                               if a[0][len(x):]!='':
                                   graph[x]=[SearchPossibleWords(a[0][len(x):])]
                               else:
                                   #print "First"
                                   graph[x]=[['','']]
                                   dontPushFlag=True
                          else:
                               dontPushFlag=True
                     else:
                          dontPushFlag=True
                 if dontPushFlag==False:
                     s2.push(SearchPossibleWords(a[0][len(x):]))
             #print graph
                     
       while s2.size()!=0:
             #print 'inside while of s2'
             a=s2.pop()
             #print a
             for x in a[1:]:
                 dontPushFlag=False
                 if x in graph:
                     #print x
                     if a[0][len(x):]!='' and x in a[0]:
                         # check if first element are same
                         key_present=0
                         for i in graph[x]:
                             if i==SearchPossibleWords(a[0][len(x):]):
                                key_present=1
                                break
                         if key_present==0 :
                            graph[x].append(SearchPossibleWords(a[0][len(x):]))
                     elif x in a[0]:
                          #print "last"
                          #print x
                          #print graph[x]
                          #if a[0]==x:
                          count=0
                          for i in graph[x]:
                              if i==['','']:
                                 count =1
                                 break
                          if count==0:
                             graph[x].append(['',''])
                          dontPushFlag=True
                     else:
                          dontPushFlag=True
                 else:
                      if x in a[0]: 
                          if a[0].index(x)==0:
                               if a[0][len(x):]!='':
                                   graph[x]=[SearchPossibleWords(a[0][len(x):])]
                               else:
                                   #print "First"
                                   graph[x]=[['','']]
                                   dontPushFlag=True
                          else:
                               dontPushFlag=True
                      else:
                           dontPushFlag=True
                 if dontPushFlag==False:
                     s1.push(SearchPossibleWords(a[0][len(x):]))
             #print graph
#print graph
        
results=find_all_paths(graph,'start','',Query)
a=[]
max=0
if len(results)>0:
    for j in results:
            if len(j)>max:
                    if max==len(j):
                            a.append(j)
                    else:
                            a=j
                    max=len(j)
    print ' '.join(a[1:-1])
else:
    print "NULL"
print("--- %s seconds ---" % (time.time() - start_time))
