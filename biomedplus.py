import pyautogui as pyg
import time
import keyboard
import random
from pyautogui import *

time.sleep(0.05)
PP = 0
PA = 0
w = 100  # ilość powtórzeń

x = ["Nie lepiej kupic Polyslash? https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=POLYSLASH ", "https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=POLYSLASH", "Gdzie tu inwestowac Polyslash?, https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=POLYSLASH", "Czemu nie, https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=POLYSLASH", "Sprawdz to, https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=POLYSLASH ", "Polyslash"]
y = ["Juz 25 marca premiera nowej gry Mech Mechanik", "tylko 1mln akcji w wolnym obiegu, obecna cena 13zł, tu moze byc drugi CreepyJar"]
z = "Co ja bede wam tlumaczyla, po wiecej informacji wejdz na forum"
zz = "Pozdrawiam "


aut = "Earth_Angel"
zzt = [aut, "Obserwatorka", "Alexa", "Agnieszka", "Anna", "Maria", "Katarzyna", "Malgorzata", "Barbara", "Ewa", "Krystyna", "Honey"]
tem = ["A moze Polyslash? Nowy typ od ",
       "Zarobek 1000%? Typ od ",
       "Nowy typ od ",
       "A moze Polyslash? Jestem ",
       "Lubie Polyslash. ",
       "Ale numer Polyslash od ",
       "Polyslash? Polecam "]

while w > 0:
    klik = 4
    dd = random.randint(0, 11)
    bb = random.randint(1, 8)
    ba = random.randint(1, 8)
    kod = ''.join(random.sample(
        'qwer tyuiopa sdf ghjk lzxc vbnm,.QWE RTY UIOP ASDF GHJK LZX VBNM ABC DEFG HIJKLM NOPRST UWXYZqw erty uiopa sddfg hjklzxc vb nm.123456 7890,;',
        100 + bb))
    aa = ''.join(random.sample('!!!!1!1!!', bb))
    cc = ''.join(random.sample('........', bb))
    ca = ''.join(random.sample('........', ba))
    pyg.click(10, 500)
    pyg.press('pagedown')
    time.sleep(0.1)
    a = (pyg.locateOnScreen('zobacz.png', confidence=0.5))[0]
    b = (pyg.locateOnScreen('zobacz.png', confidence=0.5))[1]
    pyg.click(a+10, b+10)
    time.sleep(2)
    w -= 1

# wersja z nowym wątkiem
# ------------------------------------------------------------------------<
    if pyg.locateOnScreen('dodaj.png', confidence=0.8) is not None:

        a1 = (pyg.locateOnScreen('dodaj.png', confidence=0.8))[0]
        b1 = (pyg.locateOnScreen('dodaj.png', confidence=0.8))[1]
        pyg.click(a1 + 10, b1 + 10)
# ------------------------------------------------------------------------>

# wersja z odpowiedzią
# ---------------------------------------------------<
#    while klik > 0:
#
#        pyg.click(578, 731 + (klik*2))
#        klik -= 1
#        time.sleep(0.1)
#
#    time.sleep(2)
#
#    if pyg.locateOnScreen('Odpowiedz.png', confidence=0.8) is not None:
#
#        a2 = (pyg.locateOnScreen('Odpowiedz.png', confidence=0.8))[0]
#        b2 = (pyg.locateOnScreen('Odpowiedz.png', confidence=0.8))[1]
#
#        pyg.click(a2 + 10, b2 + 10)
#
#    else:
#
#        pyg.press('down')
#
#       if pyg.locateOnScreen('Odpowiedz.png', confidence=0.8) is not None:
#
#            a2 = (pyg.locateOnScreen('Odpowiedz.png', confidence=0.8))[0]
#            b2 = (pyg.locateOnScreen('Odpowiedz.png', confidence=0.8))[1]
#
#            pyg.click(a2 + 10, b2 + 10)
# --------------------------------------------------->

    time.sleep(2)
    pyg.write(x[random.randint(0, 5)] + ca, interval=0.01)
    pyg.press('enter')
    pyg.write(y[random.randint(0, 1)], interval=0.01)
    pyg.press('enter')
    pyg.write(z + cc, interval=0.01)
    pyg.press('enter')
    pyg.write(zz + zzt[dd] + cc, interval=0.01)
    pyg.press('enter')
    pyg.press('enter')
    pyg.press('enter')
    pyg.press('enter')
    pyg.write('Kod weryfikacyjny: ' + kod + cc, interval=0.01)
    time.sleep(1)
    pyg.click(635, 362)
    pyg.write(zzt[dd], interval=0.1)
    pyg.press('tab')
    pyg.write(tem[PP]+zzt[dd]+aa, interval=0.1)
    PP += 1

    if PP > 6:
        PP = 0

    if PA == 40:
        PA = 0

 #   if pyg.locateOnScreen('wyslij.png', confidence=0.8) is not None:
 #       a2 = (pyg.locateOnScreen('wyslij.png', confidence=0.8))[0]
 #       b2 = (pyg.locateOnScreen('wyslij.png', confidence=0.8))[1]

 #       pyg.click(a2 + 10 + PA, b2 + 10 + PA)
        PA += 2
#    pyg.click(750, 980)
    time.sleep(4)

    if pyg.locateOnScreen('Przejdz.png', confidence=0.8) is not None:
        a2 = (pyg.locateOnScreen('Przejdz.png', confidence=0.8))[0]
        b2 = (pyg.locateOnScreen('Przejdz.png', confidence=0.8))[1]

        pyg.click(a2 + 10, b2 + 10)
        PA += 2
    pyg.hotkey('ctrl', 'tab')
    time.sleep(10)
