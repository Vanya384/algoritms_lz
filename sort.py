import random

def zapolnenie(arr,digit):
    for i in range(digit):
        arr.append(random.randint(0,100001))


def bubble_Sort(arr):
    length=len(arr);
    i=0;
    for i in range(length):
        for j in range(length-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        print(arr)


def selection_sort(arr):
    length=len(arr)
    i=0
    j=0
    for i in range(length):
        min_index=0
        for j in range(length-i):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[min_index],arr[length-i-1]=arr[length-i-1],arr[min_index]
        print(arr)


def main():
    arr=[]
    digit=100
    zapolnenie(arr,digit)
    selection_sort(arr)
    print(arr)

main()




