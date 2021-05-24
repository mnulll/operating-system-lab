def banker(n, m, max, allocate):
    safe_sequence = []*n
    needed = [[0 for i in range(m)]for j in range(n)]
    available = [1, 5, 2, 0]
    for i in range(n):
        for j in range(m):
            needed[i][j] = max[i][j]-allocate[i][j]
    print("Allocation        Max            Needed          Available\n")
    flag = [0]*n
    for i in range(n):
        for j in range(n):
            if flag[j] == 0:
                boolean = True
                for k in range(m):
                    if needed[j][k] > available[k]:
                        boolean = False
                        break
                if boolean:
                    safe_sequence.append(j)
                    for z in range(m):
                        print(allocate[j][z], end=" ")
                    print("\t", end=" ")
                    for z in range(m):
                        print(max[j][z], end=" ")
                    print("\t", end=" ")
                    for z in range(m):
                        print(needed[j][z], end=" ")
                    print("\t", end=" ")
                    for z in range(m):
                        print(available[z], end=" ")
                    print()
                    for z in range(m):
                        available[z] += allocate[j][z]
                    flag[j] = 1
    if sum(flag) == n:
        print("\nSafe state")
    else:
        for i in range(n):
            if flag[i] == 0:
                for z in range(m):
                    print(allocate[i][z], end=" ")
                print("\t", end=" ")
                for z in range(m):
                    print(max[i][z], end=" ")
                print("\t", end=" ")
                for z in range(m):
                    print(needed[i][z], end=" ")
                print("\t", end=" ")
                print("Exceed available resources")
                print("\n\nUnsafe State")
    print("\nSafe Sequence: ", end=" ")
    for i in range(len(safe_sequence)):
        print("> P", safe_sequence[i], end="\t")


num_processes = 5
num_devices = 4
max_resources = [[0, 0, 11, 2], [1, 7, 1, 0],
                 [2, 3, 5, 6], [0, 6, 5, 2], [0, 6, 2, 6]]
allocated_resources = [[0, 0, 1, 2], [1, 0, 0, 0],
                       [1, 3, 5, 4], [0, 6, 3, 2], [0, 0, 1, 4]]
banker(num_processes, num_devices, max_resources, allocated_resources)
