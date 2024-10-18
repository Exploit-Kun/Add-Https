import os
from colorama import init, Fore, Style
init()
REQUIRED_MODULES = [ 'colorama']
def add_protocol_to_urls(urls):
    updated_urls = []
    for url in urls:
        # Hapus spasi atau karakter newline di setiap baris
        url = url.strip()
        # Cek apakah URL sudah dimulai dengan "http://" atau "https://"
        if not url.startswith("http://") and not url.startswith("https://"):
            # Jika belum, tambahkan "https://" sebagai default
            url = "https://" + url
        updated_urls.append(url)
    return updated_urls

print(Fore.GREEN + "╭─" + Fore.GREEN + "+ Y4udSec07")
print(Fore.GREEN + "│" + Style.RESET_ALL + "Auto Add Https")
print(Fore.GREEN + "│" + Style.RESET_ALL + "Auto Add Http")
print(Fore.GREEN + "╰─────────────────────────" + Style.RESET_ALL)
if __name__ == "__main__":
    input_file = input(Fore.YELLOW + "Masukkan nama file input: ")
    output_file = input(Fore.YELLOW + "Masukkan nama file output: ")

# Membaca daftar URL dari file input.txt
with open(input_file, 'r', encoding='utf-8') as file:
    list_website = file.readlines()

# Memproses daftar URL untuk menambahkan protokol
updated_list = add_protocol_to_urls(list_website)

# Menyimpan hasil ke file output.txt
with open(output_file, 'w') as file:
    for url in updated_list:
        file.write(url + "\n")

print(f"Proses selesai. URL yang telah diperbarui disimpan di {output_file}.")



