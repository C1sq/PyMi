from scipy import stats
from PyQt5.QtWidgets import QMessageBox

class Heandler:
    def __init__(self):
        self.stats = stats

    def studen_nez(self, data):
        try:
            return self.stats.ttest_ind(*data)
        except Exception as e:
            QMessageBox.critical(None, "Ошибка", f"Ошибка при выполнении t-теста для независимых выборок: {e}")
            return None

    def studen_zav(self, data):
        try:
            return self.stats.ttest_rel(*data)
        except Exception as e:
            QMessageBox.critical(None, "Ошибка", f"Ошибка при выполнении t-теста для зависимых выборок: {e}")
            return None

    def mana_ui(self, data):
        try:
            return self.stats.mannwhitneyu(*data)
        except Exception as e:
            QMessageBox.critical(None, "Ошибка", f"Ошибка при выполнении теста Манна-Уитни: {e}")
            return None

    def wilk(self, data):
        try:
            return self.stats.wilcoxon(*data)
        except Exception as e:
            QMessageBox.critical(None, "Ошибка", f"Ошибка при выполнении теста Уилкоксона: {e}")
            return None

    def kru(self, data):
        try:
            return self.stats.kruskal(*data)
        except Exception as e:
            QMessageBox.critical(None, "Ошибка", f"Ошибка при выполнении теста Крускала-Уоллиса: {e}")
            return None

    def fisher_test(self, data, alternative='two-sided'):
        try:
            # Проверяем, что входные данные имеют размер 2x2
            if len(data) != 2 or len(data[0]) != 2 or len(data[1]) != 2:
                QMessageBox.warning(None, "Ошибка данных", "Данные должны быть в формате таблицы 2x2.")
                return None

            odds_ratio, p_value = self.stats.fisher_exact(data, alternative=alternative)
            return f'Отношение шансов (Odds Ratio): {odds_ratio}, P-значение: {p_value}'
        except Exception as e:
            QMessageBox.critical(None, "Ошибка", f"Ошибка при выполнении точного теста Фишера: {e}")
            return None

    def bart(self, data):
        try:
            return self.stats.bartlett(*data)
        except Exception as e:
            QMessageBox.critical(None, "Ошибка", f"Ошибка при выполнении теста Бартлетта: {e}")
            return None

    def leve(self, data):
        try:
            return self.stats.levene(*data)
        except Exception as e:
            QMessageBox.critical(None, "Ошибка", f"Ошибка при выполнении теста Левена: {e}")
            return None


had = Heandler()
print(had.fisher_test([[12, 12, 12, 1, 21, 2, 1], [23432, 654, 6546, 5235432, 24, 235, 2354]]))
