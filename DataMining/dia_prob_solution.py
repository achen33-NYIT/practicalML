

def stringCompr(inputStr):
    myTable = {}
    result = ''
    inputArr = list(inputStr)
    prev = ''
    curr = ''
    
    
    for idxOne, x in enumerate(inputArr): # curr char
        curr = x
        count = 1
        if curr == prev:
            continue
        lookAheadArr = inputArr[idxOne + 1:]
        for idxTwo, y in enumerate(lookAheadArr): # counting number of chars in seq # break out of inner loop if no more in seq
            if x != y:
                myTable[x] = count
                prev = x
                break # break out of loop
            else:
                count += 1
        prev = x
        myTable[x] = count # if str ends with a sequence of same char
        if myTable[x] == 1:
            result += x
        else:
            result += (x + str(myTable[x]))
    return result

resultOne = stringCompr("abcaaabbb")
resultTwo = stringCompr("abcd")
print('Test 1:', ('abca3b3' == resultOne))
print('Test 2:', ('abcd' == resultTwo))


  
        