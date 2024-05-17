Q = int(input())
for testcase in range(Q):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    brr = []
    for i in range(len(arr)):
        if i <M-1 :
            continue
        brr.append(arr[i]-arr[i-M+1])
    print(f'#{testcase+1}: {min(brr)}')