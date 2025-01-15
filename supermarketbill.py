from datetime import datetime
#declaration of prices
name=input("enter your name:")
lists=('''          rice        Rs 70/kg
          sugar       Rs 48/kg
          wheat atta  Rs 65/kg
          salt        Rs 28/kg
          biscuit     Rs 10
          colgate     Rs 40
          oil         Rs 120/litre
       ''')

#intially values

price=0
totalamount=0
finalprice=0
pricelist=[]
ilist=[]
qlist=[]
plist=[]

items={'rice':70,'sugar':48,'wheat atta':65,'salt':28,'biscuit':10,'colgate':40,'oil':120}

option=int(input("for list of item press 1 :"))
option==1
print(lists)
for i in range(len(items)):
    inp1=int(input("to buy items press 1 else press 2:"))
    if inp1==2:
      break
    if inp1==1:
      item=input("enter your items:")
      quantity=int(input("enter quantity:"))
    if item in items.keys():
        price=quantity*(items[item])
        pricelist.append((item,quantity,items,price))
        totalamount+=price
        ilist.append(item)
        qlist.append(quantity)
        plist.append(price)
        gst=(totalamount*5)/100
        finalamount=gst+totalamount
    else:
       print("sorry the item is not there")
else:
   print("wrong option")
inp=input("can i bill the items yes or no:")
if inp=='yes':
   pass
   if finalamount!=0:
      print(25*"=","madhumathi stores",25*"=")
      print(25*"=","hyderabad")
      print("Name:",name,30*" ","Date:",datetime.now())
      print(75*"-")
      print("sno",8*" ",'items',3*" ",'quantity',5*" ",8*" " ,'price')
      for i in range(len(pricelist)):
        print(i,6*' ',5*' ',ilist[i],3*' ',qlist[i], 10*' ',plist[i])
      print(75*"-")
      print(50*" ",'totalamount:','Rs',totalamount)
      print('gst amount',40*" ",'Rs',gst)
      print(75*"-")
      print(50*" ","finalamount:",'Rs',finalamount)
      print(75*"-")
      print(25*" ","thank you bunny visit again")
      print(75*"-")


   
   