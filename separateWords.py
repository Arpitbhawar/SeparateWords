import time
# Stack class to keep track of the associated words
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

# definition to Search for all possible words present in the dictionary that can satisfy var_Query
def SearchPossibleWords(var_Query):
    tempDictionary={}
    dictionaryElements=[]
    dictionaryElements.append(var_Query)
    initial=var_Query[0:1].lower()
    for x in dictionary:
        # match first 2 characters of the string to improve performance by reducing the number of words to trace
        if x[0:1].lower()==initial:
           # validating that the code works as case insensitive
           if x.lower() in var_Query.lower():
              if (var_Query.lower()).index(x.lower())==0:
                  dictionaryElements.append(x)
    return dictionaryElements

# finding all the paths possible present in the graph
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
    
start_time = time.time() # start time to measure the performance of long strings
# some test cases to validate the code 
#Query='FryBhindiFryPastaPizzaAalooParathaDumbiriyaniCappuccino'
#Query='FryBhindiFryPastaPizzaAalooParathaDumbiriyaniCappuccinoPlainRiceHalfBotiMasalaNatiChickenNatiChickenGheeRoastChickenKabab'
Query='FryBhindiFryPastaPizzaAalooParathaDumbiriyaniCappuccinoPlainRiceHalfBotiMasalaNatiChickenNatiChickenGheeRoastChickenKababFryBhindiFryPastaPizzaAalooParathaDumbiriyaniCappuccinoPlainRiceHalfBotiMasalaNatiChickenNatiChickenGheeRoastChickenKabab'
# dictionary of all the words that are expected to come in string 
dictionary='Daal DaalBaati Cappuccino Aaloo Paratha Fry Pasta Pizza Bhindi Dumbiriyani Plain Rice Half Boti Masala Nati Chicken Ghee Roast Kabab'.split(' ')
# Creating two stacks to keep track of the substrings after truncating the words present in the dictionary and calling them recursively
s1=Stack()
s2=Stack()
# initialize and empty dictionary to keep track of all the possible combination of words sequence possible
graph={}

graph['start']=[SearchPossibleWords(Query)]
s1.push(graph['start'][0])
# keep truncating the string until stacks are empty
while (s1.size()!=0 or s2.size()!=0):
       while s1.size()!=0:
             #print 'inside while of s1'
             a=s1.pop()
             #print a
             for x in a[1:]:
                  #dont push Flaf is initialized to check if all the words have been trancated or not dontPushFlag=False if the string is fully truncated
                 dontPushFlag=False
                 # Check if key is already present in graph if present the new combination of words will be appended in the array present in stack
                 if x in graph:
                     #print x
                     # check if key is present in dictionary present in stack
                     if a[0][len(x):]!='' and x in a[0]:
                         # check if first element are same
                         key_present=0
                         #print "keypresent"
                         for i in graph[x]:
                              # search for all the possible words with which the string may start
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
                              # append if the ke is the last word of the string 
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
