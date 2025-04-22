import random

# Membuat angka acak antara 1 dan 100
def create_number():
    return random.randint(1, 100)    

# Fungsi untuk menebak angka
def get_guess(tebakan, created_number):
    if tebakan < created_number:
        return "Tebakanmu terlalu rendah!"
    elif tebakan > created_number:
        return "Tebakanmu terlalu tinggi!"
    else:
        return "Selamat! Kamu berhasil menebak angka!"