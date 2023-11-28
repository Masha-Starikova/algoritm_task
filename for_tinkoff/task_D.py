n = int(input())
A = list(map(int, input().split()))
print(A)

off = A[1::2]
on = A[0::2]
sum_A = sum(on)
print('сумма подписок', sum_A)
min_on = min(on)
max_off = max(off)

if max_off > min_on:
    result = sum_A - min_on + max_off
    if result > sum_A:
        print(result)
    else:
        print(sum_A)
else:
    print(sum_A)