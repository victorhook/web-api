import json


class DB:

    def __init__(self, path):
        self.path = path
        if not self.path.exists():
            self.save([])

    def load(self):
        with open(self.path) as f:
            return json.load(f)

    def save(self, data):
        with open(self.path, 'w') as f:
            json.dump(list(set(data)), f, indent=4)
