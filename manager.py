import json

class PhotonCell(dict):
    def __init__(self, dict):
        super().__init__(**dict)

class PhotonDB:
    def __init__(self, file_path, autosave=False):
        self.autosave = autosave
        self.file_path = file_path
        self.content = [PhotonCell(cell) for cell in self.load_cells_from_file()]
 
    def load_cells_from_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def save(self, file_path=None):
        if not file_path:
            file_path = self.file_path
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(self.content, file, default=lambda x: dict(x), indent=4)

    def autosave_decorator(func):
        def func_wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            
            if self.autosave:
                self.save()

            return result

        return func_wrapper

    def get(self, **kwargs):
        result = []
        for cell in self.content:
            atende_aos_critérios = all(cell.get(key) == value for key, value in kwargs.items())
            if atende_aos_critérios:
                result.append(cell)
        return result

    @autosave_decorator
    def remove(self, **kwargs):
        self.content = [cell for cell in self.content if not all(cell.get(key) == value for key, value in kwargs.items())]

    @autosave_decorator
    def add(self, **kwargs):
        self.content.append(kwargs)

    def __str__(self):
        return str([dict(cell) for cell in self.content])

if __name__ == '__main__':
    pdb = PhotonDB('db.json')
    pdb.add(name='Ryan')
    cell = pdb.get(name='Benfica')
    print(cell)