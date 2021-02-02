class array1():
    def __init__(self, myarray):
        self.myarray = myarray

    # len method
    def len(self):
        return len(self.myarray)

    # get method
    def get(self, i):
        return self.myarray[i]

    # set method
    def set(self, val, i):
        self.myarray[i] = val
        return self.myarray


# dynamic array
class array2(array1):

    # add method
    def add(self, val):
        for i in range(super().len()):
            if i == super().len() - 1:
                self.myarray.append(val)
        return self.myarray

    # delete method
    def dele(self):
        for i in range(super().len()):
            if i == super().len() - 1:
                self.myarray.pop(i)
        return self.myarray


#  Other Functions

# contain function
def contains(myarray, val):
    i = 0
    while i != myarray.len():
        if val == myarray.get(i):
            return True
        else:
            i += 1
    return False


# reverse function
def reverse(myarray):
    new_array = []
    for i in range(myarray.len() - 1, -1, -1):
        new_array.append(myarray.get(i))
    return new_array


# insert function
def insert(myarray, val, n):
    i = 0
    new_array = []
    while i != myarray.len():
        if i == n:
            new_array.append(val)
            new_array.append(myarray.get(i))
        else:
            new_array.append(myarray.get(i))
        i += 1
    return new_array


# Initializing the array
arrayel = array2([5, 4, 2, 1, 9, 8])

# Executing the methods
print("Len = ", arrayel.len())
print("Get = ", arrayel.get(3))
print("Set = ", arrayel.set(3, 2))
print("Add = ", arrayel.add(7))
print("Delete(last element) = ", arrayel.dele())
print("Contains = ", contains(arrayel, 1))
print("Reverse = ", reverse(arrayel))
print("Insert = ", insert(arrayel, 3, 0))

# Time complexity: o(n)
# Space complexity: o(n)
