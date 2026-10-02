import string

# Cтворює текстовий файл TF7_1 із символьних рядків різної довжини
def create_file():
    text = """Це перший символьний рядок, який містить різні слова.
Тут є слова з подвоєнням: аллея, роздоріжжя, Ганна, book, apple, та суддя!
А також звичайні слова без подвоєнь, розділені комами, крапками та тире.
І ще один тестовий рядок для перевірки."""

    while True:
        print("1 - написати власний рядок.\n" \
            "2 - вибрати рядок за замовчуванням.\n" \
            "Ваш вибір: ", end="")
        choice = input()

        if choice == '1':
            text = input("Введіть ваш текст:\n")
            break  
        elif choice == '2':
            break  
        else:
            print("\nПомилка: Некоректний вибір. Будь ласка, введіть 1 або 2.\n")

    try:
        file1 = open("TF7_1.txt", "w", encoding="utf-8")
        file1.write(text)
        file1.close()
        print("Файл TF7_1.txt успішно створено.")
    except IOError:
        print("Помилка під час створення файлу TF7_1.txt")

# Читає вміст файлу TF7_1, знаходить слова з подвоєнням букв і записує їх у файл TF7_2 по одному в рядок
def process_files():
    try:
        file1 = open("TF7_1.txt", "r", encoding="utf-8")
        content = file1.read()
        file1.close()
    except IOError:
        print("Помилка під час відкриття файлу TF7_1.txt")
        return

    # Видалення розділових знаків
    content_clean = content.translate(str.maketrans('', '', string.punctuation))
    
    words = content_clean.split()
    double_letter_words = []

    for word in words:
        for i in range(len(word) - 1):
            if word[i] == word[i+1]:
                double_letter_words.append(word)
                break

    try:
        file2 = open("TF7_2.txt", "w", encoding="utf-8")
        if not double_letter_words:
            print("Слів з подвоєнням букв немає.\n")
            file2.write("Слів з подвоєнням букв немає.")
        else:
            for word in double_letter_words:
                file2.write(word + "\n")
        file2.close()
        print("Результат записано у TF7_2.txt.")
    except IOError:
        print("Помилка під час запису у файл.")


# Виклик функцій
create_file()
process_files()

# Для Міхальова М. О.
# Додати функцію яка читає вміст файлу TF7_2 і друкує його по рядках в консоль.

def print_second_file():
    try:
        file2 = open("Практика 4/TF7_2.txt", "r", encoding="utf-8")
        for line in file2:
            print(line, end="")
    except Exception as e: 
        print(f"Помилка під час відкриття файлу TF7_2.txt - {e}")
        return

print_second_file()