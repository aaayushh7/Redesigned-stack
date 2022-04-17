from ast import Delete


print("\n\t <--Stacking program-->")
print("\n\033[4mChoose the data type:\033[0m")
print("   1. Dictionary type {i.e. [x,y]}")
print("   2. List type {i.e. [x]}")
sele=int(input("input here -> "))
if sele==1:

    stk=[]
    print("\n \tcurrent list -> ",stk)
    y=0
    x=0
    v=0
    vtk=[]
    t=0
    n=0

    def push(stk):
        n=int(input("enter size of the list -> "))
        for i in range(0,n):
                rolno=int(input("enter roll number -> "))
                name=str(input("enter name -> "))
                stk.append([rolno,name])
                print(stk)


    def pop(stk):
        if stk==[]:
            print("the list is empty")
        else:
            print("object deleted is -> " ,stk.pop())

    def traverse(stk):
        if stk==[]:
            print("\n --> Enter data first")
        else:
            for i in range(len(stk)-1,-1,-1):
                print(stk[i])

    def middle(stk):
        v=len(stk)
        if (v%2)!=0:
            y=(v+1)//2
            print(stk[y-1])
        elif (v%2)==0:
            y=v//2
            print(stk[y-1])

    def edit(stk):
        print("\t 1. Add Elements")
        print("\t 2. Delete element")
        r=int(input("Enter option number -> "))
    

        if r==1:
               k=int(input("Enter number of the inputs -> "))
               for i in range(0,k):
                                     rllno=int(input("Enter roll number -> "))
                                     nme=str(input("enter name -> "))
                                     stk.append([rllno,nme])
                                     vtk.append([rllno,nme])
        print("Updated list is -> ",stk)
        
    
        if r==2:
           
              supscript = str.maketrans("th", "ᵗʰ")
              o=("nth".translate(supscript))
              print("Enter ",o," value below:")
              t=int(input(" --> "))
              del stk[t-1]
    
              print("New list is -> ",stk)
              
    
        else:
            print("Enter valid option")

    

    
    def see(vtk):
            print("Added values so far -> ",vtk)


   
    while True:


        print("\n-------------------------------------")
        print("                 Menu")
        print("-------------------------------------")
        print("1. push values (Recommended)")
        print("2. pop")
        print("3. traverse")
        print("4. middle value")
        print("5. Edit")
        print("6. Show added values")
        print("7. Exit")
        print("-------------------------------")
        x=int(input("Enter choice -> "))
        print("-------------------------------")
        if(x>=9):
              print("\n ---> Enter a valid choice ")
        elif x==3:
                traverse(stk)
        elif x==1:
                push(stk)
        elif x==2:
                pop(stk)  
        elif x==4:
                middle(stk)
        elif x==5:  
                edit(stk)
        elif x==6:
                see(vtk)
  
        elif x==7:
                break

    print("================================")
    print("         program Ended")
    print("================================")

