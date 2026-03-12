import time
time_input = input("Enter time: (HH:MM:SS): ")

hours, minutes, seconds = map(int, time_input.split(":"))

countdown = hours * 3600 + minutes * 60 + seconds

for x in range(countdown, 0, -1):
    hrs = x // 3600
    mins = (x % 3600) // 60
    secs = x % 60
    print(f"{hrs:02}:{mins:02}:{secs:02}", end="\r")
    time.sleep(1)

print("\nTime is up")