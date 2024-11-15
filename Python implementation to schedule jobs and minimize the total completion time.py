def job_scheduling(processing_times):
    """
    Schedule jobs to minimize total completion time using a greedy algorithm.

    :param processing_times: List of job processing times.
    :return: Total completion time and the job order.
    """
    # Sort jobs by processing times (shortest job first)
    sorted_jobs = sorted(processing_times)
    
    total_completion_time = 0
    current_time = 0
    job_order = []

    # Calculate total completion time
    for time in sorted_jobs:
        current_time += time
        total_completion_time += current_time
        job_order.append(time)

    return total_completion_time, job_order


# Example usage
processing_times = [4, 2, 8, 3, 5]  # Example job processing times
total_time, order = job_scheduling(processing_times)

print("Total Completion Time:", total_time)
print("Job Order:", order)
