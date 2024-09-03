num=int(input("Enter the Number"))

previous=0

current=1

isfibo=False

if num in (0,1):

    isfibo=True
      
else:
    
    next=previous+current
    
    while(next<=num):
        
        next=previous+current
        
        previous=current
        
        current=next
        
        if next==0:
            
            isfibo=True
            
            break

print(isfibo)

