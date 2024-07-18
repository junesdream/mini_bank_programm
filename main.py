
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
