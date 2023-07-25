# импорт установленного модуля
from prettytable import PrettyTable
# импорт загрузчика `from_csv`
from prettytable import from_csv
# импорт sqlite
import sqlite3
# импорт загрузчика `from_db_cursor`
from prettytable import from_db_cursor


def import_from_csv():
    with open("myfile.csv") as fp:
        # создание таблицы из `myfile.csv`
        my_table_csv = from_csv(fp)
    print(my_table_csv)


def import_from_db():
    connection = sqlite3.connect("mydb.db")
    cursor = connection.cursor()
    cursor.execute("SELECT field1, field2, field3 FROM my_table")
    # создание таблицы из объекта курсора
    my_table_db = from_db_cursor(cursor)
    print(my_table_db)


# создание экземпляра
my_table = PrettyTable()

# имена полей таблицы
my_table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]

# добавление данных по одной строке за раз
my_table.add_row(["Adelaide", 1295, 1158259, 600.5])
my_table.add_row(["Brisbane", 5905, 1857594, 1146.4])
my_table.add_row(["Darwin", 112, 120900, 1714.7])

# добавление списка строк
my_table.add_rows(
    [
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)

# Добавление колонки таблицы с именем 'Some Flag'
my_table.add_column("Some Flag",
                    [True, True, False, False, True, False, True])

# вывод таблицы в терминал
print(my_table)
