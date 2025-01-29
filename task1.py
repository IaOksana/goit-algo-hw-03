# Завдання 1

# Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, переміщає їх до нової директорії та сортує в піддиректорії, назви яких базуються на розширенні файлів.


# Також візьміть до уваги наступні умови:

# 1. Парсинг аргументів. Скрипт має приймати два аргументи командного рядка: шлях до вихідної директорії та 
# шлях до директорії призначення (за замовчуванням, якщо тека призначення не була передана, вона повинна бути 
# з назвою dist).

# 2. Рекурсивне читання директорій:
# Має бути написана функція, яка приймає шлях до директорії як аргумент.
# Функція має перебирати всі елементи у директорії.
# Якщо елемент є директорією, функція повинна викликати саму себе рекурсивно для цієї директорії.
# Якщо елемент є файлом, він має бути доступним для копіювання.

# 3. Копіювання файлів:
# Для кожного типу файлів має бути створений новий шлях у вихідній директорії, використовуючи розширення файлу 
# для назви піддиректорії.
# Файл з відповідним типом має бути скопійований у відповідну піддиректорію.

# 4. Обробка винятків. Код має правильно обробляти винятки, наприклад, помилки доступу до файлів або директорій.

# Завдання 1:

# 1. Парсинг аргументів. Скрипт приймає два аргументи командного рядка: шлях до вихідної директорії та шлях 
# до директорії призначення (за замовчуванням, якщо тека призначення не була передана, вона повинна бути 
# з назвою dist).

# 2. Рекурсивне читання директорій:
# Написана функція, яка приймає шлях до директорії як аргумент.
# Функція перебирає всі елементи у директорії.
# Якщо елемент є директорією, функція викликає саму себе рекурсивно для цієї директорії.
# Якщо елемент є файлом, він є обробленим для копіювання.

# 3. Копіювання файлів:
# Для кожного типу файлів створюється новий шлях у вихідній директорії, використовуючи розширення файлу для 
# назви піддиректорії.
# Файл з відповідним типом копіюється у відповідну піддиректорію.

# 4. Обробка винятків: код обробляє винятки, наприклад, помилки доступу до файлів або директорій.

# 5. Після виконання програми всі файли у вихідній директорії рекурсивно скопійовано в нову директорію та 
# розсортовано в піддиректорії за їх розширенням.

import os
from pathlib import Path
import argparse
import shutil


def parse_folder(source, dist):
    try:
        for element in source.iterdir():
            if element.is_dir():
                print(f"Parse folder: {element.name}")
                parse_folder(element, dist)
            if element.is_file():
                # Get file extension (without the dot)
                file_extension = element.suffix.lstrip(".") or "no_extension"

                # Define the destination subdirectory based on the extension
                destination_subdir = dist / file_extension

                # Ensure the subdirectory exists
                destination_subdir.mkdir(parents=True, exist_ok=True)

                # Define the destination file path
                destination_file = destination_subdir / element.name

                # Check if the file already exists
                if not destination_file.exists():
                    shutil.copy(element, destination_file)
                    print(f"Copied {element.name} to {destination_subdir}")
                else:
                    print(f"File {element.name} already exists in {destination_subdir}, skipping copy.")
    except PermissionError:
        print(f"🚫 Permission denied: Unable to access '{source}' or '{dist}'.")

    except FileNotFoundError:
        print(f"❌ Error: The source file '{source}' was not found.")

    except OSError as e:
        print(f"⚠️ OS Error: {e}")

    except Exception as e:
        print(f"🔥 Unexpected error: {e}")
        

def main(): #  command line example: python task1.py --source . --dist new_dist
    parser = argparse.ArgumentParser(description='Copying files sorted by extentions')
    parser.add_argument("--source", type=Path, required=True, help="Path to source folder")
    parser.add_argument("--dist", type=Path, default=Path('dist'), help="Path to dist folder")
    args = parser.parse_args()

    if os.path.exists(args.source):
        if not os.path.exists(args.dist):
            os.mkdir(args.dist)

        parse_folder(args.source, args.dist)        
    else:
        print("Please try with another valid path")


if __name__ == "__main__":
    main()