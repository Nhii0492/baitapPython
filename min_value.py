def get_min_value(arr):
    if not (isinstance(arr, list) and not  isinstance(arr, str)):
        return None 
    if len(arr) == 0:
        return 
    if len(arr) > 0:
        result = arr[0]
        for element in arr: 
            if element < result:
                result = element
        return result 
    else: 
        return None

A = [4, 1, 4, 6, 9, -9]
print("Giá trị nhỏ nhất là", get_min_value(A))


