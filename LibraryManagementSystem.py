import time
books = {
    "1984" : 1,
    "Animal Farm" : 3,
    "Mein Kampf" : 0
}
# Numbers indicate available copies
books_rented = {
    "1984" : 2,
    "Animal Farm" : 0,
    "Mein Kampf" : 3
}
def view_available_books():
    for key, element in books.items():
        if element > 1:
            print(f"We have {element} copies of {key} available")
        elif element == 1:
            print(f"We have 1 copy of {key} available")

def borrow_books():
    available_books = []
    for key, element in books.items():
        if element > 0:
            available_books.append(key)
    books_present = True
    if available_books == "":
        books_present = False
    
    while books_present:
        for element in available_books:
            if books[element] == 1:
                print(f"{element} has 1 available copy.")
            else:
                print(f"{element} has {available_books[element]} available copies.")
        book_to_borrow = input("Please enter the name of the book you would like to borrow (or q to stop borrowing): ")
        if book_to_borrow.lower() == "q":
            break
        elif book_to_borrow not in available_books:
            print("We're sorry, but that book isn't available.")
        else:
            books[book_to_borrow] -= 1
            books_rented[book_to_borrow] += 1
            if books[book_to_borrow] == 0:
                available_books.remove(book_to_borrow)
            print(f"You have borrowed '{book_to_borrow}', {books[book_to_borrow]} copies remain.")

def return_books():
    borrowed_books = []
    for key in books:
        if books_rented[key] > 0:
            borrowed_books.append(key)
    books_not_returned = True
    if borrowed_books == "":
        books_not_returned = False
    
    while books_not_returned:
        for element in borrowed_books:
            print(f"{element} has {books_rented[element]} non-returned copies.")
        book_to_return = input("Please enter the name of the book you would like to return (or q to stop returning): ")
        if book_to_return.lower() == "q":
            break
        elif book_to_return not in borrowed_books:
            print("That book is not rented out.")
            time.sleep(2)
        else:
            books[book_to_return] += 1
            books_rented[book_to_return] -= 1
            if books_rented[book_to_return] == 0:
                borrowed_books.remove(book_to_return)
                if borrowed_books == "":
                    print("There are no more books rented out.")
                    time.sleep(2)
                    break
            if books_rented[book_to_return] == 1:
                print(f"You have returned a copy of {book_to_return}. Now there is {books_rented[book_to_return]} copy not returned.")
                time.sleep(3)
            else:
                print(f"You have returned a copy of {book_to_return}. Now there are {books_rented[book_to_return]} copies not returned.")
                time.sleep(3)




while True:
    action = input("Would you like to (v)iew available books, (r)eturn a book, (b)orrow a book or (l)eave?: ")
    if action.lower() == "v":
        view_available_books()
    elif action.lower() == "r":
        return_books()
    elif action.lower() == "b":
        borrow_books()
    elif action.lower() == "l":
        break
    else:
        print("Please decide whether you want to (v)iew available books, (r)eturn a book or (b)orrow a book.")
        time.sleep(3)