def shelf(shop, requests, n):
    print("shop not sort:", shop)
    for k in requests:
        count = 0
        shop_sort = sorted(shop[k[0]-1:k[1]])
        print("shop whith sort:", shop_sort)
        for i in range(1, len(shop_sort)):
            a = abs(shop.index((shop_sort[i])) - shop.index((shop_sort[i-1])))
            print("Добовляем:", a)
            count += a
        if requests.index(k) < n-1:
            count += 1
        print(count)

def data_input():
    requests = []
    shop = list(map(str, input()))
    n = int(input())
    for _ in range(n):
        req = input().split()
        requests.append((int(req[0]), int(req[1])))
    return shop, requests, n

shop, requests, n = data_input()
shelf(shop, requests, n)