# Health_Managment_System_Using_Python
This is the health management system software. Created only using python .This is very helpful for who are in diet . It takes the input from the user as food Or exercise and store it in a new file with date and time .You can also retrieve the data using this code. 

## importing datetime module


```bash 
  import datetime
  def gettime():
    return datetime.datetime.now()
```
 Datetime module is imported and the real time is taken in a function called gettime() for future use

## Adding Food Or Exercise
```bash
  def log():
    b = int(input("Enter a number 1 for Harry 2 for Rifaz"))
    if b==1:
        c = int(input("Enter a number 1 for food 2 for exercise"))
        if c==1:
            d=int(input("How many Items you want to add"))
            print("Enter The Food Items")
            while d>0:
                e = input()
            
                with open("/storage/emulated/0/Python Examples Made By Rifaz/harryfood.txt","a") as har:
                    har.write(str([str(gettime())])+":"+e+"\n")
                d=d-1
            print("Items successfully Added")           
        elif c==2:
            h=int(input("How many Items you want to add"))
            print("Enter The Exercises")
            while h>0:
                i = input()
            
                with open("/storage/emulated/0/Python Examples Made By Rifaz/harryexe.txt","a") as har:
                    
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
            
                with open("/storage/emulated/0/Python Examples Made By Rifaz/Rifazfood.txt","a") as har:
                    har.write(str([str(gettime())])+":"+l+"\n")
                    k=k -1
            print("Items successfully Added")           
        elif j==2:
            m=int(input("How many Items you want to add"))
            print("Enter The Exercises")
            while m>0:
                n = input()
            
                with open("/storage/emulated/0/Python Examples Made By Rifaz/Rifazexe.txt","a") as har:
                    
                    har.write(str([str(gettime())])+":"+n+"\n")
                    m=m-1
            print("Items successfully Added")   
        else:
               print("invalid Enter")
    else:
            print("invalid Enter")   
```
This is the code used for log items to the file like food or exercise and the entair code is taken in a user-defined function called log().
Here it takes input for 2 persons (you can change the name of the person in this code)
If you want to 
