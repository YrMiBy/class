class Task(): # Создание класса Task (задача)
    def init(self, description, term, status): # атрибуты: описание, срок, статус (выполнено, нет)
        self.description = description # создание характеристики (атрибута)
        self.term = term
        self.status = status

    def description_task(self): # функция добавление задачи
        print(f'{self.description} добавлена задача')
        self.description += 1

    def completing_task(self): # функция отметки выполнения задачи
        print(f'{self.term} выполнена задача')
        self.term -= 1
    def status_task(self): # функция статуса задачи
        print(f'{self.status} статус задачи')

    def info(self):
        print(f'добавлена задача - {self.description}')
        print(f'выполнена задача - {self.term}')
        print(f'статус задачи - {self.status}')


