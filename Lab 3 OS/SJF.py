def SJF(at, bt):
    time = 0
    arrival_time = at[0]
    burst_time = bt[0]
    burst = []*len(bt)
    arrive = []*len(at)
    complete = []*len(at)
    turnaround = []*len(at)
    waiting = []*len(at)
    current_process = 0
    for i in range(len(at)):
        if at[i] < arrival_time:
            current_process = i
            arrival_time = at[i]
            burst_time = bt[i]
        elif at[i] == arrival_time:
            if bt[i] < burst_time:
                current_process = i
                arrival_time = at[i]
                burst_time = bt[i]

    # print(current_process)
    # print(at)
    # print(bt)
    time += arrival_time
    while len(at) != 0:
        time += burst_time
        complete.append(time)
        # print(at)
        # print(current_process)
        arrive.append(at[current_process])
        burst.append(bt[current_process])
        turnaround.append(time-at[current_process])
        waiting.append(time-at[current_process]-bt[current_process])
        at.pop(current_process)
        bt.pop(current_process)
        for i in range(len(at)):
            if at[i] <= time:
                current_process = i
                burst_time = bt[i]
                arrival_time = at[i]
                break
        for i in range(len(at)):
            if at[i] <= time:
                if bt[i] < burst_time:
                    burst_time = bt[i]
                    arrival_time = at[i]
                    current_process = i
                elif bt[i] == burst_time and at[i] < arrival_time:
                    burst_time = bt[i]
                    current_process = i
                    arrival_time = at[i]

    print("Arrival Time    Burst time   Complete time     Turnaround Time      Waiting time")
    for i in range(len(arrive)):
        print(arrive[i], "\t\t", burst[i],
              "\t\t", complete[i], "\t\t", turnaround[i], "\t\t\t", waiting[i])


x = [2, 3, 0, 4, 5]
y = [6, 5, 5, 1, 3]
SJF(x, y)
