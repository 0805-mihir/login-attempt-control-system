# Login Attempt Control System

## Project Overview

The **Login Attempt Control System** is a Python-based cybersecurity project developed to monitor login activities and prevent unauthorized access caused by repeated incorrect password attempts.

The system tracks failed login attempts using usernames and IP addresses. After five failed login attempts, the account is locked and the corresponding IP address is blocked for 15 minutes.

It also maintains a security audit log and provides a brute-force attack simulation feature to test the implemented security mechanisms.

## Project Objectives

- Monitor successful and failed login attempts.
- Detect repeated incorrect password attempts.
- Prevent brute-force login attacks.
- Lock user accounts after five failed attempts.
- Block IP addresses after five failed attempts.
- Apply a 15-minute lockout period.
- Maintain security audit logs.
- Analyze login activity using a CSV dataset.

## Features

- **User Authentication:** Verifies usernames and passwords.
- **Failed Login Tracking:** Counts failed attempts for each username and IP address.
- **Account Lockout:** Automatically locks an account after five failed login attempts.
- **IP-Based Blocking:** Blocks an IP address after five failed attempts.
- **15-Minute Lockout:** Temporarily blocks accounts and IP addresses.
- **Brute-Force Simulation:** Simulates repeated incorrect login attempts.
- **Security Audit Logging:** Records login activities and security events.
- **Dataset Analysis:** Analyzes login records and identifies suspicious usernames and IP addresses.

## Technologies Used

- Python 3.12
- Pandas
- CSV Dataset
- DateTime Module
- Visual Studio Code

## Project Structure

```text
Login-Attempt-Control-System/
│
├── login_control.py
├── cyber_login_attempts.csv
├── security_audit.log
├── test_logs.txt
├── README.md
└── Login_Attempt_Control_System_Report.pdf
```

## Installation

### 1. Install Python

Install Python 3.12 or above on your system.

### 2. Install Required Library

Open the terminal and execute:

```bash
pip install pandas
```

### 3. Clone the Repository

```bash
git clone https://github.com/0805-mihir/login-attempt-control-system.git
```

### 4. Open the Project Folder

```bash
cd login-attempt-control-system
```

## How to Run

Execute the following command in the terminal:

```bash
python login_control.py
```

## Demo Login Credentials

The project uses predefined demo credentials.

| Username | Password |
|---|---|
| admin | Admin@123 |
| testuser | Test@123 |

## Main Menu

The program provides the following options:

1. Login
2. Simulate Brute Force Attack
3. Exit

## Dataset Analysis

The project uses `cyber_login_attempts.csv` to analyze login activities.

Dataset analysis results:

| Parameter | Result |
|---|---:|
| Total Login Attempts | 500 |
| Successful Logins | 353 |
| Failed Logins | 147 |
| Unique Usernames | 46 |
| Unique IP Addresses | 201 |

The analysis identifies usernames and IP addresses with the highest number of failed login attempts.

## Security Mechanism

The system applies the following security rules:

- Maximum Failed Attempts: 5
- Account Lockout Duration: 15 Minutes
- IP Blocking Duration: 15 Minutes

When the failed login count reaches five, the system locks the account and blocks the associated IP address for 15 minutes.

## Testing

The project was tested using different test cases.

| Test Case | Result |
|---|---|
| CSV Dataset Analysis | PASS |
| Successful Login | PASS |
| Invalid Password Detection | PASS |
| Account Lockout | PASS |
| IP-Based Blocking | PASS |
| Brute-Force Simulation | PASS |
| Security Audit Logging | PASS |
| Repeated Access Prevention | PASS |

Detailed test results are available in `test_logs.txt`.

## Security Audit Logging

The system records security events in the `security_audit.log` file.

The log includes:

- Successful login attempts.
- Failed login attempts.
- Account lockout events.
- IP blocking events.
- Further access attempts from blocked IP addresses.

## Limitations

- Failed attempt counters are stored in memory and reset when the program restarts.
- The project uses predefined demo credentials.
- Passwords are stored as plain text in the demonstration code.
- The system is designed as a local Python application.
- Advanced database-based authentication and production-level rate limiting are not implemented.

## Future Enhancements

- Implement secure password hashing.
- Integrate database-based user management.
- Develop an administrator dashboard.
- Add email alerts for suspicious login activities.
- Implement advanced rate-limiting techniques.
- Add graphical security reports.

## Project Report

The detailed project report is included in:

`Login_Attempt_Control_System_Report.pdf`

## Conclusion

The Login Attempt Control System demonstrates basic cybersecurity techniques for protecting user accounts against repeated unauthorized login attempts.

The project successfully implements login authentication, failed attempt tracking, account lockout, IP-based blocking, brute-force simulation, dataset analysis, and security audit logging.

It provides practical knowledge of Python programming and important cybersecurity concepts.

## Author

**Mihir Koshti**

B.E. Computer Engineering

**Project Organization:** Workora

**Project Domain:** Cybersecurity
