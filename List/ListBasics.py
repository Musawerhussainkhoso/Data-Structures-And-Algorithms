list = [1,2,3,4,5]
list02 = ["Apple","Banana","Cheku"]
for i in range(len(list)):
    print(list[i])

#there are the mmany methods within the list here some of them are:
#adding elements within the list
list.append(122)#adding new element in the list at the end
list.pop()#removing the last element from the list
print(len(list))# return the length of the list
print(list.count(1))#return the number of times the element is present in the list
list.insert(2,333)# insert used to add any element at the specific position
list.extend([56,67,78,89])#used to add multiple elements at the end of the list
list.remove(333)# used to remove the element from the list
print(list)