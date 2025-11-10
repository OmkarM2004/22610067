import sys
from datetime import datetime

durations = {}
logins = {}

for line in sys.stdin:
    user, val = line.strip().split("\t")
    action, time_str = val.split(",")
    t = datetime.strptime(time_str, "%H:%M")

    if action == "login":
        logins[user] = t
    elif action == "logout" and user in logins:
        duration = (t - logins[user]).total_seconds() / 60
        durations[user] = durations.get(user, 0) + duration
        del logins[user]

if durations:
    max_time = max(durations.values())
    for u, d in durations.items():
        if d == max_time:
            print(f"{u}\t{d}")
