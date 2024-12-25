N = map(int, input().split())
power_N = []

for i in N:
    power_N.append(i**2)

print(sum(power_N) % 10)