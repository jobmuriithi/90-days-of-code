from datetime import datetime

now = datetime.now()

formatted = now.strftime("%d %b %Y")

print(formatted)

from datetime import datetime

deadline = datetime(2026, 12, 31)

print("Deadline:", deadline)

from datetime import datetime

today = datetime.now()

deadline = datetime(2026, 12, 31)

remaining_time = deadline - today
print("Remaining time:", remaining_time)