def Consec_Seven(a_List):
    for i in range(len(a_List)):
        if a_List[i]==7 and a_List[i-1]==7:
            return True
        else:
            pass
    return False
            
Consec_Seven([0,1,7,2,7])

def Sum_Int(a_List):
    sum=0
    for i in range(len(a_List)):
        sum=sum+a_List[i]
        if(a_List[i]==0):
            return(sum)
    return(sum)
Sum_Int([1,20,12,8,0,8,10])


def Int_Sum(a_List):
    sum=0
    i=0
    while i<len(a_List):
        if a_List[i]==2:
            for i in range(i+1,len(a_List)):
                if a_List[i]==3:
                    break
        else:
            sum+=a_List[i]
        i+=1
    return(sum)
        
Int_Sum([1,3,4,2,3,8])
        

           

