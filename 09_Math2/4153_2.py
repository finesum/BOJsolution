#BOJ 4153
#정렬 후 인덱스 사용해서 식 세움.
#스터디원 풀이: 최댓값 value를 리스트에서 지운 뒤 인덱스 0, 1 사용

while True:
    a, b, c  = map(int, input().split())
    size = sorted([a, b, c])
    if a == 0 and b == 0 and c == 0:
        break
    elif size[2]**2 == size[0]**2 + size[1]**2:
        print("right")
    else:
        print("wrong")