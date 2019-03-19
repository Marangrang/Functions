def bubble_sort(items):
    for i in range(len(items) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):
            if items[j + 1] < items[j]:
                items[j], items[j + 1] = items[j + 1], items[j]
                no_swap = False
        if no_swap:
            return


def merge_sort(items):
    if len(items) >1:
        mid = len(items)//2 #Finding the mid of the array
        L = items[:mid] # Dividing the array elements
        R = items[mid:] # into 2 halves

        merge_sort(L) # Sorting the first half
        merge_sort(R) # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                items[k] = L[i]
                i+=1
            else:
                items[k] = R[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(L):
            items[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            items[k] = R[j]
            j+=1
            k+=1

# Code to print the list
def printList(items):
    for i in range(len(items)):
        print(items[i],end=" ")


def quick_sort(items):
    """Quicksort using array"""
    if items == []:
        return []
    else:
        pivot = items[0]
        lesser = quick_sort([x for x in items[1:] if x < pivot])
        greater = quick_sort([x for x in items[1:] if x >= pivot])
        return lesser + [pivot] + greater
