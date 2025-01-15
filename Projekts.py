# Šis kods aprēķinās cik ilgs laiks ir vajadzīgs lai noskatītos kādu šovu.

# Definīcijas
from datetime import datetime,timedelta
import math
a = 0
b = 0
list=[]


# Input

nosaukums=str(input('Ievadiet šova nosaukumu: '))

sez=int(input('Cik sezonu ir šim šovam? '))

    # Cikls kas saglabā cik episožu ir katrā sezonā.
while a < sez:
    a += 1
    item=int(input(f'Ievadiet episožu sk {a}. sezonā. '))
    list.append(item)

ep = sum(list)

ep_gar={'īsa':20, 'vidēji īsa':40, 'vidēja':40, 'vidēji gara':50, 'gara': 60}

gar=(input('Ievadiet episodes garumu (Īsa (20min), vidēji īsa (30 min), vidēja(40 min), vidēji gara (50 min), gara (60 min)): ').lower())

koef=float(input('Ievadiet atskaņošanas ātruma koeficentu (1x, 1.5x, 2x) '))

time,pauz=map(int,input('Pēc cik ilga skatīšanās laika jūs ņemsiet pauzi(A) un cik ilgi(B)? (Rakstiet formā: A B)').split())

t_day=int(input('Cik min dienā jūs varat skatīties? '))


# Aprēķins.
laiks_bez_pauz=(ep_gar[gar] * koef) * float(ep)    # Aprēķina cik minūtes aizņēms šis šovs.
print(laiks_bez_pauz)

if time == 0:
    kop_laiks=laiks_bez_pauz
else:
    kop_laiks=(laiks_bez_pauz//time) * pauz + laiks_bez_pauz                  # Aprēķina cik būs kopēja pauze.
    b = (laiks_bez_pauz//time) * pauz
    print(kop_laiks, laiks_bez_pauz, b)



stundas=kop_laiks/60                                     # Pārveido kopējās min, uz stundām.
dienas=laiks_bez_pauz/t_day                              # Pārveido no stundām uz dienām.
atlikums=stundas%24                                      # Cik stundas paliek pēc dienām.

#datetime
now=datetime.now()
end_t= now + timedelta (hours=atlikums, days=dienas)

# Izvade.
print(f'Jūs šovu {nosaukums} noskatīsīties {stundas:.0f}h, jeb {dienas:.0f} Dienās, {stundas%24:.0f}h. Jūs šo šovu pabeigsiet skatīties: {end_t}')  # Aprēķina cik ilgs būs kopējais skatīšanās laiks. Ieskaitot pauzes.