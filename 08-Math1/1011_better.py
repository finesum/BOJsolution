#BOJ 1011_better
#위치 기준 패턴을 더 간단하게 구현. while True 또한 자주 써야겠다.
#Runtime 측면에서 개선된 버전.

def leap(d: int):
    n = 2
    if d == 1:
        return 1
    elif d == 2:
        return 2
    else:
        while True:
            if d <= n*(n+1):
                break
            n+=1
        if d<=n*n:
            return n*2-1
        else:
            return n*2

for i in range(int(input())):
    start, end  = map(int, input().split())
    print (leap(end-start))