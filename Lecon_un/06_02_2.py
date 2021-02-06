def f_1(*args, **kwargs):
    print(args[0], args[1])
    print(kwargs['a'])


f_1(1, 2, a=44)
f_1(1, 2, 3, a=33)
