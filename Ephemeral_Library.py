class Library:
    def __init__(self):
        Books = []
        while True:
            i = int(input(" For Exit 0\n For Add Books 1\n For Number 2\n For Print Books 3\nPress the Input: "))
            if i == 0:
                break
            elif i == 1:
                new_book = input("Book Name: ").capitalize()
                if new_book in Books:
                    print("Already Added in List.")
                else:
                    Books.append(new_book)
                    print("Succesfully Added")
            elif i == 2:
                print("The Number of Books is: ",len(Books))
            elif i == 3:
                print("The Books are\n",Books,"\n")
            else:
                print(f"{i} is invalid")
l = Library()