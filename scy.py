
def insertionSort(intList):
  n = len(intList)
  for i in range(1, n):
   #{
   # sort intList[0], intList[1], ..., intList[i]
   k = i
   while (k > 0) and (intList[k-1] > intList[k]):
   #{
    # swap intList[k] and intList[k-1]
    temp = intList[k-1]
    intList[k-1] = intList[k]
    intList[k] = temp
    k = k - 1
  #}
  #}


def selectionSort(intList):
     n = len(intList)
     for i in range(0, n-1):
         #{
         # find the minimum item in intList[i .. n-1]
         kMin = i
         for k in range(i+1, n):
             if (intList[k] < intList[kMin]):
                kMin = k
             # swap intList[i] and intList[kMin]
             if (kMin != i):
                 temp = intList[i]
                 intList[i] = intList[kMin]
                 intList[kMin] = temp
     #}

def bubbleSort(intList):
     n = len(intList)
     for i in range(0, n-1):
         #{
         for j in range(1, n-i):
             #{
             # compare adj items, swap if in wrong order
             if intList[j-1] > intList[j]:
                 # swap intList[j-1] and intList[j]
                 temp = intList[j-1]
                 intList[j-1] = intList[j]
                 intList[j] = temp
                 #}
                 #}

def bubbleSort(intList):#优化的冒泡算法
     n = len(intList)
     for i in range(0, n-1):
         swapped = False
         for j in range(1, n-i):
             # compare adj items, swap if in wrong order
             if intList[j-1] > intList[j]:
                 # swap intList[j-1] and intList[j]
                 temp = intList[j-1]
                 intList[j-1] = intList[j]
                 intList[j] = temp
                 # remember that swap is needed
                 swapped = True
             if not swapped:
                 # swap is NOT needed, so list is SORTED
                 break

def shellSort(alist):#---------------没看懂
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        print("After increments of size",sublistcount,
            "The list is",alist)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
            currentvalue = alist[i]
            position = i
        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap
        alist[position]=currentvalue
alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)

def mergeSort(alist):#---------------没看懂
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
            # after the first loop end
            temp = alist[first]
            alist[first] = alist[rightmark]
            alist[rightmark] = temp
            return rightmark

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)