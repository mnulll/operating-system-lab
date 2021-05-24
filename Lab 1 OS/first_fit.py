def best_fit(block_size,x,process_size,y):
    allocate=[-1]*y

    for i in range(y):
        indicator=-1
        for j in range(x):
            if block_size[j]>=process_size[i]:
                indicator=j
                block_size[j]*=-1
                break
        if indicator != -1:
             allocate[i]=indicator
            
    print("Process No. Process Size     Block no.") 
    for i in range(y): 
        print(i + 1, "         ", process_size[i],  
                                end = "         ")  
        if allocate[i] != -1:  
            print("      ",allocate[i] + 1)  
        else: 
            print("Not Allocated") 


blockSize = [100, 500, 200, 300, 600]  
processSize = [212, 417, 112, 426]  
m = len(blockSize)  
n = len(processSize)  
  
best_fit(blockSize, m, processSize, n)