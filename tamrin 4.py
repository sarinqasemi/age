class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):        
         print(f"Title: {self.title}")  
         print(f"Author: {self.author}")
         print(f"Price: ${self.price:.2f}")

    def apply_discount(self, discount_percent):
         self.price = self.price * (1 - discount_percent / 100)


book1 = Book("Harry Potter", "J.K. Rowling", 700000)
book2 = Book("The Alchemist", "Paulo Coelho", 650000)

print("Book 1 :")
book1.display_details()

discount = float(input("Enter discount percentage for Book 2: "))
book2.apply_discount(15)

print("Book 1 :")
book1.display_details()
print("Book 2 :")
book2.display_details()
