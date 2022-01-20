#BOJ 3009
#네 개의 점 중 세 개의 점이 주어졌을 때 나머지 한 점 구하기 - 좋은 알고리즘 아이디어!

x = [] * 3
y = [] * 3
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
print (sum(list(set(x)))*2-sum(x), sum(list(set(y)))*2-sum(y))