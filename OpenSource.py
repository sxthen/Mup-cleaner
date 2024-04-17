import os
import shutil
import tempfile
import time

# Функция для очистки временных файлов пользователя
def clean_user_temp_files():
    temp_dir = tempfile.gettempdir()
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
            except Exception as e:
                print(f"Failed to delete {file}: {e}")

# Функция для очистки временных файлов пользователя (%temp%)
def clean_user_env_temp_files():
    temp_dir = os.getenv("TEMP")
    if temp_dir:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except Exception as e:
                    print(f"Failed to delete {file}: {e}")

# Функция для очистки недавних файлов
def clean_recent_files():
    recent_dir = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Recent")
    for root, dirs, files in os.walk(recent_dir):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
            except Exception as e:
                print(f"Failed to delete {file}: {e}")

# Функция для очистки файлов cookie
def clean_cookies():
    cookie_dir = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Cookies")
    for root, dirs, files in os.walk(cookie_dir):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
            except Exception as e:
                print(f"Failed to delete {file}: {e}")

# Функция для очистки Prefetch
def clean_prefetch():
    prefetch_dir = os.path.join(os.getenv("SystemRoot"), "Prefetch")
    for root, dirs, files in os.walk(prefetch_dir):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
            except Exception as e:
                print(f"Failed to delete {file}: {e}")

def clear_screen():
    # Очистка экрана консоли в Windows
    os.system('cls')

def main():
    while True:
        clear_screen()

        print("Select actions to perform:")
        print("1. Clean user's temporary files")
        print("2. Clean user's environment temporary files")
        print("3. Clean recent files")
        print("4. Clean cookies")
        print("5. Clean Prefetch")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            clean_user_temp_files()
            print("User's temporary files cleaned successfully.")
        elif choice == "2":
            clean_user_env_temp_files()
            print("User's environment temporary files cleaned successfully.")
        elif choice == "3":
            clean_recent_files()
            print("Recent files cleaned successfully.")
        elif choice == "4":
            clean_cookies()
            print("Cookies cleaned successfully.")
        elif choice == "5":
            clean_prefetch()
            print("Prefetch files cleaned successfully.")
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

        time.sleep(3)  # Задержка в 3 секунды

if __name__ == "__main__":
    main()
