class Task(): # Создание класса Task (задача)
    def init(self, description, term, status): # атрибуты: описание, срок, статус (выполнено, нет)
        self.description = description # создание характеристики (атрибута)
        self.term = term
        self.status = status

    def add_task(self, col): #  добавление задачи
        print(f'{self.description} добавлена задача')
        self.description += 'не выполнена'

    def completing_task(self): # отметка выполнения задачи
        print(f'{self.term} выполнена задача')
        self.description = 'выполнена'

    def status_task(self): #  статус задачи
        if self.description == 'выполнена':
            self.status = 'выполнена'
        else:
            self.status = 'не выполнена'
        print(f'{self.status} статус задачи')

    def tasks_not(self, col): # количество не выполненных задач
        for i in range(self.description):
            if self.description == 'не выполнена':
                col +=1
        print(col)
    


