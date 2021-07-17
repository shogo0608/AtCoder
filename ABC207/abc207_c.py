class Area:
    def __init__(self, t, l, r):
        self.t = t
        self.l = l
        self.r = r

def main():
    # 入力
    N = int(input())
    areas = {}
    for i in range(1, N+1):
        t, l, r = [int(j) for j in input().split()]
        areas[i] = Area(t, l, r)

    # 処理
    answer = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            # 区間が明らかに被っているもの
            if areas[i].l < areas[j].r and areas[j].l < areas[i].r:
                answer += 1
            # 閉区間か開区間かで被るか被らないか変わるもの
            elif areas[i].l == areas[j].r:
                if areas[i].t in [1, 2] and areas[j].t in [1, 3]:
                    answer += 1
            elif areas[i].r == areas[j].l:
                if areas[i].t in [1, 3] and areas[j].t in [1, 2]:
                    answer += 1

    # 出力
    print(answer)

if __name__ == '__main__':
    main()