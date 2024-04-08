def find_negative(arr, count=0):
    if len(arr) == 0:
        return count
    elif arr[0] < 0:
        count += 1
        return find_negative(arr[1:], count)
    else:
        return find_negative(arr[1:], count)


array = [-2, -5, 3, 0, -7, 10]
print(find_negative(array))
