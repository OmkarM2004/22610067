import sys
for line in sys.stdin:
    try:
        user, action, time = line.strip().split(",")
        print(f"{user}\t{action},{time}")
    except:
        continue

#Get-Content log.txt | python mapper.py | Sort-Object | python reducer.py 
