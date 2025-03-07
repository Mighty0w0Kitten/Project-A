# Импортируем модули из папки modules
from modules.data_loader import load_data
from modules.nlp_utils import preprocess_text
from modules.model import train_model
from modules.query_parser import parse_query

# Основная логика программы
def main():
    # Пример запроса от пользователя
    user_query = input("Введите запрос: ")

# Обрабатываем запрос
    response = parse_query(user_query)

    # Выводим ответ
    print(response)

    # Загружаем данные
    # data = load_data('data.txt')  # Функция для загрузки данных

    # Обрабатываем текст
    #processed_data = preprocess_text(data)  # Обрабатываем текст

    # Обучаем модель
    # model = train_model(processed_data)  # Обучаем модель

    #print("Модель успешно обучена!")

if __name__ == "__main__":
    main()
