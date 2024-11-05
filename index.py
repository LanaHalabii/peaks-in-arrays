def find_peaks(array):
    peaks = []                                                    #array where we will store the index of the peak values
    len_array = len(array)
    for i in range(1, len_array - 1):                             #exlude first and last values of the array
        if array[i] > array[i - 1] and array[i] > array[i +1]:
            peaks.append(i)                                        #append index of element into the peak array if it is a peak
    
    return peaks

array = [1,5,3,6,2,9]
print(find_peaks(array))

