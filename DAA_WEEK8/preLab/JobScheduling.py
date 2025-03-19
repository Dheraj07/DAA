def job_scheduling(jobs):
    jobs.sort(key=lambda x:x[0], reverse=True )
    max_deadline=max(job[1] for job in jobs)
    time_slots=[-1]*max_deadline
    total_profit=0

    for index, (profit,deadline) in enumerate(jobs):
        for slot in range(min(deadline,max_deadline)-1,-1,-1):
            if time_slots[slot]==-1:
                time_slots[slot]=index
                total_profit+=profit
                break
    job_sequence=[jobs[i] for i in time_slots if i!=-1]
    return job_sequence,total_profit
jobs = [(5, 2), (4, 1), (6, 2), (3, 1)]
job_sequence, max_profit = job_scheduling(jobs)

print("Job sequence:", [jobs.index(job) + 1 for job in job_sequence])
print("Maximum profit:", max_profit)
