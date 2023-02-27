from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Project_contact_book.contact_book import ContactBook

from datetime import datetime

engine = create_engine("sqlite:///kontaktu_knyga.db")
Session = sessionmaker(bind=engine)
session = Session()

choices = """ 1 - show existing contacts, 
2 - enter a new contact
3 - change a contact
4 - delete
5 - search
6 - filter by date of birth
ENTER - get out
"""

while True:
    the_choice = input(choices)
    if the_choice == "":
        break

    elif the_choice == "1":
        contacts = session.query(ContactBook).all()
        for s in contacts:
            print(s)

    elif the_choice == "2":
        name = input("Add a name: ").capitalize()
        lname = input("Add a last name: ").capitalize()
        bday = datetime.strptime(input("Add a birth day, pvz: 2000-01-01: "), "%Y-%m-%d").date()
        job = input("Add a user responsibilities: ")
        while True:
            phone_number = 0
            try:
                phone_number = int(input("Add phone"))
            except ValueError:
                print("That's not a number!")

            phone_number_str = str(phone_number)
            if (len(phone_number_str) < 9) or (len(phone_number_str) > 9):
                print("Wrong number!!!")
            else:
                print("OK")
                break
        email_adress = "{0}@gmail.com".format(name)
        book = ContactBook(name, lname, bday, job, phone_number, email_adress)
        session.add(book)
        session.commit()

    elif the_choice == "3":
        contacts = session.query(ContactBook).all()
        for s in contacts:
            print(s)
        change_contact = int(input("Enter the contact id, where you want change contact: "))
        nr = session.query(ContactBook).get(change_contact)
        change_choice = input(
            "1 - change name, 2 - change last name, 3 - change birth day, 4 - chenge job, 5 - change phone nuber,"
            "6 - change email adres")
        if change_choice == "1":
            nr.name = input("Add a new name: ").capitalize()
        elif change_choice == "2":
            nr.lname = input("Add a new last name: ").capitalize()
        elif change_choice == "3":
            nr.bday = datetime.strptime(input("Add a new birth day: "), "%Y-%m-%d").date()
        elif change_choice == "4":
            nr.job = input("Add a new user responsibilities: ")
        elif change_choice == "5":
            nr.phone_number = int(input("Add phone"))
            while True:
                phone_number = 0
                try:
                    phone_number = int(input("Add phone"))
                except ValueError:
                    print("That's not a number!")

                phone_number_str = str(phone_number)
                if (len(phone_number_str) < 9) or (len(phone_number_str) > 9):
                    print("Wrong number!!!")
                else:
                    print("OK")
                    break
        elif change_choice == "6":
            nr.email_adress = "{0}@gmail.com".format(nr.name)
        else:
            print("Choice not found")
        session.commit()

    elif the_choice == "4":
        contacts = session.query(ContactBook).all()
        for s in contacts:
            print(s)
        del_contact = int(input("Enter the contact id, where you want delete contact: "))
        nr = session.query(ContactBook).get(del_contact)
        session.delete(nr)
        session.commit()

    elif the_choice == "5":
        search_with_letter = input("Enter first 2 of name or last name letters: ")
        filtr = search_with_letter + "%"
        print("CONTACT INFO")
        rezults = session.query(ContactBook).filter(
            ContactBook.name.ilike(filtr) |
            ContactBook.lname.ilike(filtr)
        ).all()

        if rezults == []:
            print(f"Nothing was found for the letter {search_with_letter}, try again")
        else:
            for contact in rezults:
                print(contact)

    elif the_choice == "6":
        contacts = session.query(ContactBook).all()
        bday_from = input("Enter the date from you want filter: ")
        bday_to = input("Enter the date to you want filter: ")
        birth = session.query(ContactBook).filter(
            (ContactBook.bday > bday_from) |
            (ContactBook.bday < bday_to)).all()
        for x in birth:
            print(x)

    else:
        print("No choice found!!")
