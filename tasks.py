import psycopg2
from config import config


def add_user():
    """insert into users(userid,name,email_id,address,contact_number)"""
    connection = None
    try:
        # read connection parameters
        params = config()

        # connect to postgreSQL server
        connection = psycopg2.connect(**params)

        # create a cursor
        cursor = connection.cursor()

        # asking user for inputs
        name = str(input("Enter user name : ")).lower()
        email = str(input("Enter mail id : "))
        add = str(input("Enter the address : "))
        contact = str(input("Enter mobile number : "))

        # execute statements
        query = "INSERT INTO users(userid,name,email_id,address,contact_number) values(nextval('userid_seq'),%s,%s,%s,%s);"
        data = (name,email,add,contact)
        cursor.execute(query,data)

        # commit the changes
        connection.commit()

        # close the connection
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def update_user(user_id):
    connection = None

    try:
        params = config()

        connection = psycopg2.connect(**params)

        cursor = connection.cursor()

        # asking user for inputs
        print("Enter the column[(n)ame, (e)mail, (a)ddress,(c)ontact] you want to update or enter 'all' for whole update : ")
        field_update = str(input("Enter the value : "))

        if field_update == 'n' or 'N':
            print("Enter the updated name : ")
            updated_name = str(input()).lower()
            query = "UPDATE users SET name = %s WHERE userid = %s;"
            data = (updated_name,user_id)
            cursor.execute(query,data)
            connection.commit()
            print("\n\nOne row and column affected ....\n\n")

        elif field_update == 'e' or 'E':
            print("Enter the updated email : ")
            updated_email = str(input())
            query = "UPDATE users SET email = %s WHERE userid = %s;"
            data = (updated_email,user_id)
            cursor.execute(query,data)
            connection.commit()
            print("\n\nOne row and column affected ....\n\n")

        elif field_update == 'a' or 'A':
            print("Enter the updated address : ")
            updated_add = str(input())
            query = "UPDATE users SET address = %s WHERE userid = %s;"
            data = (updated_add,user_id)
            cursor.execute(query,data)
            connection.commit()
            print("\n\nOne row affected and column ....\n\n")

        elif field_update == 'c' or 'C':
            print("Enter the updated contact : ")
            updated_con = str(input())
            query = "UPDATE users SET contact_number = %s WHERE userid = %s;"
            data = (updated_con,user_id)
            cursor.execute(query,data)
            connection.commit()
            print("\n\nOne row and column affected ....\n\n")

        elif field_update == 'all' or 'ALL':
            print("Enter the updated name : ")
            updated_name = str(input()).lower()
            print("Enter the updated email : ")
            updated_email = str(input())
            print("Enter the updated address : ")
            updated_add = str(input())
            print("Enter the updated contact : ")
            updated_con = int(input())
            query = "UPDATE users SET name = %s, email = %s, address = %s, contact_number = %s WHERE userid = %s;"
            data = (updated_name,updated_email,updated_add,updated_con,user_id)
            cursor.execute(query,data)
            connection.commit()
            print("\n\nOne row affected .... Several colum affected ......\n\n")

        # close the connection
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def show_all_users():
    connection = None

    try:
        params = config()

        connection = psycopg2.connect(**params)

        cursor = connection.cursor()

        # execute statements
        query = "SELECT name,email_id,address,contact_number from users;"

        cursor.execute(query)

        rows = cursor.fetchall()
        print("\n\nNumber of rows counted : ",cursor.rowcount)

        for row in rows:
            print(row)

        # close the connection
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def get_userid(name,contact_number):
    connection = None

    try:
        params = config()

        connection = psycopg2.connect(**params)

        cursor = connection.cursor()

        # execute statements
        query = "SELECT DISTINCT userid,name FROM users WHERE name = %s AND contact_number = %s;"
        data = (name,contact_number)
        cursor.execute(query,data)

        id = cursor.fetchone()[0]
        print(id)
        # close the connection
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return id

def remove_users(userid):
    connection = None
    try:
        params = config()

        connection = psycopg2.connect(**params)

        cursor = connection.cursor()

        # execute statements
        cursor.execute("DELETE FROM users WHERE userid = %s;",(userid,))
        print("row deleted ......{0}".format(cursor.rowcount))
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def add_librarian():
    connection = None

    try:
        params = config()

        connection = psycopg2.connect(**params)

        cursor = connection.cursor()

        # asking user for inputs
        name = str(input("Enter librarian name : "))
        contact = str(input("Enter mobile number : "))

        # execute statements
        query = "INSERT INTO librarian(libid,name,contact_number) values(nextval('lib_seq'),%s,%s);"
        data = (name, contact)
        cursor.execute(query,data)

        # commit the changes
        connection.commit()

        print("\n\n{0} is added...\n\n".format(name))
        # close the connection
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def show_all_librarian():
    connection = None

    try:
        params = config()

        connection = psycopg2.connect(**params)

        cursor = connection.cursor()

        # execute statements
        query = "SELECT * from librarian;"

        cursor.execute(query)

        rows = cursor.fetchall()


        for row in rows:
            print(row)

        print("Number of rows counted : ",cursor.rowcount,"\n\n")
        # close the connection
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()




