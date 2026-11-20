
import pandas as pd
from datetime import datetime, timedelta

# ==========================================
# LOGIN ATTEMPT CONTROL SYSTEM
# ==========================================

MAX_ATTEMPTS = 5
LOCK_DURATION = 15

USERS = {
    "admin": "Admin@123",
    "testuser": "Test@123"
}

FAILED_ATTEMPTS = {}
IP_FAILED_ATTEMPTS = {}

LOCKED_UNTIL = {}
IP_LOCKED_UNTIL = {}


# ==========================================
# SECURITY AUDIT LOG
# ==========================================

def log_event(message):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("security_audit.log", "a") as file:
        file.write(f"[{timestamp}] {message}\n")


# ==========================================
# DATASET ANALYSIS
# ==========================================

def analyze_dataset():

    print("\n========== DATASET ANALYSIS ==========")

    try:
        df = pd.read_csv("cyber_login_attempts.csv")

        failed = df[df["Result"] == "Failure"]

        print("Total Login Attempts:", len(df))
        print("Successful Logins:",
              len(df[df["Result"] == "Success"]))
        print("Failed Logins:", len(failed))

        print("\nTop Failed Usernames:")
        print(failed["Username"].value_counts().head(10))

        print("\nTop Failed IP Addresses:")
        print(failed["SourceIP"].value_counts().head(10))

    except FileNotFoundError:
        print("[!] CSV dataset not found!")

    except Exception as error:
        print("[!] Dataset Error:", error)


# ==========================================
# CHECK LOCK STATUS
# ==========================================

def check_lock(lock_dict, key):

    current_time = datetime.now()

    if key in lock_dict:

        if current_time < lock_dict[key]:

            remaining = lock_dict[key] - current_time

            print("[!] ACCESS BLOCKED!")

            print("Try again after:",
                  int(remaining.total_seconds()), "seconds")

            return True

        else:

            del lock_dict[key]

            print("[+] Lock period expired.")

    return False


# ==========================================
# AUTHENTICATION SYSTEM
# ==========================================

def authenticate(username, password, ip_address):

    # Check IP lockout
    if check_lock(IP_LOCKED_UNTIL, ip_address):

        log_event(
            f"Blocked IP access | IP: {ip_address}"
        )

        return False

    # Check username lockout
    if check_lock(LOCKED_UNTIL, username):

        log_event(
            f"Blocked account access | User: {username} | IP: {ip_address}"
        )

        return False

    # Check username
    if username not in USERS:

        print("[!] Invalid username or password.")
        return False

    # Initialize counters
    FAILED_ATTEMPTS.setdefault(username, 0)
    IP_FAILED_ATTEMPTS.setdefault(ip_address, 0)

    # Verify password
    if USERS[username] == password:

        print("\n[+] LOGIN SUCCESSFUL!")
        print("Welcome,", username)

        FAILED_ATTEMPTS[username] = 0
        IP_FAILED_ATTEMPTS[ip_address] = 0

        log_event(
            f"Successful login | User: {username} | IP: {ip_address}"
        )

        return True

    # Wrong password
    FAILED_ATTEMPTS[username] += 1
    IP_FAILED_ATTEMPTS[ip_address] += 1

    user_count = FAILED_ATTEMPTS[username]
    ip_count = IP_FAILED_ATTEMPTS[ip_address]

    print("\n[!] LOGIN FAILED!")

    print("Username Failed Attempts:",
          user_count, "/", MAX_ATTEMPTS)

    print("IP Failed Attempts:",
          ip_count, "/", MAX_ATTEMPTS)

    log_event(
        f"Failed login | User: {username} | IP: {ip_address}"
    )

    current_time = datetime.now()

    # Username-based lockout
    if user_count >= MAX_ATTEMPTS:

        LOCKED_UNTIL[username] = (
            current_time + timedelta(minutes=LOCK_DURATION)
        )

        print("\n[!] ACCOUNT LOCKED FOR 15 MINUTES!")

        log_event(
            f"ACCOUNT LOCKED | User: {username} | "
            f"IP: {ip_address} | Duration: 15 minutes"
        )

    # IP-based lockout
    if ip_count >= MAX_ATTEMPTS:

        IP_LOCKED_UNTIL[ip_address] = (
            current_time + timedelta(minutes=LOCK_DURATION)
        )

        print("\n[!] IP ADDRESS BLOCKED FOR 15 MINUTES!")

        log_event(
            f"IP BLOCKED | IP: {ip_address} | Duration: 15 minutes"
        )

    return False


# ==========================================
# BRUTE FORCE SIMULATION
# ==========================================

def simulate_brute_force():

    print("\n========== BRUTE FORCE SIMULATION ==========")

    test_username = "testuser"
    test_ip = "203.0.113.10"

    print("Target Account:", test_username)
    print("Source IP:", test_ip)

    print("\nSimulating 5 wrong password attempts...\n")

    for attempt in range(1, MAX_ATTEMPTS + 1):

        print(f"\nAttempt {attempt}:")

        authenticate(
            test_username,
            "WrongPassword123",
            test_ip
        )

    print("\n========== SIMULATION RESULT ==========")

    if test_username in LOCKED_UNTIL:
        print("[+] ACCOUNT LOCKOUT: SUCCESS")

    if test_ip in IP_LOCKED_UNTIL:
        print("[+] IP RATE LIMITING: SUCCESS")

    print("[+] Brute force simulation completed.")


# ==========================================
# MAIN MENU
# ==========================================

def main():

    analyze_dataset()

    while True:

        print("\n" + "=" * 45)
        print("       LOGIN SECURITY SYSTEM")
        print("=" * 45)

        print("1. Login")
        print("2. Simulate Brute Force Attack")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            username = input("Enter username: ")
            password = input("Enter password: ")
            ip_address = input("Enter source IP address: ")

            authenticate(username, password, ip_address)

        elif choice == "2":

            simulate_brute_force()

        elif choice == "3":

            print("\n[+] Exiting Login Security System.")
            break

        else:

            print("[!] Invalid choice. Try again.")


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":
    main()
