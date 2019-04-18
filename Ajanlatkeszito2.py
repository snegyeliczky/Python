class work_karegories:
    def __init__(self,kategori,price):
        self.kategori = kategori
        self.price = price

    def total_price_maker(self,quantity):
        return self.price*quantity

wcm = {'fünyirás':1000,"ásas":2500,"füvesites":4210}

funyiras = work_karegories('fünyiras',1000)
asas = work_karegories("ásás",2500)
fuvesites = work_karegories("füvesites",4210)

#print(funyiras.__dict__)
#print(asas.total_price_maker(int(input("Add meg a menyiséget: "))))

kategori= input("add meg a kategoriat: ")
quantity = input("add meg a mennyiséget: ")
price = wcm[kategori]*int(quantity)
print(price)



prices = ["Az ajánlat paraméterei a következöek: "]
all_price = []

def price_macker(kategori,price,manige):
    total_price= price*manige
    all_price.append(total_price)
    total_price_element= kategori+": "+str(total_price)+" Forint"
    prices.append("\n"+total_price_element)
    print(prices)
    print(all_price)

def price_writer(file_name):
    with open(file_name,"w") as offer_file:
                for i in range(len(prices)):
                    offer_file.write(prices[i])
                offer_file.write("\n"+"összesen: "+str(sum(all_price))+" Forint")
    

#while True:
#    price_macker(input("Add meg a munka típusát: "),int(input("Add meg az munkatípus egységárát: ")),int(input("Add meg az munkatípus mennyiségét: ")))
#   price_writer("Ajánlat.txt")
