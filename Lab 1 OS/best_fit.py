def best_fit(block_size,x,process_size,y):
    allocate=[-1]*y

    for i in range(y):
        indicator=-1
        for j in range(x):
            if block_size[j]>=process_size[i]:
                if indicator == -1:
                    indicator=j
                elif block_size[j]<block_size[indicator]:
                    indicator=j
        if indicator != -1:
             allocate[i]=indicator
             block_size[indicator]*=-1

    print("Process No. Process Size     Block no.") 
    for i in range(n): 
        print(i + 1, "         ", process_size[i],  
                                end = "         ")  
        if allocate[i] != -1:  
            print("      ",allocate[i] + 1)  
        else: 
            print("Not Allocated") 


block_size = [400,300,500,600,700]  
process_size = [126,234,456,677]  
m = len(block_size)  
n = len(process_size)  
  
best_fit(block_size, m, process_size, n)
