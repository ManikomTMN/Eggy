from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QLineEdit, QDateEdit, QListWidgetItem
)
from PySide6.QtCore import Qt, QDate
from .models import Task, load_tasks, save_tasks

class TaskManager(QWidget):
    def __init__(self):
        super().__init__()
        self.tasks = load_tasks()
        self.list = QListWidget()

        self.input = QLineEdit()
        self.input.setPlaceholderText("New task")
        self.date = QDateEdit(QDate.currentDate())
        self.date.setCalendarPopup(True)

        add_btn = QPushButton("Add")
        del_btn = QPushButton("Delete")

        # Connect buttons — methods must exist in this class
        add_btn.clicked.connect(self.add_task)
        del_btn.clicked.connect(self.delete_task)

        top = QHBoxLayout()
        top.addWidget(self.input)
        top.addWidget(self.date)
        top.addWidget(add_btn)

        layout = QVBoxLayout(self)
        layout.addLayout(top)
        layout.addWidget(self.list)
        layout.addWidget(del_btn)

        self.list.itemChanged.connect(self.save_checked_state)

        self.refresh()

    def refresh(self):
        self.list.clear()
        for t in self.tasks:
            item_text = f"{t['title']} — {t['due_date']}"
            item = QListWidgetItem(item_text)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            state = Qt.Checked if t.get("done") else Qt.Unchecked
            item.setCheckState(state)
            self.list.addItem(item)

    def add_task(self):
        if not self.input.text():
            return
        task = Task(self.input.text(), self.date.date().toString())
        self.tasks.append(task.to_dict())
        save_tasks(self.tasks)
        self.input.clear()
        self.refresh()

    def delete_task(self):
        row = self.list.currentRow()
        if row >= 0:
            self.tasks.pop(row)
            save_tasks(self.tasks)
            self.refresh()

    def save_checked_state(self, item):
        index = self.list.row(item)
        if 0 <= index < len(self.tasks):
            self.tasks[index]['done'] = item.checkState() == Qt.Checked
            save_tasks(self.tasks)
