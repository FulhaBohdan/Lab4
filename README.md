# Аналіз Дат та Часу

Цей Python-код містить клас `Date` для роботи з датами та проведення базового аналізу розподілу часу, зокрема, сну та навчання.

## Клас `Date`

Клас `Date` дозволяє створювати об'єкти дати з вказаними днем, місяцем та роком, а також виконувати деякі аналітичні операції.

### Методи

  * `__init__(self, day: int, month: int, year: int)`:
    Конструктор класу, ініціалізує об'єкт `Date` з вказаними днем, місяцем та роком.

  * `__gt__(self, other)`:
    Перевантажує оператор порівняння "більше ніж" (`>`) для об'єктів `Date`. Порівнює об'єкти за роком. Повертає `True`, якщо рік поточного об'єкта більший за рік іншого об'єкта.

  * `sleep_analysis(self)`:
    Розраховує приблизну кількість годин сну на рік, виходячи з припущення, що людина спить одну третину доби.

  * `study_analysis(self)`:
    Розраховує приблизну кількість годин навчання на місяць, виходячи з припущення про 4 години навчання на день.

  * `sleep_vs_study_comparison(self)`:
    Виконує комплексний аналіз співвідношення часу сну та навчання на місяць. Виводить у консоль наступні показники (в годинах та відсотках):

      * Сон за місяць
      * Навчання за місяць
      * Вільний час (як відсоток від загального часу та в годинах)
      * Час, доступний для "лабораторної з ООП" (як половина вільного часу)

  * `is_leap_year(self)`:
    Визначає, чи є рік об'єкта високосним, і повертає кортеж `(bool, str)`, де `bool` вказує, чи є рік високосним, а `str` містить відповідне повідомлення.

### Приклад Використання

У блоці `if __name__ == "__main__":` продемонстровано створення об'єктів `Date` та використання їхніх методів:

```python
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
```

Цей приклад створює два об'єкти `Date`, викликає метод `sleep_vs_study_comparison()` для першого об'єкта, перевіряє, чи є його рік високосним, і порівнює роки відкриття двох "університетів".
