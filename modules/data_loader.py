# Пример функции для загрузки данных
def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()  # Читаем весь текст из файла
