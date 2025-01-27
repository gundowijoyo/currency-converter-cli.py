import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    
    if "rates" in data:
        rate = data["rates"].get(to_currency)
        if rate:
            converted_amount = amount * rate
            print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            print(f"Tidak ada data nilai tukar untuk {to_currency}.")
    else:
        print("Gagal mendapatkan data nilai tukar.")

def main():
    print("Masukkan jumlah uang yang ingin dikonversi:")
    amount = float(input())
    print("Masukkan mata uang asal (contoh: USD):")
    from_currency = input().upper()
    print("Masukkan mata uang tujuan (contoh: EUR):")
    to_currency = input().upper()
    
    convert_currency(amount, from_currency, to_currency)

if __name__ == "__main__":
    main()
  
