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
        


# one = largest([1, 2, 3, 4, 0])  
# two = largest([10, 4, 2, 231, 91, 54])  

# print(f"one: {one}, two: {two}")