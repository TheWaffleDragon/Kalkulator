import logging as log

#log.basicConfig(level=log.INFO)

#Dodawanie
def add(x,y):
    return (x + y)

#odejmowanie
def sub(x,y):
    return x - y

#mnozenie
def mul(x,y):
    return x * y

#dzielenie
def div(x,y):
    return x / y
wynik = 0

while True:
    dzialanie = input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ')
    
    if dzialanie in ('1', '2', '3', '4'):
        x = float(input('Podaj składnik 1: '))
        y = float(input('Podaj składnik 2: '))
        if dzialanie == '1':
            wynik = add(x,y)
            log.info(f"Dodaję {x} i {y}")
            break
            
        elif dzialanie == '2':
            wynik = sub(x, y)
            log.info(f"Odejmuję {y} od {x}")
            break
        
        elif dzialanie == '3':
            wynik = mul(x, y)
            log.info(f"Mnożę {x} i {y}")
            break
        
        elif dzialanie == '4':
            wynik = div(x, y)
            log.info(f"Dzielę {x} przez {y}")
            break
            


print(f"Wynik to {wynik}")    