from mimetypes import inited

import bcrypt
import os

import bcrypt

def hash_password(plain_text_password):
    password_bytes = plain_text_password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')

import bcrypt
def hash_password(p):
    return bcrypt.hashpw(p.encode(), bcrypt.gensalt()).decode()
USER_DATA_FILE = "users.txt"

import os, bcrypt

USER_DATA_FILE = "users.txt"

def hash_password(p):
    return bcrypt.hashpw(p.encode(), bcrypt.gensalt()).decode()

def register_user(username, password):
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            if any(line.startswith(username + ",") for line in f):
                return False
    with open(USER_DATA_FILE, "a") as f:
        f.write(f"{username},{hash_password(password)}\n")
    return True

def login_user(username, password):
    try:
        with open("users.txt", "r") as file:
            for line in file:
                user, pwd = line.strip().split(",")
                if user == username and pwd == password:
                    return True
        return False
    except FileNotFoundError:
        return False

def validate_username(u):
    return (len(u) >= 3 and u.isalnum(), "Invalid username")

def validate_password(p):
    return (len(p) >= 6 and any(c.isdigit() for c in p), "Weak password")


def display_menu():
    """Displays the main menu options."""
    print("\n" + "=" * 50)
    print("  MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print("  Secure Authentication System")
    print("=" * 50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-" * 50)

USERS_FILE = "users.txt"

def valid_user(u):  return len(u) >= 3 and u.isalnum()
def valid_pass(p):  return len(p) >= 6 and any(c.isdigit() for c in p)

def load_users():
    try:
        with open(USERS_FILE) as f:
            return dict(line.strip().split(",", 1) for line in f if "," in line)
    except FileNotFoundError:
        return {}

def save_user(u, p):
    with open(USERS_FILE, "a") as f: f.write(f"{u},{p}\n")

def register_flow():
    u = input("New username: ").strip()
    p = input("New password: ").strip()
    if not valid_user(u):  return print("Invalid username (min 3, letters/numbers).")
    if not valid_pass(p):  return print("Weak password (min 6 with a digit).")
    users = load_users()
    if u in users:         return print("Username already exists.")
    save_user(u, p); print("Registered!")

def login_flow():
    u = input("Username: ").strip()
    p = input("Password: ").strip()
    print("Welcome back Alice!" if load_users().get(u) == p else "Login failed")

def main():
    while True:
        print("\n1) Register  2) Login  3) Exit")
        c = input("Choose: ").strip()
        if   c == "1": register_flow()
        elif c == "2": login_flow()
        elif c == "3": print("Bye!"); break
        else: print("Invalid option")

if __name__ == "__main__":
    main()




