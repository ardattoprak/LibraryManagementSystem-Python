book = open("books.txt","r",encoding="utf-8")
student = open("students.txt","r",encoding="utf-8")

def operation1():
    with open("books.txt","r") as book:
        for a in book:
            a = a.rstrip("\n")
            a = a.split(",")

            ISBN = a[0]
            bookname= a[1]
            authorname = a[2]
            TorF = a[3]
            print(a)

def operation2():
    with open("books.txt","r") as book:
        for a in book:
            a = a.rstrip("\n")
            a = a.split(",")

            ISBN = a[0]
            bookname = a[1]
            authorname = a[2]
            TorF = a[3]
            if a[3] == 'T':
                print(a[1])

def operation3():
    ISBN = input("Please enter ISBN number of the book:")
    bookname = input("Please enter name of the book:")
    authorname = input("Please enter name of the author of the book")

    with open("books.txt", "a") as book:
        book.write(ISBN +"," + bookname +"," + authorname+"," + "F" )

def operation4():
    with open("books.txt", "r") as book:
        newISBN = input("Please enter the ISBN:")
        for a in book:
            a = a.rstrip("\n")
            a = a.split(",")

            ISBN = a[0]
            bookname = a[1]
            authorname = a[2]
            TorF = a[3]
            if a[0] == newISBN:
                print(a[0:4])
def operation5():
    with open("books.txt", "r") as book:
        newBookname = input("Please enter the book name:")
        for a in book:
            a = a.rstrip("\n")
            a = a.split(",")

            ISBN = a[0]
            bookname = a[1]
            authorname = a[2]
            TorF = a[3]
            if newBookname in bookname:
                print(a[0:4])

def operation6():
    with open("books.txt", "r") as book:
        searchingstudentid = input("Please enter the student id: ")
        searchingbookISBN = input("Please enter the book ISBN: ")
        for a in book:
            a = a.rstrip("\n")
            a = a.split(",")

            ISBN = a[0]
            bookname = a[1]
            authorname = a[2]
            TorF = a[3]

    with open("students.txt", "r") as student:
        for b in student:
            b = b.split(" ")

            studentid = b[0]
            studentname = b[1]
            studentsurname = b[2]
            studentbooks = ""
    a1 = []
    if searchingbookISBN in ISBN:
        print("The book is in the library.")
        if searchingstudentid in studentid:
            with open("books.txt", "r+", encoding="utf-8") as file:
                for a in file:
                    a = a.rstrip("\n")
                    a1 = a.split(",")
                    if searchingbookISBN in a1:
                        if a1[3] == "F":
                            a1[3] = "T"
    print(a1)

while True:
    operation = input('-----------------------\nPress 1 to see all books in the library.\nPress 2 to list all the books that are checked out.\nPress 3 to add a new book.\nPress 4 to search a book by ISBN number\nPress 5 to search a book by name\nPress 6 to check out a book to a student\n-----------------------')

    if operation == '1':
        operation1()
    elif operation == '2':
        operation2()
    elif operation == '3':
        operation3()
    elif operation == '4':
        operation4()
    elif operation == '5':
        operation5()
    elif operation == '6':
        operation6()
    else:
        break
