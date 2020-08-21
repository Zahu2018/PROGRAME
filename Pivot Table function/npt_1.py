# NEW PIVOT TABLE v2.0 by Zah Florian at 19.05.2020
#pivot table, #tabel pivotant
# Face un tabel pivotant dint-un tabel pe orizontala
""" EXEMPLU TABEL
1,19,5,2020,23126,33,1414,,,Product_1,Product_2,Product_3,Product_4
1,19,5,2020,23126,33,1414,132,100,26.58,18.7,7.6,1.6
1,19,5,2020,40617,18,1414,,0,Product_1,Product_2,Product_5,Product_6
1,19,5,2020,40617,18,1414,485,120,11.86,7.43,10.56,3.6
1,19,5,2020,40617,18,1414,497,120,11.86,7.43,10.56,3.6
"""
def deschide_fila():
    #file_name = input("Introdu numele fisierului: ")
    file_name = "1.csv"
    with open(file_name, 'r') as fn:
        text = fn.read()
        return text
        
        
def fa_dictionarul(text, prima_coloana=9):
    def fa_lista_linii(text):
        #1. Face o lista de liste de elemente
        initial = 0
        nr_linii = text.count('\n')
        lista = []
        for i in range(nr_linii):
            final = text.find('\n', initial)
            linie = text[initial:final].split(',')
            lista.append(linie)
            initial = final + 1
        return lista
            
    def fa_lista_matrice(lista, pc):  # pc = prima coloana
        #2. Facem o lista de matrice
        lista_matrice = []
        matricea = []
        for item in lista:
            if str(item[pc]).isupper():
                if matricea != []:
                    lista_matrice.append(matricea)
                else:
                    pass
                matricea = []
                matricea.append(item)
            else:
                matricea.append(item)
        #matricea.append(item) # !!! TREBUIE INDEPARTAT !!!
        lista_matrice.append(matricea)
        return lista_matrice
        
    def fa_dictionar(lista_matrice):
        #3. Facem un dictionar
        dicti = {}
        for mat in lista_matrice:
            for item in mat[0]:
                if item.isnumeric() == False:
                    index = mat[0].index(item)
                    inaltime = len(mat) # inaltimea matricei
                    for i in range(1, inaltime):
                        suma = 0
                        suma_i = 0
                        m = mat[i][index]
                        try:
                            valoare = float(m)
                            suma += valoare
                            suma_i += suma
                            if item in dicti:
                                var = round(float(dicti.get(item)),2)
                                suma_i += var
                                dicti[item] = "{:.2f}".format(suma_i) # {:.2f}
                            else:
                                dicti[item] = "{:.2f}".format(suma_i) # {:.2f}
                        except:
                            print('Nu pot converti in float = {}, rand = {}'.format(item, i))
        if '' in dicti.keys():
            dicti.pop('')
        return dicti
        
    
    lista_linii = fa_lista_linii(text)
    lista_matrice = fa_lista_matrice(lista_linii, prima_coloana)
    dicti = fa_dictionar(lista_matrice)
    return dicti
    
    
    
    
def main():
    text_fila = deschide_fila()    # return text
    #print(text_fila)
    dic = fa_dictionarul(text_fila)  # return dict
    for k,v in dic.items():
        print("{} = {}".format(k, v))
main()