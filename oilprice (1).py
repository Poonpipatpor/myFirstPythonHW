import json
import xmltodict
from suds.client import Client
price_oil = {"Gasoline 95": 29.16,
             "Gasoline 91": 25.30,
             "Gasohol 91": 21.68,
             "Gasohol E20": 20.2,
             "Gasohol 95": 21.2,
             "Diesel": 21.2}

client = Client('https://www.pttor.com/OilPrice.asmx?WSDL')
OilPrice = client.service.CurrentOilPrice(Language='thai')

OilPrice1 = xmltodict.parse(OilPrice)  # ได้ผลลัพธ์เป็น json ในสตริง
Price = eval(json.dumps(OilPrice1))  # เรียกใช้งาน json ในสตริง
print(Price)

for i in Price["PTTOR_DS"]["FUEL"]:
    if ("PRICE" in i):
        price_oil[i["PRODUCT"]] = float(i["PRICE"])


while True:
    print("#"*80)
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*25 + "Welcome" + " "*25 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")

    print("#"*80)

    print("#"*80)
    print("###########" + " "*25 + "price oil" + " "*23 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("#"*11 + " "*8 + "1.Gasoline 95 ราคา " +
          '%.2f' % (price_oil["Gasoline 95"]) + " BATH" + " "*20+"#"*12)
    print("#"*11 + " "*8 + "2.Gasoline 91 ราคา " +
          '%.2f' % (price_oil["Gasoline 91"]) + " BATH" + " "*20+"#"*12)
    print("#"*11 + " "*8 + "3.Gasohol 91  ราคา " +
          '%.2f' % (price_oil["Gasohol 91"]) + " BATH" + " "*20+"#"*12)
    print("#"*11 + " "*8 + "4.GasoholE20  ราคา " +
          '%.2f' % (price_oil["Gasohol E20"]) + " BATH" + " "*20+"#"*12)
    print("#"*11 + " "*8 + "5.Gasohol 95  ราคา " +
          '%.2f' % (price_oil["Gasohol 95"]) + " BATH" + " "*20+"#"*12)
    print("#"*11 + " "*8 + "6.Diesel ราคา " +
          '%.2f' % (price_oil["Diesel"]) + " BATH" + " "*25+"#"*12)
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("#"*80)

    f = int(input("which type of fuel do you want?"))

    print("#"*80)
    print("###########" + " "*25 + "price oil" + " "*23 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("#"*11 + " "*8 + " "*10 + "1.คำนวณเงินเป็นลิตร" + " "*23 + "#"*12)
    print("#"*11 + " "*8 + " "*10 + "2.คำนวณลิตรเป็นเงิน" + " "*23 + "#"*12)
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("#"*80)

    c = int(input())

    p = float(input())

    if (f == 1):
        if c == 1:
            total = p / price_oil["Gasoline 95"]
        elif c == 2:
            total = p * price_oil["Gasoline 95"]
    elif (f == 2):
        if c == 1:
            total = p / price_oil["Gasoline 91"]
        elif c == 2:
            total = p * price_oil["Gasoline 91"]
    elif (f == 3):
        if c == 1:
            total = p / price_oil["Gasohol 91"]
        elif c == 2:
            total = p * price_oil["Gasohol 91"]
    elif (f == 4):
        if c == 1:
            total = p / price_oil["Gasohol E20"]
        elif c == 2:
            total = p * price_oil["Gasohol E20"]
    elif (f == 5):
        if c == 1:
            total = p / price_oil["Gasohol 95"]
        elif c == 2:
            total = p * price_oil["Gasohol 95"]
    elif (f == 6):
        if c == 1:
            total = p / price_oil["Diesel"]
        elif c == 2:
            total = p * price_oil["Diesel"]

    print(total)
    input_exit = input()
    if (input_exit == "exit"):
        break
