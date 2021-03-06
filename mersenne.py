from prime import is_prime_prob, isprime
import time

base = 2
exponent = 21701
starttime = time.time()
count = 0

try:
    while True:
        cur = time.time()
        print(f"Checking {base}^{exponent}... ", end='')
        if not isprime(exponent):
            exponent+=2
            print()
            continue
        if is_prime_prob(base**exponent-1):
            print(f"M({exponent}) is probably prime")
            break
        exponent+=2
        count+=1
        end = time.time() - cur
        print(f"{end:.2f} seconds")
except KeyboardInterrupt:
    print("Found {} probable primes in {} seconds".format(count, time.time()-starttime))    
