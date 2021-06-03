def isValidSubsequence(array, sequence):
    i = s = 0
    while i < len(array) and s < len(sequence):
        if array[i] == sequence[s]:
            s+=1
        i+=1
    return s == len(sequence)





if __name__== '__main__':
    result = isValidSubsequence([1,1,1,1,1], [1,1,1])
    print(result)