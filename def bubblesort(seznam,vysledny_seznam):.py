def bubblesort(seznam):
    a=0
    while a < len(seznam):
        print('ok')
        if seznam[a]>seznam[a+1]:
            x=seznam[a]
            seznam[a]=seznam[a+1]
            seznam[a+1]=x
        return seznam
        
    a+=1
    return a   
    
    


seznam = [5,2,13,-12,54,-100]

bubblesort(seznam)
print(seznam)