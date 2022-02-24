Rumus = 'F = m * a'

class HUKUMNewtonII:
    def menu (self):
        menu = """
        >>>>menu Hukum Newton 
        Hello, saya Priskila Ayunda. Selamat datang di kelas saya. Saya akan membantu menyelesaikan soal Hukum Newton II. Ayo pilih menu (angka) yaaaa
        1. Menghitung Gaya
        2. Menghitung Percepatan
        3. Menghitung Massa Benda
        4. KELUAR
        """
        return menu

    def Menghitung_Gaya (self, massabenda,percepatan):
        hasil = int(massabenda)*(percepatan)
        return hasil

    def Menghitung_Percepatan (self, massabenda,gaya):
        hasil = int(gaya)/int (massabenda)
        return hasil

    def Menghitung_MassaBenda (self, gaya, percepatan):
        hasil = int(gaya)/int (percepatan)
        return hasil
        
while True:
    print (HUKUMNewtonII().menu())
    pilih = input ('Saya memilih nomor :...')

    if pilih =='1':
        print ('Baik, saya akan Menghitung Gaya yang terjadi dengan mengunakan Hukum Newton II')
        while True:
            orang = input('Masukan dulu nama orangnya atau nama benda: ')
            massabenda = input('Masukan dulu massa bendanya, satuannya menggunakan (Kg)= ')
            percepatan = input('Masukkan nilai percepatannya dulu= ')
            hitung = HUKUMNewtonII().Menghitung_Gaya(massabenda,percepatan)
            Hasil_Gaya = f'besar gaya yang diperlukan {orang} untuk memindahkan sebuah batu dengan massa benda {massabenda} Kg dengan percepatan meter/sekon^2 adalah sebesar {hitung} N'
            print (Hasil_Gaya)
            print('{1} lagi atau {2} atau {3}')
            pilih2 = input('Saya memilih nomor :...')
            if pilih2 =='1': continue
            else : break

    elif pilih =='2':
        print ('Baik, saya akan Menghitung Percepatannya')
        while True:
            orang = input('Masukan dulu nama orangnya atau nama benda: ')
            massabenda = input('Masukan dulu massa bendanya, satuannya menggunakan (Kg) = ')
            gaya = input('Masukkan nilai gaya = (N) ')
            hitung = HUKUMNewtonII().Menghitung_Percepatan(gaya,massabenda)
            Hasil_Percepatan= f'percepatan dari {orang} yang memiliki massa {massabenda} Kg, yang didorong dengan gaya sebesar {gaya} N adalah {hitung} m/s^2'
            print (Hasil_Percepatan)
            print('{1} lagi atau {2} atau {3}')
            pilih2 = input('Saya memilih nomor :...')
            if pilih2 =='2': continue
            else : break

    elif pilih =='3':
        print ('Baik, saya akan Menghitung Massa benda')
        while True:
            orang = input('Masukan dulu nama orangnya atau nama benda: ')
            gaya = input('Masukan besar gaya yang diberikan = (N) ')
            percepatan = input('Masukkan nilai perceptannya dulu (m/s^2)= ')
            hitung = HUKUMNewtonII().Menghitung_MassaBenda(gaya,percepatan)
            hasil_massabenda = f'massa dari {orang} yang didorong dengan gaya sebesar {gaya} N dengan percepatan {percepatan} m/s^2 adalah {hitung} Kg'
            print (hasil_massabenda)
            print('{1} lagi atau {2} atau {3}')
            pilih2 = input('Saya memilih nomor : ')

            if pilih2 == '3': continue
            else : break 

    elif pilih =='4' :
        print ('Kamu memilih menu KELUAR, Terimakasih')
        while True:
            pilih2 = input('Saya memilih KELUAR')

            if pilih2 == '4': continue
            else : break

    else : break