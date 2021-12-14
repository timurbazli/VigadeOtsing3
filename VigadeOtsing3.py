from random import *

def arvud_loendis():
    """Компьютерные списки
    """
    s=[]
    pos=[]
    neg=[]
    null=[]
    neg=[]
    kesk=[]
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
        mini,maxi=vahetus(mini,maxi)
    generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    jagamine(s,pos,neg,null)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",null)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    print(s)

def vahetus(a:int,b:int):
    """kui min suurem kui max, siis vahetame neid omavahel
    :param int a: minimaalne arv, mis on suurem kui max
    :param int b: maximaalne arv, mis on väiksem kui min 
    :rtype int,int:
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """Генерирует рандомные, целые числа.
    :param int a: числа-ограничители (a-это минимальное число)
    :param int b: числа-ограничители (b-это максимальное число)
    :rtype int,int:
    """
    for i in range(n):
        loend.append(randint(a,b))
    

def jagamine(loend:list,p:list,n:list,null:list):
    """
    :param list loend: 
    :param list p:
    :param list n: общее кол-во чисел
    :param list null:
    :rtype: list
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            null.append(el)

def keskmine(loend:list):
    """Находит кол-во положительных элементов.

    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend:list,el:float):
    """Добавляет элемент, сортирует список
    :rtype: float
    """
    loend.append(el)
    loend.sort()

arvud_loendis()