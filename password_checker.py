import re

def check_password_strength(password):
    """Assess the strength of a password and provide feedback."""
    
    feedback = []
    
    # Check password length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters.")
    elif len(password) < 12:
        feedback.append("Password is somewhat short. Consider using at least 12 characters.")
    
    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should include at least one uppercase letter.")
    
    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        feedback.append("Password should include at least one lowercase letter.")
    
    # Check for numbers
    if not re.search(r'[0-9]', password):
        feedback.append("Password should include at least one number.")
    
    # Check for special characters
    if not re.search(r'[@#$%^&+=!]', password):
        feedback.append("Password should include at least one special character.")
    
    # Assess overall strength
    if not feedback:
        return "Password is strong."
    else:
        return "\n".join(feedback)

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength_feedback = check_password_strength(password)
    print("\nPassword Strength Assessment:")
    print(strength_feedback)
