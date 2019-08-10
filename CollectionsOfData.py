from Product_Info import  Product_Info

# price 오름차순
def quick_sorted(arr):
    if len(arr) > 1:
        pivot = arr[len(arr) - 1].price
        left, mid, right = [], [], []
        for i in range(len(arr) - 1):
            if arr[i].price < pivot:
                left.append(arr[i])
            elif arr[i].price > pivot:
                right.append(arr[i])
            else:
                mid.append(arr[i])
        mid.append(arr[len(arr) - 1])
        return quick_sorted(left) + mid + quick_sorted(right)
    else:
        return arr
