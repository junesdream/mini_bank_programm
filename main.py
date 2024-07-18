""" #Mini Bank Programm with Python 

def show_balance(balance):
    print("**********************")
    print(f"Your balance is {balance:.2f}")
    print("**********************")

def deposit():
    print("**********************")
    total = float(input("Enter an amount to be deposited: "))
    print("**********************")
    if total < 0:
        print("You cannot deposit a negative amount.")
        print("**********************")
        return 0
    else:
        return total
    
def withdraw(balance):
    print("**********************")
    total = float(input("Enter an amount to be withdrawn: "))
    print("**********************")

    if total < 0:
        print("**********************")
        print("You cannot withdraw a negative amount.")
        print("**********************")
        return 0
    elif total > balance:
        print("**********************")
        print("You cannot withdraw more than your balance.")
        print("**********************")
        return 0
    else:
        return total

def main():
    balance = 0
    is_running = True

    while is_running:
        print("**********************")
        print("*** Banking Program ****")
        print("**********************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("**********************")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
            
        else:
            print("**********************")
            print("Invalid choice. Please enter a number between 1 and 4.")
            print("**********************")

    print("**********************")
    print("Have a nice day and see you soon!")
    print("**********************")


if __name__ == "__main__":
    main()
     """

# Mini Bank Programm mit Python
# Dieses Programm simuliert eine einfache Bankanwendung, bei der der Benutzer sein Guthaben anzeigen,
# Einzahlungen vornehmen und Abhebungen tätigen kann.

def show_balance(balance):
    """Zeigt den aktuellen Kontostand an."""
    print("**********************")
    print(f"Ihr Kontostand beträgt: {balance:.2f} EUR")
    print("**********************")

def deposit():
    """Ermöglicht dem Benutzer eine Einzahlung vorzunehmen."""
    print("**********************")
    try:
        total = float(input("Bitte geben Sie den Betrag ein, den Sie einzahlen möchten: "))
        if total < 0:
            raise ValueError("Sie können keinen negativen Betrag einzahlen.")
    except ValueError as e:
        print(e)
        print("**********************")
        return 0
    print(f"Sie haben {total:.2f} EUR eingezahlt.")
    print("**********************")
    return total
    
def withdraw(balance):
    """Ermöglicht dem Benutzer eine Abhebung vorzunehmen."""
    print("**********************")
    try:
        total = float(input("Bitte geben Sie den Betrag ein, den Sie abheben möchten: "))
        if total < 0:
            raise ValueError("Sie können keinen negativen Betrag abheben.")
        elif total > balance:
            raise ValueError("Sie können nicht mehr als Ihr Guthaben abheben.")
    except ValueError as e:
        print(e)
        print("**********************")
        return 0
    print(f"Sie haben {total:.2f} EUR abgehoben.")
    print("**********************")
    return total

def display_menu():
    """Zeigt das Hauptmenü an."""
    print("**********************")
    print("*** Banking Programm ****")
    print("**********************")
    print("1. Kontostand anzeigen")
    print("2. Einzahlung vornehmen")
    print("3. Abhebung vornehmen")
    print("4. Beenden")
    print("**********************")

def main():
    balance = 0.0  # Anfangskontostand
    is_running = True

    while is_running:
        display_menu()
        choice = input("Bitte wählen Sie eine Option (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
            print("Vielen Dank, dass Sie unser Banking Programm genutzt haben. Auf Wiedersehen!")
        else:
            print("Ungültige Wahl. Bitte wählen Sie eine Nummer zwischen 1 und 4.")
            print("**********************")

if __name__ == "__main__":
    main()
