# Programma kas aprekina cik ilgs laiks ir nepieciesams lai noskatitos kadu sovu

import math
a = 0
list = []

# Ievaddati

nosaukums=str(input('Ievadiet šova nosaukumu: '))
sez=int(input('Cik sezonu ir šim šovam? '))

# Cikls kas saglabā cik episožu ir katrā sezonā.
while a < sez:
    a += 1
    item=int(input(f'Ievadiet episožu sk {a}. sezonā. '))
    list.append(item)

ep = sum(list)
ep_gar_dic={'īsa':20, 'vidēji īsa':30, 'vidēja':40, 'vidēji gara':50, 'gara': 60}
ep_lenght=(input('Ievadiet episodes garumu (Īsa (20min), vidēji īsa (30 min), vidēja(40 min), vidēji gara (50 min), gara (60 min)): ').lower())
watch_min=int(input('Cik min dienā jūs varat skatīties? '))
koef=float(input('Ievadiet skatīšanās laika koef (x0.5, x1, x1.5, x2) '))

# Aprēķins

# Cik min skatīsies. Man vajag iziet cauri sezonam un iznemt epizodes lai es varetu aprekinat laiku.
total_time_min = (ep * ep_gar_dic[ep_lenght]) // koef        #Aprēķina cik min paies lai noskatitos visu sovu, ar koeficentu
diena = total_time_min // watch_min                          #Cik dienas skatīsies
leftover_min = (total_time_min - (diena * watch_min))        #Cik minutēs palika kuras nevarēja pārveidot uz pilnām dienām
reserve_h = leftover_min // 60                               #Atlikušās stundas no rezerves min
min = leftover_min % 60                                      #Atlikušās min, pēc stundas aprēķina
    

# Izvade
print(f'Jūs šovu {nosaukums}, skatīsieties: Kopējās min {total_time_min:.0f}, Cik dienas tas aizņems {diena:.0f}, palikušās min {leftover_min:.0f}, Cik pilnu stundu palika {reserve_h:.0f}, cik min palika {min:.0f}')