def max_activities(activities):
    activities.sort(key=lambda x: x[1])

    count = 1
    last_end_time = activities[0][1]

    for i in range(1, len(activities)):
        if activities[i][0] >= last_end_time:
            count += 1
            last_end_time = activities[i][1]

    return count

activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8)]
print(max_activities(activities))  # Output: 3
