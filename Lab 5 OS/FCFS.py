def FCFS(at, bt):
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

    time += arrival_time
    flag = True
    while len(at) != 0:
        if flag:
            time += burst_time
            complete.append(time)
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
                flag = True
                break
            else:
                flag = False

        if flag:
            for i in range(len(at)):
                if at[i] < arrival_time:
                    current_process = i
                    burst_time = bt[i]
                    arrival_time = at[i]
        elif len(at) != 0:
            time += 1

    print("Arrival Time    Burst time   Complete time     Turnaround Time      Waiting time")
    for i in range(len(arrive)):
        print(arrive[i], "\t\t", burst[i],
              "\t\t", complete[i], "\t\t", turnaround[i], "\t\t\t", waiting[i])


x = [5, 0, 4, 6, 4]
y = [2, 1, 3, 5, 4]
FCFS(x, y)
