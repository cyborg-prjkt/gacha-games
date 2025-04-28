import random
import time
import os

saldo = 0
saldo_bank = 10
gacha_minim = 0

def loading():
    loading = ["|", "/", "-", "\\"]
    for frame in loading:
        clear()
        print(f"🎲 Mengacak hadiah... {frame}")
        time.sleep(0.01)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def back():
    try:
        menu_back = input("back to menu [y/n] : ").lower()
    except ValueError:
        print("Input tidak valid!")
    if menu_back == "y":
        menu()
    elif menu_back == "n":
        exit()
    else:
        clear()
        print("pilihan tidak valid")
        print()
        back()

def menu():
        clear()
        print("----- MENU -----")
        print()
        print("[1] GACHA")
        print("[2] CEK SALDO")
        print("[3] CEK BANK")
        print("[4] ISI SALDO")
        print("[5] TARIK UANG")
        print()
        try:
            pilihan = input("PILIH MENU: ")
        except ValueError:
            print("Input tidak valid! Harus berupa angka.")
        if pilihan == "1":
            gacha()
        elif pilihan == "2":
            cek_saldo()
        elif pilihan == "3":
            cek_bank()
        elif pilihan == "4":
            isi_saldo()
        elif pilihan == "5":
            tarik_uang()
        else:
            clear()
            print("pilihan tidak valid")
            time.sleep(1.5)
            menu()

def gacha():
    clear()
    global saldo,gacha_minim
    if saldo < 1:
        print("saldo anda sudah habis, mohon isi saldo dahulu")
        time.sleep(1.5)
        isi_saldo()
    clear()
    print("----- GACHA ------")
    print()
    print("[0] BACK TO MENU")
    print()
    try:
        pilih_gacha = int(input("masukkan jumlah uang $"))
    except ValueError:
        clear()
        print("Input tidak valid! Harus berupa angka.")
        time.sleep(1.5)
        gacha()
    clear()
    if pilih_gacha == 0:
        clear()
        back()
    elif pilih_gacha > saldo:
        clear()
        print("saldo anda tidak cukup")
        time.sleep(1.5)
        gacha()
    elif pilih_gacha < 10:
        clear()
        print("minimal gacha $10")
        time.sleep(1.5)
        gacha()
    print(f"saldo anda dikurangi untuk gacha sebesar ${pilih_gacha}")
    time.sleep(1.5)
    clear()
    gacha_minim += 1
    if gacha_minim > 12:
        gacha_minim -= 12
    elif gacha_minim in (3, 6, 9, 12):
        hadiah = random.randint(0, 10000)
    else:
        hadiah = random.randint(0, 100000000)
    saldo -= pilih_gacha
    clear()
    for i in range(3):
        loading()
    time.sleep(1.5)
    if hadiah == 0:
        clear
        print("coba lagi, semoga beruntung!")
        back()
    else:
        clear()
        bonus = random.uniform(0.1, 0.10)
        hadiah_bonus = int(hadiah * bonus)
        total = hadiah + hadiah_bonus
        saldo += total
        print(f"selamat! kamu mendapatkan hadiah ${hadiah:,} dengan bonus ${hadiah_bonus:,}")
        back()

def cek_saldo():
    clear()
    print("--- CEK SALDO ---")
    print()
    print(f"SALDO ANDA SAAT INI: ${saldo:,}")
    back()

def cek_bank():
    clear()
    global saldo_bank
    if gacha_minim in (3, 6, 9, 12):
        saldo_bank * 0.1
    print("--- CEK BANK ---")
    print()
    print(f"SALDO BANK ANDA SAAT INI: ${saldo_bank:,}")
    back()

def isi_saldo():
    clear()
    global saldo,saldo_bank
    if saldo > 0:
        print(f"saldo anda masih ada ${saldo:,}")
        print("isi saldo saat sudah habis saja")
        back()
    print("--- ISI SALDO ---")
    print()
    print("[0] BACK TO MENU")
    print()
    try:
        isi = int(input("berapa uang yang mau diisi $"))
    except ValueError:
        clear()
        print("Input tidak valid! Harus berupa angka.")
        time.sleep(1.5)
        isi_saldo()
    if isi == 0:
        clear()
        back()
    elif isi > saldo_bank:
        clear()
        print("saldo bank anda tidak cukup")
        time.sleep(1.5)
        isi_saldo()
    elif isi > 10:
        clear()
        print("batas isi saldo minimal $10")
        time.sleep(1.5)
        isi_saldo()
    clear()
    print("sukses dikirim ke akun anda")
    time.sleep(1.5)
    clear()
    saldo_bank -= isi
    saldo += isi
    print(f"saldo anda saat ini: ${saldo:,}")
    back()

def tarik_uang():
    clear()
    global saldo, saldo_bank
    print("--- TARIK UANG ---")
    print()
    print(f"SALDO ANDA SAAT INI: ${saldo:,}")
    print()
    print("[0] BACK TO MENU")
    print()
    try:
        jumlah_tarik = int(input(f"masukkan jumlah uang yang ingin ditarik $"))
    except ValueError:
        clear()
        print("Input tidak valid! Harus berupa angka.")
        time.sleep(1.5)
        tarik_uang()
    if jumlah_tarik == 0:
        clear()
        back()
    elif jumlah_tarik < 1000:
        clear()
        print("minimal tarik uang $1000")
        time.sleep(1.5)
        tarik_uang()
    elif jumlah_tarik > saldo:
        clear()
        print("saldo anda tidak cukup")
        time.sleep(1.5)
        tarik_uang()
    else:
        clear()
        saldo -= jumlah_tarik
        saldo_bank += jumlah_tarik
        clear()
        print("uang sedang diproses")
        time.sleep(1.5)
        clear()
        print(f"anda telah menarik uang sebesar ${jumlah_tarik:,}")
        print()
        print(f"saldo anda saat ini: ${saldo:,}")
        print(f"saldo bank anda saat ini: ${saldo_bank:,}")
        print()

        back()

if __name__ == "__main__":
    menu()