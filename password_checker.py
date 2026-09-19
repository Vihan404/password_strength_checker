import re

def check_password_strength(password):
    """
    Evaluates the strength of a password based on length, 
    character variety, and composition.
    """
    score = 0
    suggestions = []

    # 1. Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("- Password is too short (Minimum 8 characters required)")

    # 2. Character type checks
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("- Missing uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("- Missing lowercase letters")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("- Missing numbers")

    if re.search(r"[ !@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("- Missing special characters (e.g., @, #, $)")

    # Determine strength level
    if score >= 5:
        strength = "Very Strong "
    elif score >= 3:
        strength = "Medium "
    else:
        strength = "Weak "

    return strength, score, suggestions

def main():
    print("--- Password Strength Checker ---")
    user_input = input("Enter a password to test: ")
    
    strength, score, hints = check_password_strength(user_input)
    
    print(f"\nResult: {strength}")
    print(f"Score: {score}/6")
    
    if hints:
        print("\nSuggestions to improve your password:")
        for hint in hints:
            print(hint)
    else:
        print("\nPerfect! Your password is secure. ")

if __name__ == "__main__":
    main()
