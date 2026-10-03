#multilevel Inheritance
class Restaurant:
    def menu(self,item):
        if item=="biryani":
            return 250
        elif item=="pizza":
            return 300
class FoodCourt(Restaurant):
    def display_menu(self):
        print("biryani-250")
        print("pizza-300")
    def billing(self, total):
        final=total+20 #packing prize 20
        print(final)
    def order(self):
        self.display_menu()
        total=0
        n=int(input())
        for i in range(n):
            item=input()
            total=total+self.menu(item)
        self.billing(total)
class Customer(FoodCourt):
    pass
c=Customer()
c.order()
