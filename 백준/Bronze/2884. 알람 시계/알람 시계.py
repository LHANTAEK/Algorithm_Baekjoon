hour, minute = map(int, input().split())
alarm = minute - 45

if alarm < 0:
    minute = 60 + alarm
    if hour == 0:
        hour = 23
    else:
        hour -= 1
else:
    minute = alarm
        
print(f"{hour} {minute}")