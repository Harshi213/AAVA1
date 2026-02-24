from auth import login
from payment import process_payment

def main():
    user = "admin"
    password = "admin123"

    if login(user, password):
        print("Login successful")
        process_payment(1000)
    else:
        print("Login failed")

if __name__ == "__main__":
    main()
