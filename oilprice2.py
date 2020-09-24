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

for i in Price["PTTOR_DS"]["น้ำมัน"]:
    if ("ราคา" in i):
        price_oil[i["ผลิตภัณท์"]] = float(i["ราคา"])


while True :
    print("#"*80)
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " " * 34 + "Welcome"+" " * 35 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("#"*80)
    print("#"*80)
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " " * 34 + "ราคาน้ำมัน" + " " * 34 + "##")
    print("##" + " " * 25 + "1.Gasoline 95 ราคา 29.19 บาท" + " " * 23 + "##")
    print("##" + " " * 25 + "2.Gasoline 91 ราคา 25.31 บาท" + " " * 23 + "##")
    print("##" + " " * 25 + "3.Gasohol 91  ราคา 21.68 บาท" + " " * 23 + "##")
    print("##" + " " * 25 + "4.Gasohol E20 ราคา 20.2  บาท" + " " * 23 + "##")
    print("##" + " " * 25 + "5.Gasohol 95  ราคา 21.2  บาท" + " " * 23 + "##")
    print("##" + " " * 25 + "6.Diesel      ราคา 21.1  บาท" + " " * 23 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("#"*80)

    o = int(input())

    # 1.เงินเป็นลิตร
    # 2.ลิตรเป็นเงิน

    print("#"*80)
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*25 +         "คำนวณ" + " " * 46 + "##")
    print("##" + " " * 25 + "1.เงินเป็นลิตร" + " " * 40 + "##")
    print("##" + " " * 25 + "1.ลิตรเป็นเงิน" + " " * 40 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("#"*80)

    s = int(input())

    print("#"*80)
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*34 + "กรอกจำนวนลิตร/เงิน" + " "*26 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("#"*80)

    p = int(input())

    if (o == 1):
        if(s == 1):
            total = p / 29.19
        elif(s == 2):
            total = p * 29.19
    elif (o == 2):
        if(s == 1):
            total = p / 25.31
        elif(s == 2):
            total = p * 25.31
    elif (o == 3):
        if(s == 1):
            total = p / 21.68
        elif(s == 2):
            total = p * 21.68
    elif (o == 4):
        if(s == 1):
            total = p / 20.2
        elif(s == 2):
            total = p * 20.2
    elif (o == 5):
        if(s == 1):
            total = p / 21.2
        elif(s == 2):
            total = p * 21.2
    elif (o == 6):
        if(s == 1):
            total = p / 21.1
        elif(s == 2):
            total = p * 21.1

    print(total)
    input()
    print("#"*80)
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*36 + "พิมพ์ exit เพื่อออก" + " "*25 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("##" + " "*76 + "##")
    print("#"*80)
    inp_exit = input()
    if (inp_exit == "exit"):
        break
