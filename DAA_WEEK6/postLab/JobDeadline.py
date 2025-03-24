def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * (max_deadline + 1)
    total_profit = 0
    job_sequence = []

    for job in jobs:
        job_id, deadline, profit = job

        for i in range(min(deadline, max_deadline), 0, -1):
            if slots[i] == -1:
                slots[i] = job_id
                total_profit += profit
                job_sequence.append(job_id)
                break

    return total_profit, job_sequence


jobs = [('A', 4, 20), ('B', 1, 10), ('C', 1, 40), ('D', 1, 30)]
profit, sequence = job_scheduling(jobs)

print(profit)
print("Profit sequence of jobs is", ", ".join(sequence))
