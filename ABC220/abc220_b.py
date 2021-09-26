K = int(input())
A, B = map(int, input().split())

A_digits = [int(i) for i in str(A)]
B_digits = [int(i) for i in str(B)]
A_dec = 0
B_dec = 0
for i in range(len(A_digits)):
    A_dec += A_digits[-i-1] * (K**i)
for i in range(len(B_digits)):
    B_dec += B_digits[-i-1] * (K**i)

print(A_dec*B_dec)