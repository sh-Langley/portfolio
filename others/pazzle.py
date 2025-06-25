def replacement(q):

    n = len(q)
    count_r = 0

    for i in range(0,n-1):
        min = i
        for j in range(i+1,n):
            if(q[j] < q[min]):
                min = j
        if(min != i):
            tmp = q[min]
            q[min] = q[i]
            q[i] = tmp
            count_r += 1

    print(f'{"整列後の行列"}{q}')

    return count_r

def fall(x):

    m = len(x)
    count_t = 0

    for w in range(0,m-1):
        for l in range(w+1,m):
            if(x[w] > x[l]):
                count_t += 1
                print(x[w],x[l])

    return count_t

def main():
    p = (2,6,3,1,7,5,4,8) #行列入力部
    print(f'{"整列前の行列"}{list(p)}')
    r = replacement(list(p))
    f = fall(p)

    print(f'{"置換回数は"}{r}{"回"}')
    print(f'{"転倒数は"}{f}')

    if(r%2 == 0 and f%2 == 0):
        print("偶置換")

    else:
        print("奇置換")

if __name__ == "__main__":
    main()
