from modules.email_manager import EmailManager
from modules.file_searcher import FileSearcher
from modules.utils import NotesManager
from modules.voice_assistant import VoiceAssistant

class MyAIHelper:
    def __init__(self):
        # Инициализируем все модули
        self.email_manager = EmailManager()
        self.file_searcher = FileSearcher()
        self.voice_assistant = VoiceAssistant()
        self.notes_manager = NotesManager()  # Подключаем модуль для заметок

    def run(self):
        # Основной цикл работы помощника
        print("AI помощник запущен...")
        while True:
            command = input("Что нужно сделать? (или 'exit' для выхода): ")
            if command == 'exit':
                break
            self.process_command(command)

    def process_command(self, command):
        # Обработка команд и взаимодействие с модулями
        if "email" in command:
            self.email_manager.handle_email(command)
        elif "search" in command:
            self.file_searcher.handle_search(command)
        elif "voice" in command:
            self.voice_assistant.handle_voice(command)
        elif "note" in command:
            self.notes_manager.add_note(command)  # Обработка команд для заметок
        else:
            print("Команда не распознана!")

if __name__ == "__main__":
    ai_helper = MyAIHelper()
    ai_helper.run()
