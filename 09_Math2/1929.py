#BOJ 1929
#에라토스테네스의 체로 소수 구하는 알고리즘 구현

start, end = map(int, input().split())
era = [1]*(end+1)
era[1] = 0

for i in range(2, int(end**0.5)+1):
    if era[i] == 1:
        for j in range(i*2, end+1, i):
            era[j] = 0

for i in range(start, end+1):
    if era[i] == 1:
        print (i)