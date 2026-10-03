#multilevel Inheritance
class Restaurant:
    def menu(self,item):
        item=item.lower()
        if item=="biryani":
            return 250
        elif item=="pizza":
            return 300
        else:
            return 0
class FoodCourt(Restaurant):
    def display_menu(self):
        print("biryani-250")
        print("pizza-300")
    def billing(self, total):
        if total==0:
            print("Invalid item")
        else:
            final=total+20 #packing prize 20
            print(final)
    def order(self):
        self.display_menu()
        total=0
        n=int(input("enter no of items:"))
        i=0
        while i<n:
            item=input("enter item name:")
            prize=self.menu(item)
            if prize==0:
                print("invalid item")
            else:
                total=total+prize
                i+=1
        self.billing(total)
class Customer(FoodCourt):
    pass
c=Customer()
c.order()
