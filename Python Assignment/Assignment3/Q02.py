#2. Find the numbers between 100 and 500, which are divisible by 3 and multiples of 5 using function in Python.

def find_nums():
    nums = []
    for i in range(100, 500):
        if i % 3 == 0 and i % 5 == 0:
            nums.append(i)
    return nums

print(find_nums())

'''
Output
[105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300, 315, 330, 345, 360, 375, 390, 405, 420, 435, 450, 465, 480, 495]
'''
