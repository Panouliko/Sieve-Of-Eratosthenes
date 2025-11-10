import time
start = time.time()
n = 10**8 #change freely
numbers = [True] * (n + 1)
numbers[0] = False
numbers[1] = False
for p in range(2, int(n**0.5 + 1)):
    if numbers[p] == True:
        for i in range(p + p, n + 1, p):
            numbers[i] = False
#add printing the primes here if you want
end = time.time()
print(f"Time Elapsed: {end - start:.3f} seconds")


#PS: if this looks too slow, there is a Java version too!