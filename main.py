import json
import os

data_file = "library.json"  

# Checks the JSON file for data
def check_library():
    if os.path.exists(data_file):
        try:
            with open(data_file, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []  # Handle empty or corrupt file
    return []

def save_library(library):
    with open(data_file, "w") as file:
        json.dump(library, file)

# Function to add a book
def add_book(library):
    title = input("Enter the title of the book: ").lower()
    author = input("Enter the author of the book: ").lower()
    publish_date = input("Enter the publish_date of the book: ").lower()
    genre = input("Enter the genre of the book: ").lower()
    read = input("Have you read the book? (yes/no): ").lower() == "yes"
    
    new_book = {
        "title": title,
        "author": author,
        "publish_date": publish_date,
        "genre": genre,
        "read": read
    }
    
    library.append(new_book)
    save_library(library)
    print(f'Book "{title}" added successfully.')

# Function to remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    initial_length = len(library)

    library = [book for book in library if book["title"].lower() != title]

    if len(library) < initial_length:
        save_library(library)
        print(f'Book "{title}" removed successfully.')
    else:
        print(f'Book "{title}" not found in the library.')

# Function to search for a book by title or author
def search_book(library):
    search_by = input("Search by title or author? ").strip().lower()
    search_term = input(f'Enter the {search_by}: ').strip().lower()

    if search_by not in ["title", "author"]:
        print("Invalid search criteria. Choose 'title' or 'author'.")
        return

    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        for book in results:
            status = "Read" if book["read"] else "Unread"
            print(f'{book["title"]} by {book["author"]} - {book["publish_date"]} - {book["genre"]} - {status}')
    else:
        print(f'No book found with "{search_term}" in {search_by}.')

# Function to display all books
def display_books(library):
    if library:
        for book in library:
            status = "Read" if book["read"] else "Unread"
            print(f'{book["title"]} by {book["author"]} - {book["publish_date"]} - {book["genre"]} - {status}')
    else:
        print("Library is empty.")

# Function to display statistics
def display_stats(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f'Total books: {total_books}')
    print(f'Read percentage: {percentage_read:.2f}%')

# Main function
def main():
    library = check_library()
    while True:
        print("\nWellcome to your Personal Library manager")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search the Library")
        print("4. Display all Books")
        print("5. Display Statistics")
        print("0. Exit")

        user = input("Select an option: \n")
        if user == "1":
            add_book(library)
        elif user == "2":
            remove_book(library)
        elif user == "3":
            search_book(library)
        elif user == "4":
            display_books(library)
        elif user == "5":
            display_stats(library)
        elif user == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == '__main__':
    main()
1