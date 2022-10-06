list = [int(x) for x in input().split()]
print("Initialized list: ", list)

list.insert(3, 4)
print("Inserting 4 at index 3: ", list)

list.remove(4)
print("Removing value 4: ", list)

list.append(60)
print("Appending 60: ", list)

list.sort()
print("Sorting: ", list)

x = list.pop()
print("Pop out last element: ", list)

list.reverse()
print("Reversing: ", list)