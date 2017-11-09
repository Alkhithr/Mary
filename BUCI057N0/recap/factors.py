def primes(n):
    primfac = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac




def main():
    n = 175
    x = primes(n)
    print('The prime factorization of {} is {}'.format(n, x))



main()
