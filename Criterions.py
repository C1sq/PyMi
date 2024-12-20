from scipy import stats
from PyQt5.QtWidgets import QMessageBox

class Heandler:
    def __init__(self):
        from scipy import stats
        self.stats = stats

    def studen_nez(self, data):
        """
        Выполняет t-тест для независимых выборок (двусторонний и односторонний) для всех возможных пар,
        если передано больше двух групп.
        """
        try:
            from itertools import combinations
            from scipy.stats import ttest_ind

            results = []
            results.append(f'Тест Стьюдента для независимых\n')
            # Если передано больше двух групп, вычисляем для всех пар
            if len(data) > 2:
                for (i, data1), (j, data2) in combinations(enumerate(data), 2):
                    # Двусторонний тест
                    stat, p_value_two_sided = ttest_ind(data1, data2, alternative='two-sided')

                    # Односторонние тесты
                    _, p_value_greater = ttest_ind(data1, data2, alternative='greater')
                    _, p_value_less = ttest_ind(data1, data2, alternative='less')

                    results.append(
                        f'Пара {i + 1} и {j + 1}:\n'
                        f'Статистика: {stat}\n'
                        f'p-значение (двустороннее): {p_value_two_sided}\n'
                        f'p-значение (одностороннее, больше): {p_value_greater}\n'
                        f'p-значение (одностороннее, меньше): {p_value_less}\n'
                    )
            else:
                # Обработка случая только для двух групп
                data1, data2 = data[0], data[1]

                # Двусторонний тест
                stat, p_value_two_sided = ttest_ind(data1, data2, alternative='two-sided')

                # Односторонние тесты
                _, p_value_greater = ttest_ind(data1, data2, alternative='greater')
                _, p_value_less = ttest_ind(data1, data2, alternative='less')

                results.append(
                    f'Статистика: {stat}\n'
                    f'p-значение (двустороннее): {p_value_two_sided}\n'
                    f'p-значение (одностороннее, больше): {p_value_greater}\n'
                    f'p-значение (одностороннее, меньше): {p_value_less}\n'
                )

            return "".join(results)

        except Exception as e:
            QMessageBox.critical(None, "Ошибка", f"Ошибка при выполнении t-теста для независимых выборок: {e}")
            return None


    def studen_zav(self, data):
        """
        Выполняет t-тест для зависимых выборок для всех возможных пар, если передано больше двух групп.
        """
        try:
            from itertools import combinations
            from scipy.stats import ttest_rel

            results = []
            results.append(f'Тест Стьюдента для зависимых\n')
            if len(data) > 2:
                for (i, data1), (j, data2) in combinations(enumerate(data), 2):
                    stat, p_value = ttest_rel(data1, data2)
                    results.append(
                        f'Пара {i + 1} и {j + 1}:\n'
                        f'Статистика: {stat}\n'
                        f'p-значение: {p_value}\n'
                    )
            else:
                data1, data2 = data[0], data[1]
                stat, p_value = ttest_rel(data1, data2)
                results.append(
                    f'Статистика: {stat}\n'
                    f'p-значение: {p_value}\n'
                )

            return "".join(results)

        except Exception as e:
            return f"Ошибка при выполнении t-теста для зависимых выборок: {e}"

    def mana_ui(self, data):
        """
        Выполняет тест Манна-Уитни для всех возможных пар, если передано больше двух групп.
        """
        try:
            from itertools import combinations
            from scipy.stats import mannwhitneyu

            results = []
            results.append(f'Тест Манна-Уитни\n')
            if len(data) > 2:
                for (i, data1), (j, data2) in combinations(enumerate(data), 2):
                    stat, p_value = mannwhitneyu(data1, data2)
                    results.append(
                        f'Пара {i + 1} и {j + 1}:\n'
                        f'Статистика: {stat}\n'
                        f'p-значение: {p_value}\n'
                    )
            else:
                data1, data2 = data[0], data[1]
                stat, p_value = mannwhitneyu(data1, data2)
                results.append(
                    f'Статистика: {stat}\n'
                    f'p-значение: {p_value}\n'
                )

            return "".join(results)

        except Exception as e:
            return f"Ошибка при выполнении теста Манна-Уитни: {e}"

    def wilk(self, data):
        """
        Выполняет тест Уилкоксона для всех возможных пар, если передано больше двух групп.
        """
        try:
            from itertools import combinations
            from scipy.stats import wilcoxon

            results = []
            results.append(f'Тест Уилкоксона\n')
            if len(data) > 2:
                for (i, data1), (j, data2) in combinations(enumerate(data), 2):
                    stat, p_value = wilcoxon(data1, data2)
                    results.append(
                        f'Пара {i + 1} и {j + 1}:\n'
                        f'Статистика: {stat}\n'
                        f'p-значение: {p_value}\n'
                    )
            else:
                data1, data2 = data[0], data[1]
                stat, p_value = wilcoxon(data1, data2)
                results.append(
                    f'Статистика: {stat}\n'
                    f'p-значение: {p_value}\n'
                )

            return "".join(results)

        except Exception as e:
            return f"Ошибка при выполнении теста Уилкоксона: {e}"

    def kru(self, data):
        """
        Выполняет тест Крускала-Уоллиса.
        """
        try:
            stat, p_value = self.stats.kruskal(*data)
            return (
                f'Тест Крускала-Уоллиса\n'
                f'Статистика: {stat}\n'
                f'p-значение: {p_value}\n'
            )
        except Exception as e:
            return f"Ошибка при выполнении теста Крускала-Уоллиса: {e}"

    def fisher_test(self, data):
        """
        Выполняет F-тест для всех возможных пар, если передано больше двух выборок.
        """
        try:
            import numpy as np
            from scipy.stats import f
            from itertools import combinations

            results = []
            results.append(f'Тест Фишера\n')
            if len(data) > 2:
                for (i, data1), (j, data2) in combinations(enumerate(data), 2):
                    var1 = np.var(data1, ddof=1)
                    var2 = np.var(data2, ddof=1)
                    F_statistic = var1 / var2 if var1 > var2 else var2 / var1
                    p_value = 1 - f.cdf(F_statistic, len(data1) - 1, len(data2) - 1)

                    results.append(
                        f'Пара {i + 1} и {j + 1}:\n'
                        f'F-статистика: {F_statistic}\n'
                        f'p-значение: {p_value}\n'
                    )
            else:
                data1, data2 = data[0], data[1]
                var1 = np.var(data1, ddof=1)
                var2 = np.var(data2, ddof=1)
                F_statistic = var1 / var2 if var1 > var2 else var2 / var1
                p_value = 1 - f.cdf(F_statistic, len(data1) - 1, len(data2) - 1)

                results.append(
                    f'F-статистика: {F_statistic}\n'
                    f'p-значение: {p_value}\n'
                )

            return "".join(results)

        except Exception as e:
            return f"Ошибка при выполнении F-теста: {e}"

    def bart(self, data):
        """
        Выполняет тест Бартлетта.
        """
        try:
            stat, p_value = self.stats.bartlett(*data)
            return (
                f'Тест Бартлетта\n'
                f'Статистика: {stat}\n'
                f'p-значение: {p_value}\n'
            )
        except Exception as e:
            return f"Ошибка при выполнении теста Бартлетта: {e}"

    def leve(self, data):
        """
        Выполняет тест Левена.
        """
        try:
            stat, p_value = self.stats.levene(*data)
            return (
                f'Тест Левена\n'
                f'Статистика: {stat}\n'
                f'p-значение: {p_value}\n'
            )
        except Exception as e:
            return f"Ошибка при выполнении теста Левена: {e}"


had = Heandler()
print(had.fisher_test([[12, 12, 12, 1, 21, 2, 1], [23432, 654, 6546, 5235432, 24, 235, 2354]]))
