#awal = C
#tujuan = J
#jalur

peta1 =  {'A':set(['B']),
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

def bfs(graf, mulai, tujuan):
    queue = [[mulai]]
    visited = set()

    while queue:     
        # masukkan antrian paling depan ke variabel jalur
        jalur = queue.pop(0)
        print("\n --------------------- \n")
        print("jalur = ", jalur)
        print("queue = ", queue)

        # simpan node yang dipilih ke variabel state, misal jalur = C,B maka simpan B ke variabel state
        state = jalur[-1]
        print("state = ", state)

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
                    queue.append(jalur_baru) #update/tambah queue dengan jalur_baru

            # tandai state yang sudah dikunjungi sebagai visited
            print("queue = ", queue)
            visited.add(state)
            print("visited = ", visited)

        #cek isi antrian
        isi = len(queue)
        print("isi = ",isi)
        if isi == 0:
            print("Tidak ditemukan")

print("HASIL = ",bfs(peta1,'C','J'))
print("\n peta = ",peta1)
