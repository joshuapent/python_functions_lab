#1

def sum_to(n):
    int1 = 0
    int2 = 0
    while True:
        int1 += int2
        int2 += 1
        if n == int2:
            n += int1
            return n

# print(sum_to(10))

#2 

# def largest(*args):
#     for arg in args: 
#         print(max(arg))

def largest(*args):
    placeholder = None
    idx = 0
    for arg in args: 
        print(arg[idx])
        idx += 1

        



one = largest([1, 2, 3, 4, 0])  
# two = largest([10, 4, 2, 231, 91, 54])  

# one = largest(1, 2)


print(f"one: {one}, two: {one}")