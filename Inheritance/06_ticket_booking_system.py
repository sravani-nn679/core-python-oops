class Movie:#multilevel
    def ticket(self, movie):
        movie=movie.lower()
        if movie=="premalu":
            return 200#ticket prize
        elif movie=="home":
            return 200
        else:
            return 0
class Booking(Movie):
    def movie(self):
        print("premalu-200")
        print("home-200")
    def billing(self,total):
        if total==0:
            print("Invalid movie")
        else:
            final=total+30 #packing prize
            print(final)
    def selection(self):
        self.movie()
        total=0
        n=int(input("enter no of tickets:"))
        for i in range(n):
            movie=input("enter movie name:")
            total=total+self.ticket(movie)
        self.billing(total)
class Customer(Booking):
    pass
c=Customer()
c.selection()


