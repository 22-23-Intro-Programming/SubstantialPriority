def factorial(int1):
    count=1
    while(int1>=1):
        count=count*int1
        int1=int1-1
    print(count)


def double_it():
    input1=input("please enter a phrase you would like to double")
    for i in range(0,len(input1)):
        print(input1[i])
        print(input1[i])

            
def camel_case():
    in1=input("please enter a filename")
    replacement=in1
    for i in range (0,len(in1)):
        if(in1[i]== " "):
           replacement=replacement.title()
           replacement=replacement.replace(" ","")
        if(in1[i]=="/"):
            replacement=replacement.replace(in1[i], "-") 
    print(replacement)
        
def main():
    factorial(10)
    factorial(5)
    factorial(3)
    double_it()
    double_it()
    double_it()
    camel_case()
    camel_case()
main()    
