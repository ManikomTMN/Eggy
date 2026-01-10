import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("data/tasks.json")


class Task:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        return self.__dict__


def load_tasks():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    DATA_FILE.parent.mkdir(exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)
