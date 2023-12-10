def des_function(right_half, key):
    return [l ^ r for l, r in zip(right_half, key)]


def xor(left, right):
    return [l ^ r for l, r in zip(left, right)]


def swapper(left, right):
    return right + left


data = list(map(int, input("Enter 8 bit data: ")))
key = list(map(int, input("Enter 4 bit key: ")))
print("Data: ", data)
print("Key: ", key)
left_half = data[:4]
right_half = data[4:]
print("Left Half: ", left_half)
print("Right Half:", right_half)
funct = des_function(right_half, key)
print("After XOR of RHS and Key: ", funct)
newLeft = xor(funct, left_half)
print("New Left: ", newLeft)

result = swapper(newLeft, right_half)
print(result)


# def des_function(left_half,key):
#     return [ l^r for l,r in zip(left_half,key)]

# def xor(func,right_half):
#     return [l^r for l,r in zip(func,right_half)]

# def swapper(left,right):
#     return right + left

# data=list(map(int,input("Enter 8-bit data ")))
# key=list(map(int,input("Enter 4-bit key ")))
# print("Data : ",data)
# print("Key :",key)
# left_half=data[:4]
# right_half=data[4:]
# print("Left Half : ",left_half)
# print("Right Half :",right_half)
# func=des_function(left_half,key)
# print("New left half : ",func)
# recv=xor(func,right_half)
# print("New right half : ",recv)
# result=swapper(left_half,recv)
# print(result)