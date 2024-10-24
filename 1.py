import random
SC=random.randint(1000,9999)
while len(str(SC))!=len(set(str(SC))):
    SC = random.randint(1000, 9999)
ch1=str(SC)
ch2=""
kv=0
while ch1!=ch2:
    kv+=1
    print("Введите код:")
    ch2 = str(input())
    while (ch2.count("0") + ch2.count("1") + ch2.count("2") + ch2.count("3")
           + ch2.count("4") + ch2.count("5") + ch2.count("6") + ch2.count("7")
           + ch2.count("8") + ch2.count("9") + ch2.count("0") != 4 or ch2[0] == 0):
        ch2 = str(input())
        print("Ошибка! Введите черырехзначное число:")
    bull = 0
    cow = 0
    if ch2[0] in ch1:
        if ch1[0] == ch2[0]:
            bull+=1
        else:
            cow+=1
    if ch2[1] in ch1:
        if ch1[1] == ch2[1]:
            bull += 1
        else:
            cow += 1
    if ch2[2] in ch1:
        if ch1[2] == ch2[2]:
            bull+=1
        else:
            cow+=1
    if ch2[3] in ch1:
        if ch1[3] == ch2[3]:
            bull += 1
        else:
            cow += 1
    print("Ход:",kv)
    print("Быки:",bull,"Коровы:",cow)
print("Отгадал!")
print("Секретный код:",SC,"Количество ходов:",kv)