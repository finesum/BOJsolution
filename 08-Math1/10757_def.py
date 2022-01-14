#BOJ 10757
#파이썬에서의 int는 비교적 범위가 커서 단순히 +로도 연산이 가능했으나
#만약 가능하지 않다는 조건 하에 큰 수 더하기 연산을 함수로 구현함.


def bigsum(a, b):
    a = a[::-1]
    b = b[::-1]
    remain = 0
    result = []
    for i in range(len(a)):
        res = int(a[i]) + int(b[i]) + remain
        remain = res//10
        result.insert(0, str(res%10))
    if remain >= 1:
        result.insert(0, str(remain))
    return result

a, b = input().split()
print("".join(bigsum(a.zfill(max(len(a), len(b))), b.zfill(max(len(a),len(b))))))