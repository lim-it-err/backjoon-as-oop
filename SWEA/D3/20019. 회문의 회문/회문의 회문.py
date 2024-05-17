def is_palindrome(input_str):
    left, right = 0, len(input_str)-1
    while left<right:
        if input_str[left] != input_str[right]:
            return False
        left+=1
        right-=1
    return True

T = int(input())
for testcase in range(T):
    input_str = input()
    N = len(input_str)
    if is_palindrome(input_str) and is_palindrome(input_str[:(N-1)//2]) and is_palindrome(input_str[N-(N-1)//2:]):
        print(f"#{testcase+1} YES")
    else:
        print(f"#{testcase+1} NO")

        

