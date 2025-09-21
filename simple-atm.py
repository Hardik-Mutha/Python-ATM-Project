# Multiple Accounts Database (PIN -> Balance + History)
accounts = {
    7894: {"balance": 5000, "history": []},
    1234: {"balance": 2000, "history": []},
    5678: {"balance": 10000, "history": []}
}

# Login with max 3 attempts
attempts = 0
pin = None
while attempts < 3:
    check = int(input("Enter your PIN: "))
    if check in accounts:
        print("Access Granted ✅")
        pin = check
        break
    else:
        print("Access Denied ❌")
        attempts += 1
else:
    print("Too many wrong attempts. Card blocked 🚫")
    exit()

# Current user account
current_account = accounts[pin]

# Functions
def balance_check():
    print(f"Your current balance is: ₹{current_account['balance']}")

def deposit_money():
    amount = int(input("Enter amount for deposit: "))
    current_account["balance"] += amount
    print(f"₹{amount} deposited successfully. Current balance: ₹{current_account['balance']}")
    current_account["history"].append(f"Deposited ₹{amount}")

def withdraw_money():
    amount = int(input("Enter amount for withdraw: "))
    if amount > current_account["balance"]:
        print("❌ Your balance is insufficient.")
    else:
        current_account["balance"] -= amount
        print(f"₹{amount} withdrawn successfully. Current balance: ₹{current_account['balance']}")
        current_account["history"].append(f"Withdrew ₹{amount}")

def transaction_history():
    print("📜 Transaction History:")
    if current_account["history"]:
        for tx in current_account["history"]:
            print("-", tx)
    else:
        print("No transactions yet.")

def transfer_money():
    receiver_pin = int(input("Enter receiver PIN: "))
    if receiver_pin not in accounts:
        print("❌ Receiver account not found.")
        return
    amount = int(input("Enter amount to transfer: "))
    if amount > current_account["balance"]:
        print("❌ Insufficient balance.")
    else:
        current_account["balance"] -= amount
        accounts[receiver_pin]["balance"] += amount
        current_account["history"].append(f"Transferred ₹{amount} to {receiver_pin}")
        accounts[receiver_pin]["history"].append(f"Received ₹{amount} from {pin}")
        print(f"✅ ₹{amount} transferred successfully to account {receiver_pin}")

# Main ATM Loop
to_continue = True
while to_continue:
    print("\n----- Welcome to Hardik ATM -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Transfer Money")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        balance_check()
    elif choice == 2:
        deposit_money()
    elif choice == 3:
        withdraw_money()
    elif choice == 4:
        transaction_history()
    elif choice == 5:
        transfer_money()
    elif choice == 6:
        print("🙏 Thank you for using Hardik ATM ☺️")
        to_continue = False
    else:
        print("❌ Invalid choice.")
