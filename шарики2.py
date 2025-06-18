class Node:
    """Узел односвязного списка для хранения цвета шарика."""
    def __init__(self, color):
        """Инициализация узла."""
        self.color = color  # Цвет шарика (целое число)
        self.next = None   # Указатель на следующий узел (изначально None)

    def __str__(self):
        """Возвращает строковое представление узла (цвет шарика)."""
        return str(self.color)


class LinkedList:
    """Односвязный список для представления линии шариков."""
    def __init__(self):
        """Инициализация списка."""
        self.head = None  # Голова списка (первый узел, изначально None)
        self.tail = None  # Хвост списка (последний узел, изначально None)
        self.size = 0     # Количество шариков в линии (изначально 0)

    def append(self, color):
        """Добавляет шарик заданного цвета в конец линии."""
        new_node = Node(color)  # Создаем новый узел с заданным цветом
        if self.head is None:
            # Если список пуст:
            self.head = new_node  # Новый узел становится головой
            self.tail = new_node  # И хвостом
        else:
            # Если в списке уже есть элементы:
            self.tail.next = new_node  # Добавляем новый узел в конец списка
            self.tail = new_node  # Обновляем хвост списка
        self.size += 1  # Увеличиваем размер списка

    def __len__(self):
        """Возвращает длину списка (количество шариков)."""
        return self.size

    def __str__(self):
        """Возвращает строковое представление линии шариков."""
        if self.head is None:
            # Если список пуст:
            return "Линия пуста"
        current = self.head  # Начинаем с головы списка
        result = ""           # Инициализируем пустую строку для результата
        while current:
            # Пока не дошли до конца списка:
            result += str(current.color) + " "  # Добавляем цвет текущего шарика в строку
            current = current.next              # Переходим к следующему шарику
        return result.strip()  # Возвращаем строку без лишних пробелов в начале и конце

    def destroy_chain(self, start, end):
        """Удаляет цепочку шариков, начиная с узла start и заканчивая узлом end."""
        destroyed_count = 0 # Инициализация счетчика удаленных узлов.
        if start is self.head:
            # Если удаляется цепочка в начале списка:
            if end.next is None:  # До конца списка
                self.head = None  # Список становится пустым
                self.tail = None  # Обнуляем указатель на хвост
                destroyed_count = self.size  # Все элементы удалены
                self.size = 0  # Размер списка равен 0
            else:
                # Если цепочка удаляется только в начале списка:
                self.head = end.next  # Новой головой становится элемент после цепочки
                destroyed_count = 0  # Обнуляем счетчик, т.к. нужно пересчитать
                current = start
                # Устанавливаем `current` на начало удаляемой цепочки (`start`).

                while current != end.next:
                    # Перебираем узлы от начала цепочки (`start`) до узла, следующего за концом цепочки (`end.next`).

                    destroyed_count += 1
                    # Увеличиваем счетчик удаленных узлов (`destroyed_count`) на каждом шаге.

                    current = current.next
                    # Переходим к следующему узлу в цепочке.

                self.size -= destroyed_count
                # Обновляем размер списка (`self.size`), вычитая количество удаленных узлов.

        else:
             # Удаление в середине списка или в конце
            current = self.head
             # Начинаем с головы списка.
            while current.next != start:
                current = current.next
                # Ищем узел, *предшествующий* началу удаляемой цепочки.

            current.next = end.next  # Перестраиваем связь:  предыдущий_узел.next = следующий_после_цепочки

            destroyed_count = 0 # Обнуляем счетчик удаленных узлов.
            current = start  # Начинаем с начала удаляемой цепочки.
            while current != end.next: # Итерируемся по узлам удаляемой цепочки.
                destroyed_count += 1 # Итерируемся по узлам удаляемой цепочки.
                if current == end:
                   break
                   # Прерываем цикл, если `current` достиг конца удаляемой цепочки.

                current = current.next # Переходим к следующему узлу в цепочке.
            if end.next == None:
                self.tail = current
                # Если удаляем до конца списка, обновляем указатель на хвост.
            self.size -= destroyed_count # Обновляем размер списка.

        return destroyed_count # Возвращаем количество удаленных узлов.


    def check_and_destroy(self):
        """Проверяет наличие цепочек и удаляет их, повторяя до тех пор, пока есть что удалять."""
        total_destroyed = 0  # Суммарное кол-во разрушенных шаров
        destroyed = True       # Флаг, показывающий, были ли уничтожены шары на текущей итерации
        while destroyed:       # Цикл повторяется, пока есть что уничтожать
            destroyed = False  # Сбрасываем флаг перед каждой итерацией
            destroyed_count = 0  # Инициализируем счетчик уничтоженных шариков на текущей итерации

            if self.head is None or self.head.next is None or self.head.next.next is None:
                # Если шаров меньше трех, то цепочки не существует, выходим
                return total_destroyed

            current = self.head   # Начинаем с головы списка
            start = self.head     # Начало текущей цепочки
            chain_length = 1      # Длина текущей цепочки

            while current.next:  # Пока не дошли до предпоследнего элемента
                if current.color == current.next.color:
                    # Если текущий и следующий шарики одного цвета, увеличиваем длину цепочки
                    chain_length += 1
                else:
                    # Иначе (цвет отличается):
                    if chain_length >= 3:
                        # Если цепочка достаточно длинная (>= 3 шаров):
                        destroyed_count += self.destroy_chain(start, current)  # Уничтожаем цепочку
                        total_destroyed += destroyed_count # Добавляем уничтоженные шары к общему количеству
                        destroyed = True # Устанавливаем флаг, что были разрушения
                        break # Прерываем цикл, чтобы начать проверку сначала
                    start = current.next  # Начинаем новую цепочку со следующего элемента
                    chain_length = 1       # Сбрасываем длину цепочки
                current = current.next  # Переходим к следующему шарику

            if not destroyed: # Если после цикла не было разрушений
                if chain_length >= 3:
                    # Проверяем, не заканчивается ли цепочка в конце списка
                    destroyed_count += self.destroy_chain(start, self.tail) # Уничтожаем цепочку в конце
                    total_destroyed += destroyed_count# Добавляем уничтоженные шары к общему количеству
                    destroyed = True# Устанавливаем флаг, что были разрушения
                break # Выходим из внешнего цикла, т.к. разрушений больше нет

        return total_destroyed # Возвращаем общее количество разрушенных шаров


