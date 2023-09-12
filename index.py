class Bike:
    def __init__(self,stock):
        self.stock = stock
    def showStock(self):
        print("TOTAL STOCK IS : ",self.stock)
    def rentBike(self,qnt):
        if qnt<= 0:
            print("ENTER THE CORRECT VALUE")
        elif qnt > self.stock:
            print("ENTERED VALUE IS GREATER THAN STOCK")
        else:
            print("YOU SELECTED ",qnt," BIKES AND THE PRICE IS ",qnt*100)
            self.stock = self.stock - qnt
            print("Total stock is ",self.stock)

obj = Bike(100)
while True:
    
    uii = int(input(''' 
1 Show stock
2 Rent a bike
3 Exit
    '''))
    if uii == 1:
        obj.showStock()
    elif uii == 2:
        n = int(input("ENTER THE QUANTITY : "))
        obj.rentBike(n)
    else:
        break
