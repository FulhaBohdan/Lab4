class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __gt__(self, other):
        if isinstance(other, Date):
            return self.year > other.year

    def sleep_analysis(self):
        hours_per_day = 24
        sleep_hours = hours_per_day / 3  # одна третина доби — це сон
        sleep_hours_per_year = sleep_hours * 365
        return sleep_hours_per_year

    def study_analysis(self):
        average_study_hours_per_day = 4
        study_hours_per_month = average_study_hours_per_day * 30  # умовний середній місяць
        return study_hours_per_month

    def sleep_vs_study_comparison(self):
        sleep_year = self.sleep_analysis()
        sleep_per_month = sleep_year / 12
        study_per_month = self.study_analysis()

        total_hours_in_month = 24 * 30  # =720 годин
        sleep_percent = (sleep_per_month / total_hours_in_month) * 100
        study_percent = (study_per_month / total_hours_in_month) * 100
        lab_in_hours = (total_hours_in_month-sleep_percent-study_percent)
        free_time_percent = 100 - sleep_percent - study_percent# вільний час протягом року
        lab_time_percent = free_time_percent / 2  # половина вільного часу, бо предмет є протягом семестру
        no_free_time_percent = sleep_per_month - study_per_month

        print(f"Сон в місяць: {round(sleep_per_month, 2)} годин")
        print(f"Сон у відсотках: {round(sleep_percent, 2)}%\n")
        print(f"Навчання в місяць (в середньому): {round(study_per_month, 2)} годин")
        print(f"Навчання у відсотках: {round(study_percent, 2)}%\n")
        print(f"Вільний час: {round(free_time_percent, 2)}% або {round( lab_in_hours, 2)} годин")
        print(f"Вільний час для лабораторної з ООП: {round(lab_time_percent, 2)}%\n")

    def is_leap_year(self):
        if self.year % 4 != 0:
            return (False, "Університет відкрився у звичайний рік — це не високосний.")
        elif self.year % 100 != 0:
            return (True, "Університет відкрився у високосний рік — це хороша ознака, якщо вірити віруванням.")
        elif self.year % 400 == 0:
            return (True, "Університет відкрився у високосний рік — це особливий випадок.")
        else:
            return (False, "Університет відкрився у звичайний рік — це не високосний.")


if __name__ == "__main__":
    unik_opening1 = Date(4, 12, 1834)
    unik_opening2 = Date(15, 9, 1588)




    print("\nАНАЛІЗ В ГОДИНАХ:\n")
    unik_opening1.sleep_vs_study_comparison()

    print("\nАНАЛІЗ ВИСОКОСНОГО РОКУ:\n")
    leap, message = unik_opening1.is_leap_year()
    print(message)

    if unik_opening2 > unik_opening1:
        print("Другий університет відкрився пізніше.")
    else:
        print("Другий університет відкрився раніше або в той самий рік.")