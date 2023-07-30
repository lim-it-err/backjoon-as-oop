N = int(input())
houses = list(map(int, input().split()))
houses.sort(reverse=True)
if N == 1:
    print(houses[0])
else:
    print(houses[(N)//2])
