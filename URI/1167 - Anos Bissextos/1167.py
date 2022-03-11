anoinicio = int(input())
anofim = int(input())
qtdbissexto = 0

if (0 <= anoinicio <= anofim <= 9999):
    while anoinicio <= anofim:
        if (anoinicio % 4 == 0 and anoinicio % 100 != 0 or anoinicio % 400 == 0):
            print(anoinicio)
            qtdbissexto += 1

        anoinicio += 1

    print('bissextos:', qtdbissexto)