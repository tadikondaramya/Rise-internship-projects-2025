import random
import string
import pyperclip  # install with: pip install pyperclip
from datetime import datetime

# Optional characters to exclude for better readability
AMBIGUOUS_CHARS = 'O0Il1|'

def get_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    score = sum([has_upper, has_lower, has_digit, has_special])

    if length >= 12 and score >= 3:
        return "Strong"
    elif length >= 8 and score >= 2:
        return "Moderate"
    else:
        return "Weak"

def generate_password(length, use_digits, use_special, avoid_ambiguous):
    if length < 4:
        raise ValueError("Password length must be at least 4")

    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    if avoid_ambiguous:
        chars = ''.join(c for c in chars if c not in AMBIGUOUS_CHARS)

    # Enforce at least one character from each selected category
    password = []
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))

    while len(password) < length:
        password.append(random.choice(chars))

    random.shuffle(password)
    return ''.join(password)

def main():
    print("🔐 Enhanced Password Generator")
    length = int(input("Enter password length (min 4): "))
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    avoid_ambiguous = input("Avoid ambiguous characters (O, 0, l, 1, etc)? (y/n): ").lower() == 'y'
    num_passwords = int(input("How many passwords to generate?: "))
    save_option = input("Save passwords to file? (y/n): ").lower() == 'y'
    copy_clipboard = input("Copy last password to clipboard? (y/n): ").lower() == 'y'

    passwords = []
    for _ in range(num_passwords):
        pwd = generate_password(length, use_digits, use_special, avoid_ambiguous)
        strength = get_strength(pwd)
        print(f"\n🔑 Password: {pwd}")
        print(f"   Strength: {strength}")
        passwords.append((pwd, strength))

    if save_option:
        with open("passwords_saved.txt", "a") as f:
            for pwd, strength in passwords:
                f.write(f"{datetime.now()} - {pwd} - Strength: {strength}\n")
        print("\n📁 Passwords saved to passwords_saved.txt")

    if copy_clipboard and passwords:
        try:
            pyperclip.copy(passwords[-1][0])
            print(f"📋 Last password copied to clipboard: {passwords[-1][0]}")
        except Exception:
            print("⚠️ Could not copy to clipboard. pyperclip not working.")

if __name__ == "__main__":
    main()
