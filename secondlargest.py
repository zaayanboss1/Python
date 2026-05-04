def arrayMean(arr,arr_size):
    total_sum=0
    for i in range(0,arr_size):
        total_sum += arr[i]

    return float(total_sum/arr_size)

def arrayMedian(arr,arr_size):
    sorted(arr)
def print2largest(a,a_size):
    largest=secondLargest=-2147483648
    for i in range(a_size):
        if (a[i]>largest):
            secondLargest=largest
            largest=a[i]


        elif (a[i]>secondLargest and a[i]!=largest):
            secondLargest=a[i]

    print(secondLargest)