emails = [
    "ali@gmail.com", "sara@yahoo.com", "ali@gmail.com", 
    "ahmed@gmail.com", "sara@yahoo.com", "zain@hotmail.com"
]


unique_ordered = list(dict.fromkeys(emails))


unique_unordered = list(set(emails))

print("--- Data Cleaning Results ---")
print("Original Dataset:", emails)
print("\nUnique Emails (Order Preserved):", unique_ordered)
print("Unique Emails (Order Not Preserved):", unique_unordered)
