#contoh peta 
peta =  {'A':set(['B']),
         'B':set(['C','E','A']),
         'C':set(['D','F','E']),
         'D':set(['C']),
         'E':set(['C','G','B']),
         'F':set(['C','H','K']),
         'G':set(['E','H']),
         'H':set(['F','I']),
         'I':set(['H','J']),
         'J':set(['I']),
         'K':set(['F'])}
   

def dfs(graf, mulai, tujuan):
    stack = [[mulai]]
    visited = set()

    while stack:
        #hitung panjang tumpukan dan masukkan ke variabel panjang_tumpukan
        panjang_tumpukan = len(stack)-1
        
        # masukkan tumpukan palinif state == tujuan:g atas ke variabel jalur
        jalur = stack.pop(panjang_tumpukan)
        print("\n --------------------- \n")
        print("panjang tumpukan = ", panjang_tumpukan)
        print("jalur = ", jalur)
        print("stack = ", stack)

        # simpan node yang dipilih ke variabel state, misal jalur = C,B maka simpan B ke variabel state
        state = jalur[-1]
        print ("state = ", state)

        # cek state apakah sama dengan tujuan, jika ya maka return jalur
        if state == tujuan:
            return jalur
        # jika state tidak sama dengan tujuan, maka cek apakah state tidak ada di visited
        elif state not in visited:
            # jika state tidak ada di visited maka cek cabang
            for cabang in graf.get(state, []): #cek semua cabang dari state
                if cabang not in visited:
                    jalur_baru = list(jalur) #masukkan isi dari variabel jalur ke variabel jalur_baru
                    jalur_baru.append(cabang) #update/tambah isi jalur_baru dengan cabang
                    stack.append(jalur_baru) #update/tambah queue dengan jalur_baru

            # tandai state yang sudah dikunjungi sebagai visited
            print("stack = ", stack)
            visited.add(state)
            print("visited = ", visited)


        #cek isi tumpukan
        isi = len(stack)
        print("isi = ", isi)
        if isi == 0:
            print("Tidak ditemukan")

print("HASIL = ",dfs(peta,'C','J'))
print("\n peta = ",peta)
