import nltk
from nltk.tokenize import word_tokenize

# Функция для предварительной обработки текста
def preprocess_text(text):
    nltk.download('punkt')  # Загружаем необходимые ресурсы NLTK

    # Токенизация текста
    tokens = word_tokenize(text)
    return tokens