def get_valid_input(prompt, data_type, validation_func=None):
    """Получает корректный ввод от пользователя с проверкой типа и дополнительной валидацией."""
    while True:
        try:
            value = data_type(input(prompt))  # Получаем ввод от пользователя и преобразуем к нужному типу
            if validation_func is None or validation_func(value):
                # Если нет функции валидации или ввод прошел валидацию:
                return value  # Возвращаем ввод
            else:
                # Иначе:
                print("Ошибка: Некорректный ввод. Пожалуйста, проверьте условия.")
        except ValueError:
            # Если ввод не может быть преобразован к нужному типу:
            print("Ошибка: Введите значение корректного типа.")
        except Exception as e:
            # Если произошла другая ошибка:
            print(f"Ошибка: {e}")


def main():
    """Основная функция программы."""
    print("=====Добро пожаловать в игру 'Шарики'!=====\n")
    print("Ваша цель: уничтожить цепочки из трех и более шариков одного цвета.\n")

    while True:  # Добавляем цикл для повторных игр
        num_balls = get_valid_input("Введите количество шариков в линии (максимум 100.000), или 'exit' для выхода: ",
                                   lambda x: int(x) if x.isdigit() else x,
                                   lambda x: (isinstance(x, int) and 1 <= x <= 100000) or x == 'exit')

        if num_balls == 'exit':
            print("Выход из игры.")
            break  # Завершаем игру

        ball_colors = []
        # Инициализируем пустой список для хранения цветов шариков.

        for i in range(num_balls):
            color = get_valid_input(f"Введите цвет шарика {i + 1} (от 0 до 9): ", int, lambda x: 0 <= x <= 9)
            ball_colors.append(color)  # Добавляем цвет в список
        # Запрашиваем цвет каждого шарика у пользователя и добавляем его в список `ball_colors`.

        ball_line = LinkedList()
        # Создаем новый экземпляр связного списка `LinkedList`.

        for color in ball_colors:
            ball_line.append(color)
        # Добавляем каждый цвет шарика из списка `ball_colors` в связный список `ball_line`.

        # Создаем связный список на основе введенных данных
        # Комментарий, поясняющий назначение этого блока кода.


        print("\nИсходная линия шариков:", ball_line)

        destroyed = ball_line.check_and_destroy()
        # Запускаем процесс уничтожения цепочек

        print("\nУничтожено шариков:", destroyed)
        print("Оставшаяся линия шариков:", ball_line)
        print("-" * 20)  # Разделитель между играми


if __name__ == "__main__":
    # Проверяем, что скрипт запущен напрямую (а не импортирован).

    try:
        main()
    # Пытаемся выполнить основную функцию программы.

    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
    # Перехватываем любые исключения, возникающие в `main()`, и выводим сообщение об ошибке.
