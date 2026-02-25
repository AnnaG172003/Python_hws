from collections import Counter
mylist = ['cat','dog','cat','mouse','dog','cat']
counter = Counter(mylist)
print (counter)
print("Most common: " ,counter.most_common(1))