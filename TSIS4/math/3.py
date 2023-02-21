import math
print("Input number of sides:")
n = int(input())
print("Input the length of a side:")
l = int(input())
Area = n*pow(l,2)/math.tanh(180/n)/4
print(f"The area of the polygon is:{Area}")