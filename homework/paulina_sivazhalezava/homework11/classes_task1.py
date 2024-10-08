class Book:
    page_material = "бумага"
    text_presence = True

    def __init__(self, book_name, author, pages_quantity, isbn, reserved):
        self.book_name = book_name
        self.author = author
        self.pages_quantity = pages_quantity
        self.isbn = isbn
        self.reserved = reserved

    def print_reserved(self):
        if self.reserved:
            return print(f"Название: {self.book_name}, Автор: {self.author}, Страниц: {self.pages_quantity}, "
                         f"Материал: {self.page_material}, зарезервирована")
        else:
            return print(f"Название: {self.book_name}, Автор: {self.author}, Страниц: {self.pages_quantity}, "
                         f"Материал: {self.page_material}")


book1 = Book("Отцы и дети", "Тургенев", "500", 12345, True)
book2 = Book("Капитал", "Маркс", "800", 11345, False)
book3 = Book("Большая Четверка", "Агата Кристи", "900", 12545, True)
book4 = Book("Американская трагедия", "Драйзер", "300", 12645, False)
book5 = Book("Сад Богов", "Даррелл", "550", 12305, False)
book1.print_reserved()
book2.print_reserved()
book3.print_reserved()
book4.print_reserved()
book5.print_reserved()


class SchoolSubjects(Book):
    def __init__(self, book_name, author, pages_quantity, isbn, subject, school_year, homework_included=False,
                 reserved=False):
        super().__init__(book_name, author, pages_quantity, isbn, reserved)
        self.subject = subject
        self.school_year = school_year
        self.homework_included = homework_included

    def textbook_reserved(self):
        basic_info = (f"{self.book_name}, Автор: {self.author}, Страниц: {self.pages_quantity}, "
                      f"Материал: {self.page_material}, предмет: {self.subject}, класс: {self.school_year}")
        if self.reserved:
            return print(f"{basic_info}, зарезервирован")
        else:
            return print(f"{basic_info}")


algebra = SchoolSubjects("Алгебра", "Иванов", 200, 123, "Математика", 9, True, reserved=True)
history = SchoolSubjects("История", "Петров", 350, 456, "История", 10, True, reserved=False)
chemistry = SchoolSubjects("Органическая химия", "Смирнова", 280, 789, "Химия", 11, True, reserved=True)
literature = SchoolSubjects("Русская литература", "Сидоров", 300, 101, "Литература", 9, False, reserved=False)
biology = SchoolSubjects("Биология", "Кузнецова", 320, 202, "Биология", 8, True, reserved=False)
algebra.textbook_reserved()
history.textbook_reserved()
chemistry.textbook_reserved()
literature.textbook_reserved()
biology.textbook_reserved()
