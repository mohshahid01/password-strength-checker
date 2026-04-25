from checker.strength import check_strength

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter password: ")

    strength, entropy = check_strength(password)

    print(f"\nStrength: {strength}")
    print(f"Entropy: {entropy} bits")

if __name__ == "__main__":
    main()
    