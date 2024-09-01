def numberOfTriplets(input1, input2, input3, input4, input5, input6):
    ans=0
    third=[]
    for i in range(0,input2):
        for j in range(0,input4):
            third.append(input1[i]^input3[j])
    for i in range(0,input6):
        for j in range(0,len(third)):
            if (bin(input5[i] ^ third[j]).count('1')) % 2 == 0:
                ans+=1
    return ans

if __name__ == '__main__':
    print(numberOfTriplets([1,2],2,[3],1,[2,3],2))
