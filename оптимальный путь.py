from math import tan, cos, sqrt, acos, radians
from matplotlib import pyplot as plt

# Параметры
a = int(input('Введите A:\n'))
c = int(input('Введите C:\n'))
b = int(input('Введите B:\n'))

s = 1
d = 10

# Построим график

x = [0,0]
y = [0,a]

x1 = [c,c]
y1 = [b,0]

x2 = [0,c]
y2 = [0,0]

x3 = [0,c]
y3 = [a,b]

# plt.plot([0,0,c,c,0,c],[0,a,b,0,0,0],color='g')

plt.plot(x,y,color='g')
plt.plot(x1,y1,color='purple')
plt.plot(x2,y2,color='b')
plt.plot(x3,y3,color='red')


plt.title("Поиск наиболее дешевого пути")
plt.ylabel('Y')
plt.xlabel('X')
plt.show()

# Найдем длину канала
kanal = sqrt(c**2-((b-a)**2))

max_gip_a = sqrt(a**2+kanal**2)
max_gip_b = sqrt(b**2+kanal**2)

max_ugol_a = round(acos(a/max_gip_a)*(180/3.14),2)
max_ugol_b = round(acos(b/max_gip_b)*(180/3.14),2)

ugol_a = 0
ugol_b = 0
summa = 10000
list_a = []
while ugol_a <= max_ugol_a:
    katet_a = a * tan(radians(ugol_a))
    if katet_a <= kanal:
        gipotenuza_a = a/cos(radians(ugol_a))
        ugol_b = 0
        while ugol_b <= max_ugol_b:
            katet_b = (b * tan(radians(ugol_b)))
            if katet_b <= kanal and katet_b>=0:
                gipotenuza_b = sqrt(katet_b**2+b**2)
                kanal_ab = kanal - (katet_a + katet_b)
                if kanal_ab>=0:
                    summ_new = gipotenuza_a+kanal_ab*(1/d)+gipotenuza_b
                    if summ_new <= summa:
                        summa = summ_new
                        katet_itog_a = katet_a
                        katet_itog_b = katet_b
                        kanal_itog_ab = kanal_ab
                else:
                    pass
            else:
                pass
            ugol_b +=5
    ugol_a+=5

itog = 0
if summa <= c:
    itog = summa
    print('Наименьшая стоимость перевозки груза будет по каналу:', itog)
else:
    itog = c
    print('Наименьшая стоимость перевозки груза будет по дороге:', itog)

# Построим график
if summa < c:

    x = [katet_itog_a, 0]
    y = [0, a]

    x21 = kanal - kanal_itog_ab
    x22 = kanal_itog_ab + katet_itog_a
    x1 = [c, x22]
    y1 = [b, 0]

    x2 = [katet_itog_a, x22]
    y2 = [0, 0]

    x3 = [0, c]
    y3 = [a, b]

    # Если по каналу дешевле, то часть по каналу зеленым цветом, а по дороге красным и наоборот
    plt.plot(x, y, color='g')
    plt.plot([0, 0,30,0,60,0,100,0], [0,a,0,a,0,a,0,a], color='m')
    plt.plot([c, c, c-30, c, c-70, c, c-100, c,], [0, b, 0, b, 0, b, 0, b], color='m')
    plt.plot(x1, y1, color='g')
    plt.plot(x2, y2, color='g')
    plt.plot(x3, y3, color='red')

    plt.title("Наилучший путь :")
    plt.show()

elif summa > c:
    plt.plot(x, y, color='r')
    plt.plot([10, 0, 30, 0, 60, 0, 100, 0], [0, a, 0, a, 0, a, 0, a], color='b')
    plt.plot([c, c, c-30, c, c-70, c, c-100, c], [0, b, 0, b, 0, b, 0, b], color='m')
    plt.plot(x1, y1, color='r')
    plt.plot(x2, y2, color='r')
    plt.plot(x3, y3, color='green')

    plt.title("Наилучший путь :")
    plt.show()



