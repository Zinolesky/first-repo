# Timer
import time

my_time = int(input("Enter time in seconds: "))

for sec in reversed(range(1, my_time + 1)):
    seconds = int(sec % 60)
    minutes = int((sec / 60) % 60)
    hours = int((sec / 60) / 60)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time up!")
