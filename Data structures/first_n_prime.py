def prime_lst(n):
    prime = [1]*(n+1)
    prime[0] = 0
    prime[1] = 0
    for i in range(2,1+(n+1)//2):
        for j in range(2,n):
            ind = i*j
            if ind< n+1:
                prime[ind]=0
            else:
                break
    return prime

print(prime_lst(15))