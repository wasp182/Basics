def bubble_sort(data:list):
    n = len(data)
    comp = 0
    for i in range(n-1):
        swapped = False
        # sort jth item in data to the correct position
        # after each ith iteration first i terms are sorted in list to their correct position
        # hence we need to do only n-1-i comparisons
        for j in range(n-1-i):
            comp+=1
            if data[j+1] < data[j]:
                data[j+1],data[j] = data[j],data[j+1]
                swapped = True
            print(data)
        # only to check if the list is already sorted or not
        if not swapped:
            break
    print(data)
    print(comp)


bubble_sort([26,486,16,4,5,89,1,351])
