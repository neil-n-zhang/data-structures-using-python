import timeit
def rec_fib_seq(n):
    if n==1 or n==2:
        return 1
    else:
        return rec_fib_seq(n-2)+rec_fib_seq(n-1)

def iter_fib_seq(n):
    if n==1 or n==2:
        return 1
    else:
        prior_one=1
        prior_two=1
        for i in range(n-2):
            num=prior_one+prior_two
            prior_one=prior_two
            prior_two=num
        return num

time_rec = timeit.Timer("rec_fib_seq(6)","from __main__ import rec_fib_seq")
print("Time for recursion is", time_rec.timeit(number=1000))

time_iter=timeit.Timer("iter_fib_seq(6)","from __main__ import iter_fib_seq")
print("Time for iteration is", time_iter.timeit(number=1000))
