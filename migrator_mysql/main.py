import getpass
from functions  import create_user
from functions import generate_password  # Импортируем функцию генерации пароля

def main():
    print("⚙️  Конфигурация миграции пользователей MySQL/MariaDB")

    # Сервер А (источник данных)
    host_a = input("Введите хост сервера A (источник): ")
    admin_user_a = input("Имя администратора (Enter для 'root'): ") or "root"
    admin_password_a = getpass.getpass("Введите пароль администратора сервера A: ")
    database_a = input("Введите имя базы данных на сервере A: ")

    # Создаем пользователя sender на сервере A
    sender_password = "StaticPassword123!"
    create_user(host_a, admin_user_a, admin_password_a, "sender", sender_password, database_a)
    
    # Сервер B (куда переносим данные)
    host_b = input("\nВведите хост сервера B (назначение): ")
    admin_user_b = input("Имя администратора (Enter для 'root'): ") or "root"
    admin_password_b = getpass.getpass("Введите пароль администратора сервера B: ")
    
    # Запрашиваем имя нового пользователя и генерируем пароль
    new_user_b = input("Введите имя нового пользователя на сервере B: ")
    new_password_b = generate_password()  # Теперь используем импортированную функцию
    database_b = input("Введите имя базы данных на сервере B: ")

    print(f"\n✅ Сгенерирован пароль для {new_user_b}: {new_password_b}")
    
    # Создаем нового пользователя на сервере B
    create_user(host_b, admin_user_b, admin_password_b, new_user_b, new_password_b, database_b)

    print("\n🎉 Миграция пользователей завершена!")

if __name__ == "__main__":
    main()
