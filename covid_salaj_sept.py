
text = '''
ZALAU 69087 103
CEHU SILVANIEI 7519 1
JIBOU 11697 1
SIMLEU SILVANIEI 17305 15
AGRIJ 1420 0
ALMASU 1961 0
BABENI 1554 0
BALAN 3732 4
BANISOR 1914 2
BENESAT 1415 0
BOBOTA 3891 4
BOCSA 3376 1
BOGHIS 1942 5
BUCIUMI 2544 0
CAMAR 1642 1
CARASTELEC 1037 0
CHIESD 2547 1
CIZER 2210 0
COSEIU 1141 0
CRASNA 6701 5
CREACA 2773 1
CRISENI 3285 3
CRISTOLT 1175 0
CUZAPLAC 1600 0
DOBRIN 1645 0
DRAGU 1421 0
FILDU DE JOS 1345 0
GALGAU 2342 1
GARBOU 2022 1
HALMASD 2354 0
HERECLEAN 3922 1
HIDA 2619 1
HOROATU CRASNEI 2539 0
ILEANDA 2411 2
IP 3706 1
LETCA 1695 0
LOZNA 918 0
MAERISTE 2871 1
MARCA 2589 1
MESESENII DE JOS 3117 0
MIRSID 2411 1
NAPRADEA 2664 1
NUSFALAU 3964 5
PERICEI 3758 2
PLOPIS 2526 0
POIANA BLENCHII 1159 0
ROMANASI 3216 2
RUS 1003 0
SAG 3256 0
SALATIG 2628 2
SAMSUD 1866 0
SANMIHAIU ALMASULUI 1679 2
SARMASAG 6586 2
SIMISNA 1141 0
SOMES ODORHEI 2764 1
SURDUC 3680 1
TREZNEA 1049 1
VALCAU DE JOS 3150 3
VARSOLT 2251 1
ZALHA 815 0
ZIMBOR 975 0
TOTAL  243525 180'''

lista = []
l = text.split('\n')
for i in l:
    if i == '' or "TOTAL" in i:
        continue
    else:
        l = []
        _ = i.split(' ')
        
        loc = ' '.join(_[:-2])
        pop = _[-2]
        imb = _[-1]
        x = f'{loc},{pop},{imb}'
        l.append(x)
        lista.append(l)


with open('rezultat.csv', 'w') as f:
    f.write("Localitatea, Populatie, Nr. imbolnaviri\n")
    for i in sorted(lista):
        j = str(i).replace('[', '').replace(']', '\n').replace("'", '')
        f.write(j)
