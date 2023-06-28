H, M = map(int, input().split())
W = int(input())

HH = (M + W) // 60
MW = (M + W) % 60

if (M + W > 59):
    if (H + HH > 23):
        H = H - 24
    H = H + HH
    print(H, MW)

else:
    if (H > 23):
        H = H - 24
    
    print(H, M + W)