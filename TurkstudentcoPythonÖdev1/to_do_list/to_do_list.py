import os

class Task:
    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed

    def __str__(self):
        status = "Tamamlandı" if self.completed else "Tamamlanmadı"
        return f"{self.name} - {status}"


class TaskManager:
    def __init__(self, file_path="tasks.txt"):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r") as file:
            tasks = []
            for line in file:
                name, completed = line.strip().split("|")
                tasks.append(Task(name, completed == "True"))
            return tasks

    def save_tasks(self):
        with open(self.file_path, "w") as file:
            for task in self.tasks:
                file.write(f"{task.name}|{task.completed}\n")

    def add_task(self, name):
        self.tasks.append(Task(name))
        self.save_tasks()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()

    def delete_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task.completed]
        self.save_tasks()

    def display_tasks(self):
        print("\nGörev Listesi:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")


def main():
    manager = TaskManager()
    while True:
        print("\n1. Görev Ekle\n2. Görevi Tamamla\n3. Tamamlananları Sil\n4. Görevleri Görüntüle\n5. Çıkış")
        choice = input("Seçiminiz: ")
        if choice == "1":
            name = input("Görev adı: ")
            manager.add_task(name)
        elif choice == "2":
            manager.display_tasks()
            index = int(input("Tamamlanacak görev numarası: ")) - 1
            manager.complete_task(index)
        elif choice == "3":
            manager.delete_completed_tasks()
        elif choice == "4":
            manager.display_tasks()
        elif choice == "5":
            print("Çıkış yapılıyor.")
            break
        else:
            print("Geçersiz seçim!")


if __name__ == "__main__":
    main()