def add_books():
    """insert into books(bookid,name,publication_company)"""
    connection = None
    try:
        # read connection parameters
        params = config()

        # connect to postgreSQL server
        connection = psycopg2.connect(**params)

        # create a cursor
        cursor = connection.cursor()

        # asking user for inputs
        name = str(input("Enter book name : ")).lower()
        publication_company = str(input("Enter publication company name : ")).lower()
        author_name = str(input("Enter author name : ")).lower()

        # execute statements
        query = "INSERT INTO books(bookid,name,publication_company) values(nextval('book_seq'),%s,%s);"
        data = (name, publication_company)
        cursor.execute(query, data)
        connection.commit()

        query_author = "INSERT INTO authors(authorid,name,bookid) values(nextval('auth_seq'),%s,%s);"
        book_id = get_bookid(name)
        data1 =(author_name, book_id)
        cursor.execute(query_author , data1)
        connection.commit()
        print("\n\n Value inserted ....\n\n")

        # close the connection
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def update_book(bookid):
    connection = None

    try:
        params = config()

        connection = psycopg2.connect(**params)

        cursor = connection.cursor()

        # asking user for inputs
        print("Enter the column[(n)ame, (p)ublication company] you want to update or enter 'all' for whole update : ")
        field_update = str(input("Enter the value : "))

        if field_update == 'n' or 'N':
            print("Enter the updated name : ")
            updated_name = str(input()).lower()
            query = "UPDATE books SET name = %s WHERE bookid = %s;"
            data = (updated_name,bookid)
            cursor.execute(query,data)
            connection.commit()
            print("\n\nOne row and column affected ....\n\n")

        elif field_update == 'p' or 'P':
            print("Enter the publication comapany : ")
            updated_pub = str(input()).lower()
            query = "UPDATE books SET publication_company = %s WHERE bookid = %s;"
            data = (updated_pub,bookid)
            cursor.execute(query,data)
            connection.commit()
            print("\n\nOne row and column affected ....\n\n")

        elif field_update == 'all' or 'ALL':
            print("Enter the updated name : ")
            updated_name = str(input()).lower()
            print("Enter the updated publication company : ")
            updated_pub = str(input()).lower()
            query = "UPDATE users SET name = %s, publication_company = %s WHERE bookid = %s;"
            data = (updated_name,updated_pub,bookid)
            cursor.execute(query,data)
            connection.commit()
            print("\n\nOne row affected .... Several colum affected ......\n\n")

        # close the connection
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def get_bookid(book):
    connection = None
    try:
        params = config()

        connection = psycopg2.connect(**params)

        cursor = connection.cursor()
        # execute statements
        query = "SELECT bookid FROM books WHERE name = %s;"
        cursor.execute(query,(book,))

        id = cursor.fetchone()[0]
        # close the connection
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return id

def remove_books(bookid):
    connection = None
    try:
        params = config()

        connection = psycopg2.connect(**params)

        cursor = connection.cursor()

        # execute statements
        cursor.execute("DELETE FROM books WHERE bookid = %s;",(bookid,))
        print("row deleted ......{0}".format(cursor.rowcount))
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def show_all_books():
    connection = None

    try:
        params = config()

        connection = psycopg2.connect(**params)

        cursor = connection.cursor()

        # execute statements
        query = "SELECT * from books;"

        cursor.execute(query)

        rows = cursor.fetchall()
        print("Number of rows counted : ",cursor.rowcount)

        for row in rows:
            print(row)

        # close the connection
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
def rent(book):
    connection = None
    try:
        params = config()

        connection = psycopg2.connect(**params)

        cursor = connection.cursor()
        # bookid for the book
        bookid = get_bookid(book)

        # execute statement
        query = "SELECT available FROM loan_book WHERE bookid = %s;"
        cursor.execute(query,(bookid,))
        rows = cursor.fetchall()

        if len(rows) == 0:
            query = "INSERT INTO loan_book(bookid,available,rented_user,date_issued,date_due_for_return,date_returned,userid) VALUES(%s,%s,%s,%s,%s,%s,%s);"
            user = str(input("Enter name of user : ")).lower()
            contact_number = str(input("Enter your mobile number : "))
            date_issue = str(input("Enter date of issuing(DD/MM/YYYY) : "))
            date_return = str(input("Enter date of returning(DD/MM/YYYY) : "))
            user_id = get_userid(user,contact_number)
            data = (bookid,'FALSE',user,date_issue,date_return,'not yet',user_id)
            cursor.execute(query,data)

            # commit the changes
            connection.commit()
        else:
            availablity = cursor.fetchone()[0]
            if availablity == True:
                query = "INSERT INTO loan_book(bookid,available,rented_user,date_issued,date_due_for_return,date_returned,userid) VALUES(%s,%s,%s,%s,%s,%s,%s);"
                user = str(input("Enter name of user : ")).lower()
                contact_number = str(input("Enter your mobile number : "))
                date_issue = str(input("Enter date of issuing(DD/MM/YYYY) : "))
                date_return = str(input("Enter date of returning(DD/MM/YYYY) : "))
                user_id = get_userid(user,contact_number)
                data = (bookid,'FALSE',user,date_issue,date_return,'not yet',user_id)
                cursor.execute(query,data)

                # commit the changes
                connection.commit()
            else:
                print("\n\nBook is already rented out....\n\n")

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def return_book(book):
    connection = None
    try:
        params = config()

        connection = psycopg2.connect(**params)

        cursor = connection.cursor()

        # get book id
        book_id = get_bookid(book)

        # execute statment
        query = "SELECT userid, date_returned from loan_book where bookid = %s;"
        cursor.execute(query,(book_id))
        userid = cursor.fetchone()[0]
        date_returned = cursor.fetchone()[1]
        if date_returned == 'not yet':
            query = "UPDATE loan_book SET date_returned = %s WHERE userid = %s;"
            date = str(input("Enter the date : "))
            data = (date,userid)
            cursor.execute(query,data)

            connection.commit()

            cursor.close()
        else:
            print("\n\nEither book has been returned or something ...\n\n")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
