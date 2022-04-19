def length(x) :
    # Fungsi implementasi dari len()
    count = 0
    for i in x :
        count += 1
    return count

def add_row(matriks) :
    # Fungsi untuk menambah baris pada matriks
    x = 0 # variable untuk kolom
    y = 0 # variable untuk baris

    # Menghitung banyak baris
    for i in matriks :
        y += 1
    # Menghitung banyak kolom
    for i in matriks[0] :
        x += 1
    
    # Membuat matriks baru yang sudah ditambah jumlah barisnya
    new_matriks = [["" for j in range(x)] for i in range(y+1)]

    # Mengisi data yang ada ke dalam matriks baru
    for i in range(y) :
        for j in range(x) :
            new_matriks[i][j] = matriks[i][j]
    
    return new_matriks # mengembalikan matriks baru