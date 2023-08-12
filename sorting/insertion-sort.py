num = [5,3,8,6,7,2]

def insertion_sort(num):
    for i in range(1,len(num)):
        key = num[i]
        j = i - 1
        while j>=0 and key<num[j]:
            num[j+1] = num[j]
        num[j+1]=key
    print(num)

insertion_sort(num)