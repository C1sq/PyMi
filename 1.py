import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, \
    QPushButton, QHBoxLayout


class Mainapp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Настройка основного окна
        self.setWindowTitle('Критерии')
        self.setGeometry(100, 100, 600, 400)

        # Создаем центральный виджет
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Создаем таблицу
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(0)  # Начальное количество строк
        self.table_widget.setColumnCount(0)  # Начальное количество столбцов

        # Создаем кнопки для добавления строк и столбцов
        self.add_row_button = QPushButton('Добавить строку')
        self.add_row_button.clicked.connect(self.add_row)  # Подключаем сигнал к слоту

        self.add_column_button = QPushButton('Добавить столбец')
        self.add_column_button.clicked.connect(self.add_column)  # Подключаем сигнал к слоту

        # Компоновка для кнопок и таблицы
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_row_button)
        button_layout.addWidget(self.add_column_button)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addLayout(button_layout)

        central_widget.setLayout(layout)

    def add_row(self):
        # Получаем текущее количество строк
        current_row_count = self.table_widget.rowCount()

        # Увеличиваем количество строк на 1
        self.table_widget.insertRow(current_row_count)

        # Заполняем новую строку пустыми ячейками или значениями
        for column in range(self.table_widget.columnCount()):
            item = QTableWidgetItem(f'Ячейка {current_row_count + 1}, {column + 1}')
            self.table_widget.setItem(current_row_count, column, item)

    def add_column(self):
        # Получаем текущее количество столбцов
        current_column_count = self.table_widget.columnCount()

        # Увеличиваем количество столбцов на 1
        self.table_widget.insertColumn(current_column_count)

        # Устанавливаем заголовок для нового столбца
        self.table_widget.setHorizontalHeaderItem(current_column_count,
                                                  QTableWidgetItem(f'Колонка {current_column_count + 1}'))

        # Заполняем новую колонку пустыми ячейками или значениями
        for row in range(self.table_widget.rowCount()):
            item = QTableWidgetItem(f'Ячейка {row + 1}, {current_column_count + 1}')
            self.table_widget.setItem(row, current_column_count, item)


# Запуск приложения
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mainapp()
    window.show()
    sys.exit(app.exec())
