from blockchain.blockchain_interface import (
    get_total_records,
    get_record
)

total = get_total_records()

print("Total Records:", total)

for i in range(total):
    print(f"\nRecord {i}")
    print(get_record(i))