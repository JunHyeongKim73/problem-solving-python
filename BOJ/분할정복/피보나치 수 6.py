
# F(M+N) = F(M-1)F(N) + F(M)F(N+1)

DIV = 1000000007

m = dict()
def fibo(num):
    if num == 1 or num == 2:
        return 1
    
    if num in m:
        return m[num]
    
    M = num - int(num/2)
    N = int(num/2)
    
    res = (fibo(M-1)*fibo(N)+fibo(M)*fibo(N+1)) % DIV
    m[num] = res
    return res

if __name__ == '__main__':
    n = int(input())
    res = fibo(n)

    print(res)