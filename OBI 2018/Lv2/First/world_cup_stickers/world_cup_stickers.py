NCM = list(input().split())
special_stickers = list(input().split())
my_stickers = set(list(input().split()))
missing_specials = NCM[1]
my_album = []


for i in range(0, int(NCM[0])):
    my_album.append(0)

for i in range(0, NCM[2]):
    my_album[my_stickers[i]-1] = 1


for i in range(0, NCM[1]):
    if my_album[special_stickers[i]-1] == 1:
        missing_specials -= 1

print(missing_specials)
