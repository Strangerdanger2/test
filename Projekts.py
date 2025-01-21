import math

def ievaddati():
    nosaukums = str(input('Ievadiet šova nosaukumu: '))
    sez = int(input('Cik sezonu ir šim šovam? '))
    return nosaukums, sez

def ievadi_ep_skaitu(sez):
    epizodes_skaits = []
    for a in range(1, sez + 1):
        item = int(input(f'Ievadiet epizožu sk {a}. sezonā. '))
        epizodes_skaits.append(item)
    return epizodes_skaits

def ievadi_papildus_datus():
    ep_gar_dic = {'īsa': 20, 'vidēji īsa': 30, 'vidēja': 40, 'vidēji gara': 50, 'gara': 60}
    ep_lenght = input('Ievadiet epizodes garumu (Īsa (20min), vidēji īsa (30 min), vidēja(40 min), vidēji gara (50 min),'
                      'gara (60 min)): ').lower()
    watch_min = int(input('Cik min dienā jūs varat skatīties? '))
    koef = float(input('Ievadiet skatīšanās laika koef (x0.5, x1, x1.5, x2) '))
    return ep_gar_dic, ep_lenght, watch_min, koef

def aprekins(ep, ep_gar_dic, ep_lenght, watch_min, koef):
    total_time_min = (ep * ep_gar_dic[ep_lenght]) // koef
    diena = total_time_min // watch_min
    leftover_min = int(total_time_min - (diena * watch_min))
    reserve_h = leftover_min // 60
    min = leftover_min % 60
    return total_time_min, diena, leftover_min, reserve_h, min

def izvade(nosaukums, total_time_min, diena, leftover_min, reserve_h, min):
    print(f'Šovs {nosaukums}, kopā aizņems: {total_time_min:.0f} min, '
          f'{diena:.0f} Dienas, atlikušās min: {leftover_min:.0f}, '
          f'{reserve_h:.0f} pilnas stundas, {min:.0f} min.')

# Galvenā programma
def main():
    nosaukums, sez = ievaddati()
    epizodes_skaits = ievadi_ep_skaitu(sez)
    ep = sum(epizodes_skaits)
    ep_gar_dic, ep_lenght, watch_min, koef = ievadi_papildus_datus()
    total_time_min, diena, leftover_min, reserve_h, min = aprekins(ep, ep_gar_dic, ep_lenght, watch_min, koef)
    izvade(nosaukums, total_time_min, diena, leftover_min, reserve_h, min)

if __name__ == "__main__":
    main()