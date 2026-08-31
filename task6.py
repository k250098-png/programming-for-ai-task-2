logs = ["INFO", "ERROR", "WARNING", "INFO", "ERROR", "INFO", "WARNING", "INFO"]


log_counts = {}
for log in logs:
    log_type = log.strip()
    log_counts[log_type] = log_counts.get(log_type, 0) + 1


unique_log_types = list(log_counts.keys())


most_frequent_log = max(log_counts, key=log_counts.get)

print("--- Log Analysis Results ---")
print("Occurrences of each log type:", log_counts)
print("Log types that appeared:", unique_log_types)
print(f"Most frequent log type: {most_frequent_log} ({log_counts[most_frequent_log]} occurrences)")
