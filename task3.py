transactions = [
    "TXN1001", "TXN1002", "TXN1001", "TXN1003", 
    "TXN1004", "TXN1002", "TXN1005", "TXN1001"
]

seen = set()
duplicates = set()


for tx in transactions:
    if tx in seen:
        duplicates.add(tx)
    else:
        seen.add(tx)

unique_transactions = set(transactions)


print("--- Transaction Processing ---")
print("Unique Transactions:", list(unique_transactions))
print("Duplicate Transactions Identified:", list(duplicates))
