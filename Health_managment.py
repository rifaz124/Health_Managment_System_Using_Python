import datetime
def gettime():
    return datetime.datetime.now()
def log():
    b = int(input("Enter a number 1 for Harry 2 for Rifaz"))
    if b==1:
        c = int(input("Enter a number 1 for food 2 for exercise"))
        if c==1:
            d=int(input("How many Items you want to add"))
            print("Enter The Food Items")
            while d>0:
                e = input()
            
                with open("harryfood.txt","a") as har:
                    har.write(str([str(gettime())])+":"+e+"\n")
                d=d-1
            print("Items successfully Added")           
        elif c==2:
            h=int(input("How many Items you want to add"))
            print("Enter The Exercises")
            while h>0:
                i = input()
            
                with open("harryexe.txt","a") as har:
                    
                    har.write(str([str(gettime())])+":"+i+"\n")
                    h = h-1
            print("Items successfully Added")   
        else:
            print("Invalid Enter")
    elif b==2:
        j = int(input("Enter a number 1 for food 2 for exercise"))
        if j==1:
            k=int(input("How many Items you want to add"))
            print("Enter The Food Items")
            while k>0:
                l = input()
            
                with open("Rifazfood.txt","a") as har:
                    har.write(str([str(gettime())])+":"+l+"\n")
                    k=k -1
            print("Items successfully Added")           
        elif j==2:
            m=int(input("How many Items you want to add"))
            print("Enter The Exercises")
            while m>0:
                n = input()
            
                with open("Rifazexe.txt","a") as har:
                    
                    har.write(str([str(gettime())])+":"+n+"\n")
                    m=m-1
            print("Items successfully Added")   
        else:
               print("invalid Enter")
    else:
            print("invalid Enter")          
            
def retrieve():
                    f = int(input("Enter a number 1 for Harry 2 For Rifaz"))
                    if f==1:
                        g = int(input("Enter A number 1 for food 2 for exercise"))
                        if g==1:
                             with open("harryfood.txt") as hf:
                                 print(hf.read())
                        elif g==2:
                             with open("harryexe.txt") as hf:
                                 print(hf.read())
                        else:
                            print("Invalid Enter")
                    elif f==2:
                        o = int(input("Enter A number 1 for food 2 for exercise"))
                        if o==1:
                             with open("Rifazfood.txt") as hf:
                                 print(hf.read())
                        elif o==2:
                             with open("Rifazexe.txt") as hf:
                                 print(hf.read())       
                                 
                        else:
                            print("Invalid enter")
                    else:
                        print("Invalid Enter")
print("Enter A Number 1 for log 2 for retrieve")
a = int(input())
if a==1:
    log()
elif a==2:
    retrieve()
else:
    print("please restart and enter 1 or 2")                    
                    
                    
                    
