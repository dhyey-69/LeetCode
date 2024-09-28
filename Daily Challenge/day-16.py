t = ["00:00", "23:59", "00:00"]

def xyz(timepoints):
    new_time = []
    
    for i in timepoints:
        i = i.split(':')
        new_time.append(i)

    time_min = []
    
    for i in new_time:
        temp_min = (int(i[0]) * 60) + int(i[1])
        time_min.append(temp_min)
    
    time_min = sorted(time_min)
    print(time_min)

    min_diff = float('inf')
    
    for i in range(1, len(time_min)):
        min_diff = min(min_diff, time_min[i] - time_min[i - 1])
    
    min_diff = min(min_diff, 1440 + time_min[0] - time_min[-1])

    return min_diff

print(xyz(t))