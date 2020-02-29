import datetime
import requests
#python -m pip install request
#> Path\easy_install.exe
r = requests.get("https://api.recursospython.com/dollar")
resul = r.json()
print("Comprar: ", resul["buy_price"])
print("Vender: ", resul["sale_price"])

horaActual = datetime.datetime.now()
print(horaActual)