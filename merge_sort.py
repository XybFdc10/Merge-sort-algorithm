def merge(left, right):
    i = 0
    j = 0
    new_arr = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_arr.append(left[i])
            i+=1
        else:
            new_arr.append(right[j])
            j+=1
    new_arr += left[i:]
    new_arr += right[j:]
    return new_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]    
    right_arr = arr[mid:]   

    # recursiion

    left = merge_sort(left_arr)     
    right = merge_sort(right_arr)   

    # merge

    return merge(left, right)

nums = [5, 1, 7, 7, 3, 2, 0]
print(merge_sort(nums))
