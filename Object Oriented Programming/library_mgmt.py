#Here the class will be library and methods will be issue book, return book, display available books


class Library:
    def __init__(self, list_of_books):
        self.available_books = list_of_books
        self.issued_books = []  # Track issued books
    
    def issue_book(self, book_name):
        """Issue a book to a user if available"""
        if book_name in self.available_books:
            self.available_books.remove(book_name)
            self.issued_books.append(book_name)  # Track issued book
            print(f"✅ You have issued '{book_name}'")
        else:
            print(f"❌ Sorry, '{book_name}' is not available")
    
    def return_book(self, book_name):
        """Return a book back to the library"""
        # FIXED: Check if book was issued (not if it's available)
        if book_name in self.issued_books:
            self.issued_books.remove(book_name)
            self.available_books.append(book_name)
            print(f"✅ You have returned '{book_name}'. Thank you!")
        else:
            print(f"❌ '{book_name}' was not issued from this library or doesn't exist.")
    
    def display_available_books(self):
        """Display all available books"""
        if self.available_books:
            print("\n📚 Available books:")
            for i, book in enumerate(self.available_books, 1):
                print(f"   {i}. {book}")
        else:
            print("\n📚 No books currently available")
    
    def display_issued_books(self):
        """Display all issued books"""
        if self.issued_books:
            print("\n📖 Currently issued books:")
            for i, book in enumerate(self.issued_books, 1):
                print(f"   {i}. {book}")
        else:
            print("\n📖 No books currently issued")
    
    def display_library_status(self):
        """Display complete library status"""
        print("\n" + "="*50)
        print("📊 LIBRARY STATUS")
        print("="*50)
        self.display_available_books()
        self.display_issued_books()
        print("="*50)


available_books = [
    "Hooked", 
    "The Art of Persuasion", 
    "Atomic Habits", 
    "Rich Dad Poor Dad", 
    "The Alchemist", 
    "Think and Grow Rich", 
    "The Almanac of Naval Ravikant", 
    "The Psychology of Money", 
    "The Subtle Art of Not Giving a F*ck"
]

library1 = Library(available_books)

print("🏛️  Welcome to the Digital Library System!")
library1.display_library_status()

# Issue a book
while True:
    issue_book = input("\n📖 Enter the name of the book you want to issue (or 'skip' to continue): ").strip()
    if issue_book.lower() == 'skip':
        break
    library1.issue_book(issue_book)
    library1.display_library_status()
    break

# Return a book
while True:
    return_book = input("\n📚 Enter the name of the book you want to return (or 'skip' to continue): ").strip()
    if return_book.lower() == 'skip':
        break
    library1.return_book(return_book)
    library1.display_library_status()
    return_book