#CSV Parser (Manual)

def len(a):
  n=0
  for i in a:
    if i!="NaN":
      n+=1
  return n

#SPLIT BARIS DENGAN DELIMETER ";"
def split(baris):
    #hitung jumlah ";" pada baris
    jumlah=0
    for i in range(len(baris)):
        if baris[i] == ";":
            jumlah += 1

    # convert string sebelum ';' menjadi elemen array
    n=0  #indeks array
    array = [0 for i in range (jumlah+1)]
    deli = 0
    for i in range(len(baris)):
        if baris[i] == ";":
            array[n] = baris[deli:i]
            deli = i + 1
            n += 1
    #menambahkan sisa string setelah delimeter terakhir ke array
    array[n] = baris[deli:]
    return array


def openCSV(namaFile, k, bar="NaN", kol="NaN"):
    # membuka data file eksternal berupa csv
    file = open(r"{}".format(namaFile), k, encoding="utf8")
    files = file.readlines()
    file.close()  

    #convet file ke dalam sebuah array
    n =0 
    array = [0 for i in range (len(files))]
    for baris in files:
        baris = split(baris)
        array[n] = baris
        n = n+1
    # output data sesuai permintaan
    if bar == "NaN" and kol == "NaN":
        return array
    elif kol == "NaN":
        return array[bar]
    else:
        return array[bar][kol]
