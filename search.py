import random
import math

def zapolnenie(number):
    arr=random.sample(range(0,1_000_001),number)
    arr = sorted(arr)
    return arr


def lin_search(arr,number):
    for i in range(len(arr)):
        if arr[i]==number:
            return i
    print("Dont searched")


def bin_search(arr,number,left,right):
    if left>right:
        print("Error")
        return -1
    elif left==right:
        if arr[left]==number:
            return left
        else:
            print("Dont searched")
            return -1
    else:
        middle=math.ceil((right+left)/2)
        if arr[middle]==number:
            return middle
        elif arr[middle]<number:
            return bin_search(arr,number,middle+1,right)
        else:
            return bin_search(arr,number,left,middle-1)

            
def main():
    arr = []
    digit = 100
    arr = zapolnenie (digit)
    position = bin_search(arr,304_212,0,100)
    return position
main()