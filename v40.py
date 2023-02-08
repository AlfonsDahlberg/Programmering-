#uppgift 1.1
list1 = ["Alfa", "Beta", "Cacau", "Dennis", "Engvald"]
print(list1)
#uppgift 1.2
list2 = list1.copy()
print(list2)
#uppgift 1.3
list2.reverse()
print(list2)
#uppgift 1.4
element1 = list2[0]
print(element1)
#uppgift 1.5
list1.insert(3, element1)
print(list1)
#uppgift 1.6
antalelement1 = list1.count(element1)
print(antalelement1)

#uppgift 2.1
tal1 = [1, 2, 3, 4, 5]
#uppgift 2.2
tal1.append(2)
print(tal1)
ny_tal = [2, 3]
tal1.extend(ny_tal)
print(tal1)
#Genom append så kan du lägga till 1 element i slutet av listan
#Genom extend så kan du lägga till flera enskilda element i slutet av listan

#uppgift 2.3
tal1.pop()
print(tal1)
tal1.remove(2)
print(tal1)
#2.4
print(len(list1))

