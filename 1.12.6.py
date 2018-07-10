n = int(input())
p = 'программист'
if (n % 10 == 1) and (n != 11) and (n != 111) and (n != 211) and (n != 311) and (n != 411) and (n != 511) and (n != 611) and (n != 711) and (n != 811) and (n != 911):
    print(n, p + '')
elif ((n % 10 == 2) or (n % 10 == 3) or (n % 10 == 4)) and ((n != 12) and (n != 13) and (n != 14) and (n != 112) and (n != 113) and (n != 114) and (n != 212) and (n != 213) and (n != 214) and (n != 312) and (n != 313) and (n != 314) and (n != 412) and (n != 413) and (n != 414) and (n != 512) and (n != 513) and (n != 514) and (n != 612) and (n != 613) and (n != 614) and (n != 712) and (n != 713) and (n != 714) and (n != 812) and (n != 813) and (n != 814) and (n != 912) and (n != 913) and (n != 914)):
    print(n, p + 'а')
else:
    print(n, p + 'ов')