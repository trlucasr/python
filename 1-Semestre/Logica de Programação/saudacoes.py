x = int(input())
y = int(input())

i = 0
total = ''
total_bdia = 0
total_btarde = 0
total_bnoite = 0

while i < x:

    total += '\n bom dia'     

    total_bdia += 1

    j = 0

    while j < y:
        
        total += '\n boa tarde'
        total_btarde += 1

        j += 1
    else:
        i += 1
else:
    total += '\n boa noite'
    total_bnoite += 1

with open("Output.txt", "w") as txtfile:
        print(total,file=txtfile)

print(total_bdia, total_btarde, total_bnoite)