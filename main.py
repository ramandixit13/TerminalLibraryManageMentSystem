import tasks
import menu as m
import psycopg2

if __name__ == '__main__':

    # input
    n = None

    while n != '0':
        m.print_menu()
        n = input("Enter a number[0-4] : ")
        #user based operations
        if n == '1':
            m.print_user_operation()
            user_input = input("Enter a number : ")
            while user_input != '5':
                if user_input == '1':
                    tasks.add_user()
                    break
                elif user_input == '2':
                    name = str(input("Enter user name : "))
                    contact_number = str(input("Enter contact number : "))
                    # get user id
                    user_id = tasks.get_userid(name,contact_number)
                    # delete operation
                    tasks.remove_users(user_id)
                    break
                elif user_input == '3':
                    name = str(input("Enter user name : "))
                    contact_number = str(input("Enter contact number : "))
                    # get the user id
                    user_id = tasks.get_userid(name,contact_number)
                    #update
                    tasks.update_user(user_id)
                    break
                elif user_input == '4':
                    tasks.show_all_users()
                    break
        # books based operations
        elif n == '2':
            m.print_books_operation()
            user_input = input("Enter a number : ")
            while user_input != '6':
                if user_input == '1':
                    tasks.add_books()
                    break
                elif user_input == '2':
                    name = str(input("Enter book name : ")).lower()
                    # get bookid
                    book_id = tasks.get_bookid(name)
                    #update
                    tasks.update_book(book_id)
                    break
                elif user_input == '3':
                    name = str(input("Enter book name : ")).lower()
                    # book id
                    book_id = tasks.get_bookid(name)
                    #update
                    tasks.remove_books(book_id)
                    break
                elif user_input == '5':
                    tasks.show_all_books()
                    break
        # rental based operations
        elif n == '3':
            m.print_rental_operations()
            user_input = input("Enter a number : ")
            while user_input != '3':
                if user_input == '1':
                    book = str(input("Enter book you want to rent : ")).lower()
                    tasks.rent(book)
                    break
                elif user_input == '2':
                    book = str(input("Enter book name you want to return : ")).lower()
                    tasks.return_book(book)
                    break
        # librarian
        elif n == '4':
            m.print_librarian_task()
            user_input = input("Enter a number : ")
            while user_input != '3':
                if user_input == '1':
                    tasks.add_librarian()
                    break
                elif user_input == '2':
                    tasks.show_all_librarian()
                    break
print("Exiting.....................")
