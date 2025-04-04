# README

## Описание программы
Программа для математического анализа данных предоставляет функционал для работы с графическим интерфейсом и позволяет пользователю применять различные критерии для анализа дисперсий.

### Основные файлы
- **[main.exe](https://github.com/C1sq/PyMi/tree/master/dist/main.exe)**: Исполняемый файл программы
- **[main.py](https://github.com/C1sq/PyMi/tree/master/main.py)**: основной файл программы, содержащий логику выполнения анализа данных.
- **[untitled.ui](https://github.com/C1sq/PyMi/tree/master/web_ui/untitled.ui)**, **[untitled1.ui](https://github.com/C1sq/PyMi/tree/master/web_ui/untitled1.ui)**, **[untitled2.ui](https://github.com/C1sq/PyMi/tree/master/web_ui/untitled2.ui)**: файлы графического интерфейса, реализованные в формате Qt Designer. Они предоставляют элементы управления и визуализации.

### Основные возможности
- Импорт данных для анализа.
- Применение различных критериев для анализа дисперсий (*добавьте здесь описание критериев*).
- Отображение результатов анализа через графический интерфейс.

### Установка и запуск
1. Убедитесь, что установлен Python 3.9 или выше.
2. Установите зависимости с помощью команды:
   ```bash
   pip install -r requirements.txt --no-cache-dir
   ```
3. Запустите приложение с помощью команды:
   ```bash
   python main.py
   ```

### Использование
1. Загрузите данные для анализа через графический интерфейс.
2. Выберите критерии анализа дисперсий из доступного списка (*добавьте описание доступных критериев*).
3. Просмотрите результаты анализа на экране и экспортируйте их при необходимости.

### Зависимости
- PyQt6 (для работы с графическим интерфейсом)
- scipy (для математических операций)
- openpyxl (для работы кода с xlsx и xls файлами таблиц)

# Основные возможности программы

Программа предоставляет методы для выполнения различных статистических тестов с использованием библиотеки `scipy.stats` и графического интерфейса с использованием `PyQt5`. Вот список доступных методов:

1. **t-тест для независимых выборок (Student's t-test for independent samples)**  
   - Метод: `studen_nez(data)`
   - Выполняет t-тест для независимых выборок.

2. **t-тест для зависимых выборок (Student's t-test for paired samples)**  
   - Метод: `studen_zav(data)`
   - Выполняет t-тест для зависимых выборок.

3. **Тест Манна-Уитни (Mann-Whitney U test)**  
   - Метод: `mana_ui(data)`
   - Выполняет тест Манна-Уитни для проверки различий между двумя независимыми выборками.

4. **Тест Уилкоксона (Wilcoxon signed-rank test)**  
   - Метод: `wilk(data)`
   - Выполняет тест Уилкоксона для парных выборок.

5. **Тест Крускала-Уоллиса (Kruskal-Wallis test)**  
   - Метод: `kru(data)`
   - Выполняет непараметрический тест Крускала-Уоллиса для сравнения нескольких групп.

6. **Точный тест Фишера (Fisher's Exact Test)**  
   - Метод: `fisher_test(data, alternative='two-sided')`
   - Выполняет точный тест Фишера для 2x2 таблиц, с возможностью выбора альтернативной гипотезы.

7. **Тест Бартлетта (Bartlett's test)**  
   - Метод: `bart(data)`
   - Проверяет гипотезу о равенстве дисперсий между несколькими выборками.

8. **Тест Левена (Levene's test)**  
   - Метод: `leve(data)`
   - Проверяет равенство дисперсий для нескольких выборок, используя менее чувствительный подход к отклонениям от нормальности.

---

# Критерии работы программы

Программа реализует обработку ошибок для каждого из тестов с помощью интерфейса `QMessageBox`, который уведомляет пользователя о возможных проблемах:

1. **Ошибки выполнения статистического теста**  
   Каждый метод обрабатывает исключения, возникающие при выполнении теста. В случае ошибки пользователю отображается сообщение с описанием проблемы.

2. **Проверка размера данных для теста Фишера**  
   В методе `fisher_test` проверяется, что данные имеют размер 2x2 перед выполнением теста. Если это не так, выводится предупреждающее сообщение.

3. **Поддержка альтернативных гипотез для теста Фишера**  
   В методе `fisher_test` предусмотрен параметр `alternative`, который позволяет выбирать альтернативную гипотезу (например, 'two-sided').

4. **Интерфейс с сообщениями об ошибках и предупреждениями**  
   Все сообщения об ошибках и предупреждениях выводятся через интерфейс `QMessageBox`, что делает программу более удобной для пользователя.
---

# Масштабируемость программы

Код программы легко масштабируется, что позволяет добавлять новые статистические тесты и расширять функциональность без значительных изменений в структуре программы.

1. **Простота добавления новых методов**  
   Все методы для выполнения статистических тестов инкапсулированы в класс `Heandler`. Для добавления нового теста достаточно создать новый метод в этом классе, который будет вызывать соответствующую функцию из библиотеки `scipy.stats` и обрабатывать возможные ошибки с помощью `QMessageBox`.

2. **Гибкость интерфейса**  
   Программа использует интерфейс `QMessageBox` для отображения сообщений об ошибках, что позволяет легко адаптировать интерфейс для новых тестов. Например, для нового теста можно добавить сообщения о успешном завершении или ошибки, если тест не может быть выполнен.

3. **Легкость в модификации**  
   Каждый метод обрабатывает ошибку внутри себя и может быть дополнен дополнительными параметрами или логикой для других статистических тестов. Для этого не требуется изменение остальной части программы, что делает масштабирование более удобным и быстрым.

4. **Поддержка различных форматов данных**  
   В дальнейшем можно легко добавить поддержку других форматов данных для ввода или расширить типы проверок данных, такие как проверка на корректность размерности массива или на соответствие формата данных, необходимого для конкретного теста.

5. **Расширяемость с использованием сторонних библиотек**  
   Если потребуется использовать новые статистические методы из других библиотек, код можно дополнить без изменений в существующей логике. Это позволит интегрировать дополнительные пакеты, такие как `statsmodels` или другие библиотеки для статистического анализа.

Таким образом, программа имеет гибкую архитектуру, которая делает её удобной для расширения и адаптации под новые требования или добавление новых функциональных возможностей.
