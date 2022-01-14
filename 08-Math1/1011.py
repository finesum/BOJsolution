#BOJ 1011
#1011_better와 같은 알고리즘이지만 구현이 다르며 연산 및 비교에서 better 버전이 더 낫다.
#이동횟수의 패턴을 구현하기보다(스터디 친구 풀이) 이동횟수의 패턴이 위치와 어떤 연관이 있는지 파악해서
#위치 기준으로 나타나는 패턴에 따라 이동횟수를 반환했다.

def leap(d: int):
    n = 2
    if d == 1:
        return 1
    elif d == 2:
        return 2
    else:
        while n >= 2:
            start = (n-1)*n
            end = n*(n+1)
            if d>start and d<=start+(end-start)/2:
                return n*2-1
            elif d>start+(end-start)/2 and d<=end:
                return n*2
            else:
                n+=1

for i in range(int(input())):
    start, end  = map(int, input().split())
    print (leap(end-start))