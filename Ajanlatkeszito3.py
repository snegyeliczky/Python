import sys
import os

if os.path.exists(sys.argv[1]):
    os.remove(sys.argv[1])


wcm = {'fűnyirás':1000,"ásás":2500,"füvesítes":4210,"gyepszelőztetés":2352,"fa metcés":3471}

def price_writer(file_name,kategori,price):
    with open(file_name,"a+") as offer_file:
                offer_file.write("\n"+kategori+": "+str(price)+" Forint")

def final_price_writer(file_name,all_price):
    with open(file_name,"a") as offer_file:
                offer_file.write("\n"+"Végösszeg: --- "+str(all_price)+" Forint")
 
all_price = 0

while True:
    print("Nyomd meg az 1-est uj tétel hozzáadásához: "+ "\n"+"Nyomd meg a 2-est a végösszeg hozzáadáshoz és a kilépéshez")
    if int(input("Add meg a választásod: ")) == 1:
        print("Megadható kategoriák: fűnyirás,ásás,füvesítés,gyepszelőztetés,fa metcés")
        kategori= input("add meg a kategoriat: ")
        quantity = input("add meg a mennyiséget: ")
        price = wcm[kategori]*int(quantity)
        all_price += price
        print(str(price)+" forint")
        price_writer(sys.argv[1],kategori,price)
    elif int(input("Add meg a választásod: ")) == 2:
        print(str(all_price)+" forint")
        final_price_writer(sys.argv[1],all_price)
        exit()
    else: 
        exit()




