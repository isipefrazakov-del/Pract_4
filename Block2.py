import json
import csv
import os


test_json = {
"Имя": "Мария Петрова",
"Возраст": "23",
"Город": "Казань"
}

file = open('test_json.json', 'w', encoding='utf-8')
json.dump(test_json, file, ensure_ascii=False, indent=2)
file.close()




try:
    # Открываем и читаем JSON файл
    json_file = open('test_json.json', 'r', encoding='utf-8')
    intern_data = json.load(json_file)
    json_file.close()
    
    # Подготавливаем данные для CSV
    csv_row = {
        'Имя': intern_data['Имя'],
        'Возраст': intern_data['Возраст'],
        'Город': intern_data['Город'],
        'Должность': 'Стажёр',
        'Зарплата': '50000'
    }
    
    # Проверяем, существует ли файл employees_with_salary.csv
    file_exists = os.path.exists('employees_with_salary.csv')
    
    # Открываем CSV файл для добавления данных
    csv_file = open('employees_with_salary.csv', 'a', encoding='utf-8', newline='')
    
    # Создаем объект для записи CSV
    writer = csv.DictWriter(csv_file, fieldnames=['Имя', 'Возраст', 'Город', 'Должность', 'Зарплата'])
    
    # Если файл новый - пишем заголовок
    if not file_exists:
        writer.writeheader()
    
    # Записываем данные стажера
    writer.writerow(csv_row)
    
    # Закрываем файл
    csv_file.close()
    
    # Выводим результат
    if file_exists:
        print(f"✅ Данные стажера добавлены в существующий файл employees_with_salary.csv")
    else:
        print(f"✅ Создан новый файл employees_with_salary.csv с данными стажера")
    
    print(f"\nДобавлена запись:")
    print(f"  Имя: {csv_row['Имя']}")
    print(f"  Возраст: {csv_row['Возраст']}")
    print(f"  Город: {csv_row['Город']}")
    print(f"  Должность: {csv_row['Должность']}")
    print(f"  Зарплата: {csv_row['Зарплата']}")

except FileNotFoundError:
    print("❌ Файл test_json.json не найден!")
    print("Создайте файл test_json.json со следующим содержимым:")
    print('''
{
  "Имя": "Иван Иванов",
  "Возраст": "22",
  "Город": "Москва"
}
    ''')

except json.JSONDecodeError:
    print("❌ Ошибка: файл test_json.json содержит некорректный JSON")

except Exception as error:
    print(f"❌ Произошла ошибка: {error}")