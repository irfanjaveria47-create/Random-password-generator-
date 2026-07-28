import random
import string

def generate_password(length, use_special):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    if use_special:
        all_characters = lowercase + uppercase + digits + special
    else:
        all_characters = lowercase + uppercase + digits

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]

    if use_special:
        password.append(random.choice(special))

    while len(password) < length:
        password.append(random.choice(all_characters))

    random.shuffle(password)
    return "".join(password)

print("=" * 45)
print("      RANDOM PASSWORD GENERATOR")
print("=" * 45)

while True:
    try:
        length = int(input("Enter password length (minimum 4): "))

        if length < 4:
            print("Password length must be at least 4.\n")
            continue

        choice = input("Include special characters? (yes/no): ").strip().lower()
        use_special = choice in ["yes", "y"]

        password = generate_password(length, use_special)

        print("\nGenerated Password:")
        print(password)

        again = input("\nGenerate another password? (yes/no): ").strip().lower()

        if again not in ["yes", "y"]:
            print("\nThank you for using the Random Password Generator!")
            break

        print()

    except ValueError:
        print("Please enter a valid number.\n")
