import random
import math

def zapolnenie(number):
    arr=random.sample(range(0,1_000_001),number)
    arr = sorted(arr)
    return arr


def lin_search(arr,number):
    for i in range(len(arr)):   #пробегаем по массиву,сверяем исходное число со всеми элементами 
        if arr[i]==number:
            return i
    print("Dont searched")


def bin_search(arr,number,left,right):
    if left>right: #неправильно заданное условие
        print("Error")
        return -1
    elif left==right: #если правая и левая границы равны,то элемент всего один
        if arr[left]==number:
            return left
        else:
            print("Dont searched")
            return -1
    else:
        middle=math.ceil((right+left)/2)   #находим центральный индекс
        if arr[middle]==number:
            return middle
        elif arr[middle]<number:
            return bin_search(arr,number,middle+1,right) #если центральный элемент меньше исходного числа,то число лежит в правой части(справа от центра)
        else:
            return bin_search(arr,number,left,middle-1)  ##если центральный элемент больше исходного числа,то число лежит в левой части(слева от центра)

            
def main():
    arr = []
    digit = 100
    arr = zapolnenie (digit)
    position = bin_search(arr,304_212,0,100)
    return position
main()
