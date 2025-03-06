from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Функция для обучения модели
def train_model(data):
    # Для простоты, мы используем фиктивные данные для обучения
    X = [[1, 2], [2, 3], [3, 4], [4, 5]]  # Данные для обучения
    y = [0, 1, 0, 1]  # Метки классов

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)  # Обучаем модель

    y_pred = model.predict(X_test)  # Прогнозируем

    accuracy = accuracy_score(y_test, y_pred)
    print(f"Точность модели: {accuracy * 100:.2f}%")

    return model
