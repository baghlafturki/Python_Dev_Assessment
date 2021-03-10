def is_subsequence(array, sequence):
    '''
    A function to check if the second list (sequence) is a subsequence
    of the first list (array)
    '''

    #both lists are not empty
    #and subsequence array is not larger than main array
    valid = len(array) >= len(sequence) and len(sequence)!=0

    result = False
    
    if valid:
        se_pointer = 0

        # for each number in array
        for num in array:

            # if there is still numbers in sequence
            if se_pointer < len(sequence):
                # increment pointer if a mach was found
                se_pointer = se_pointer + 1 if num == sequence[se_pointer] else se_pointer
    
        # if number of pointers equals the length,
        # this means second list is a subsequence of the first
        if se_pointer == len(sequence):
            result = True

    return "true" if result is True else "false"
        



array = [5,1,22,25,6,-1,9,10]
sequence = [1,6,-1,10]


print(is_subsequence(array, sequence))
    
