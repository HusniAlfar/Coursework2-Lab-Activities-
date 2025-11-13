# Week 7: Secure Authentication System

**Student Name:** Husni Alfar  
**Student ID:** M01002718  
**Course:** CST1510 – CW2 – CST1510 Programming For Data Communications and Networks

---

##  Project Description
A simple command-line authentication system that allows users to **register** and **log in** securely.  
The program validates inputs, stores user data in a file, and verifies credentials during login.

---

##  Features
- User **registration** with duplicate check  
- User **login** with password verification  
- **Input validation** for username and password  
- **File-based** data storage using `users.txt`  
- Simple, clean, and easy-to-run command-line interface  

---

##  Technical Implementation
- **Language:** Python 3  
- **Storage:** Plain text file (`users.txt`) with `username,password` pairs  
- **Validation:**  
  - Username: 3–20 characters, alphanumeric only  
  - Password: Minimum 6 characters, must include a number  
- **Login Logic:** Reads users from file and matches credentials  
- **Error Handling:** Handles missing file and invalid inputs gracefully  

---

## Example Usage
```bash
1) Register
2) Login
3) Exit
```
- Enter a username and password to register  
- Then log in using your credentials  

---

##  File Structure
```
Week7/
│
├── authy.py         # Main program file
├── users.txt        # User data file (auto-created)
├── Week07_LAB.pdf   # Lab instructions
└── README.md        # Documentation
```

---

##  How to Run
```bash
python authy.py
```

---

**Husni Alfar**
**M01002718**  
Middlesex University, CST1510 – Programming for Data Communications and Networks
