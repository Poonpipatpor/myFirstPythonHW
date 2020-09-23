from suds.clients import Client
price_oil = {"Gasoline 95" : 29.16,
             "Gasoline 91" : 25.30,
             "Gasohol  91" : 21.68,
             "Gasohol  E20": 20.2,
             "Gasohol  95" : 21.2,
             "Diesel"      : 21.2}

client = Client('http://www.pttor.com/OilPrice.asmx?WSDL')
Oilprice = client.service.CurrentOilPrice(Language = 'thai')

import xmltodict,json
OilPrice1 = xmltodict.parse(OilPrice) # ผลลัพธ์จะเท่ากับ json ในสตริง
Price = eval(json.dumps(OilPrice1)) # เรียกใช้งาน json ในสตริง
print(Price)

for i in Price["PTTOR_DS"



while True:
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
    print("##" + " "*76 + "##")ofidznbhof
