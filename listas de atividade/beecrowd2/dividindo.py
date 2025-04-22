N = int(input())
for _ in range(N):
    X, Y = map(int, input().split())
    if Y == 0:
        print("divisao impossivel")
    else:
        result = X / Y
        print(f"{result:.1f}")
