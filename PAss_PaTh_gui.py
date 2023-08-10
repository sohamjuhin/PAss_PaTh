import tkinter as tk
from tkinter import ttk

class PasswordStrengthTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Tester")

        self.password_label = ttk.Label(root, text="Enter Password:")
        self.password_label.pack(pady=10)

        self.password_entry = ttk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        self.strength_label = ttk.Label(root, text="")
        self.strength_label.pack(pady=10)

        self.test_button = ttk.Button(root, text="Test Strength", command=self.test_strength)
        self.test_button.pack()

    def test_strength(self):
        password = self.password_entry.get()
        strength = self.calculate_strength(password)
        self.display_strength(strength)

    def calculate_strength(self, password):
        length_score = min(len(password) // 4, 5)
        upper_score = 1 if any(c.isupper() for c in password) else 0
        lower_score = 1 if any(c.islower() for c in password) else 0
        digit_score = 1 if any(c.isdigit() for c in password) else 0
        symbol_score = 1 if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/~" for c in password) else 0

        total_score = length_score + upper_score + lower_score + digit_score + symbol_score
        return total_score

    def display_strength(self, strength):
        if strength >= 5:
            strength_text = "Strong"
        elif strength >= 3:
            strength_text = "Moderate"
        else:
            strength_text = "Weak"

        self.strength_label.config(text=f"Password Strength: {strength_text}")

if __name__ == "__main__":
    root = tk.Tk()
    strength_tester = PasswordStrengthTester(root)
    root.mainloop()
