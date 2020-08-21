# CREAZA O PAGINA HTML CU UN TABEL CU DATE
# PROVENITE DINTR-UN FISIER CSV

import csv         # to read csv file
import webbrowser  # to open html created

inceput = """<html>
<body>
    <table style="border: 1px solid black">\n"""
sfarsit = """</table>
    </body>
</html>"""   


def creaza_html(csv_reader):
    # CREAZA COD TABEL HTML
    tabel = ""
    line_count = 0
    for row in csv_reader:
        # prima linie deosebita de celelalte
        if line_count == 0:
            s1 = ""
            for item in row:
                s1 = s1 + f'<td>{item}</td>'
            row_html = f'<tr style="background-color:#8cb3d9">{s1}</tr>\n'
            tabel = tabel + row_html
            line_count += 1
        else:
            s1 = ""
            for item in row:
                s1 = s1 + f'<td title="...alt">{item}</td>'
            row_html = f'<tr style="background-color:#f0f2f4">{s1}</tr>\n'
            tabel = tabel + row_html
            line_count += 1
    return tabel


def citeste_csv(fila_csv):
    # CITESTE FISIERUL CSV
    with open(fila_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        tabel = creaza_html(csv_reader)
        return tabel


mijloc = citeste_csv("data.csv")  # mijloc = tabel
text_tabel = inceput + mijloc + sfarsit
print(text_tabel)
with open("data.html", "w") as f:
    f.write(text_tabel)
    
# SA DESCHIDA AUTOMAT FISIERUL HTML DUPA CA A FOST CREAT
url = 'data.html'
webbrowser.open(url, new=2)  # open in new tab
