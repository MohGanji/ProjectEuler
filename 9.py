for a in range(2,1000):
    for b in range(2, 1000):
        c = 1000-a-b
        if(c*c == b*b + a*a):
            print a*b*c
            exit()

