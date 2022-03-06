import random # untuk ngerandom wordsnya
import time # biar ada delay waktu

print("Selamat datang di permainan Hangman!")
time.sleep(1)
nama = input("Siapa nama kamu? ")
print("Halo " + nama + "! Salam kenal!")
time.sleep(1)

def mainlagi():
    print("\nApakah kamu ingin bermain lagi?")
    while True:
        mainlagi = input("Masukkan 'y' jika mau dan 'n' jika tidak ya: ")
        if mainlagi == 'y':
            main()
            break
        elif mainlagi == 'n':
            print("Terima kasih sudah bermain Hangman!")
            exit()
            break
        else:
            print("Pastikan kamu masukkan huruf yang tepat ya! 'y' jika mau dan 'n' jika tidak")

def gambarhangman():
    if nyawa == 4:
        print("   _____ \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")

    elif nyawa == 3:
        print("   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")

    elif nyawa == 2:
        print("   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")

    elif nyawa == 1:
        print("   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")

    elif nyawa == 0:
        print("   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |    / \ \n"
                "__|__\n")

def main():
    print("\nTema Permainan:")
    print("1. Negara\n2. Makanan\n3. Hewan")
    while True:
        tema = int(input("Kamu ingin bermain dengan tema apa?\nMasukkan angkanya: "))
        if tema == 1:
            print("Mari kita mulai permainan Hangman dengan tema Negara!")
            time.sleep(1)
            kata = ["indonesia", "belanda", "amerika"]
            break;
        elif tema == 2:
            print("Mari kita mulai permainan Hangman dengan tema Makanan!")
            time.sleep(1)
            kata = ["model", "soto", "apel"]
            break;
        elif tema == 3:
            print("Mari kita mulai permainan Hangman dengan tema Hewan!")
            time.sleep(1)
            kata = ["anjing", "kucing", "babi"]
            break;
        else:
            print("Masukkan angka pilihan yang tepat ya!\n")


    alfabet = ('abcdefghijklmnopqrstuvwxyz')
    alfabetketebak = []
    katatebak = random.choice(kata)
    tebakan = False
    global nyawa
    nyawa = 5
    
    while tebakan == False and nyawa > 0:
        print("\nNyawamu sekarang ada " + str(nyawa)+ " ya!")
        inputan = input("Masukkan kata ataupun huruf yang kamu mau: ").lower() 
        time.sleep(1) 
        if len(inputan) == 1:
            if inputan not in alfabet:
                print("Masukin alfabet yang benar yaa!")
            elif inputan in alfabetketebak:
                print("Udah pernah ditebak ituuu")
            elif inputan not in katatebak:
                nyawa -= 1
                gambarhangman()
                print("Maaf sekali, tidak ada kata tersebut di sini :(")
                alfabetketebak.append(inputan)
            elif inputan in katatebak:
                print("Yup! Betul sekali!")
                alfabetketebak.append(inputan)
            else:
                print("Mohon maaf, kamu masih salah :(")

        elif len(inputan) == len(katatebak):
            if inputan == katatebak:
                print("Mantap sekali! Anda benar!")
                tebakan = True
            else:
                nyawa -= 1
                gambarhangman()
                print("Mohon maaf, kamu masih salah :(")

        else:
            nyawa -= 1
            gambarhangman()
            print("Mohon maaf, kamu masih salah :(")
        
        status = ''
        if tebakan == False:
            for letter in katatebak:
                if letter in alfabetketebak:
                    status += letter
                else:
                    status += '_'
            print(status)

        if status == katatebak:
            print("Mantab sekali! Anda benar!")
            tebakan = True
        elif nyawa == 0:
            print("\nKamu sudah kalah :(")
            print("Kata yang tepat adalah: " + katatebak)

    mainlagi()

main()