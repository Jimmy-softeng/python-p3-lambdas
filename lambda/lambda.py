class Lambda:
    def myfunct(x):
        return lambda a,b:(a+b)*x
    
    sum_times_2=myfunct(2)
    print(sum_times_2(10,20))
    