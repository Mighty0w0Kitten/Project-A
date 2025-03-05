# modules/notes_manager.py
class NotesManager:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)
        print(f"Заметка добавлена: {note}")

    def list_notes(self):
        if not self.notes:
            print("Заметок нет.")
        else:
            print("Список заметок:")
            for note in self.notes:
                print(note)
