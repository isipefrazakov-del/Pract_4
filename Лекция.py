import json

country_data = {
    "название": "Германия",
    "столица": "Берлин",
    "население": 83200000
}

# Сохранение в JSON-файл
with open('country.json', 'w', encoding='utf-8') as file:
    json.dump(country_data, file, ensure_ascii=False, indent=2)

# Чтение файла country.json
try:
    with open('country.json', 'r', encoding='utf-8') as file:
        country_data = json.load(file)
    
    # Добавление нового ключа "язык"
    country_data['язык'] = 'французский'
    
    # Сохранение изменений обратно в файл
    with open('country.json', 'w', encoding='utf-8') as file:
        json.dump(country_data, file, ensure_ascii=False, indent=2)
    
    print("Файл country.json успешно обновлен.")
    print("Добавлен ключ 'язык' со значением 'французский'")
    print("Обновленные данные:")
    print(json.dumps(country_data, ensure_ascii=False, indent=2))
    
except FileNotFoundError:
    print("Файл country.json не найден. Сначала создайте его через задачу 2.")
except Exception as e:
    print(f"Произошла ошибка: {e}")

    