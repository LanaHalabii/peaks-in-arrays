def find_peaks(array):
    peaks = []
    len_array = len(array)
    for i in range(1, len_array - 1):
        if array[i] > array[i - 1] and array[i] > array[i +1]:
            peaks.append(i)
    
    return peaks

array = [1,5,3,6,2,9]
print(find_peaks(array))

