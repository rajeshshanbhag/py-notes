import mysql.connector
from contextlib import contextmanager

@contextmanager
def get_db_cursor(commit=False):
    connection=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='expense_manager'
    )

    cursor=connection.cursor(dictionary=True)             # gives results in dictionary format
    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()

    def fetch_all_records():
        with get_db_cursor() as cursor:
            cursor.execute('SELECT * FROM expenses')
            expenses=cursor.fetchall()
            for expense in expenses:
                print(expense)

    def fetch_expenses_for_date(expense_date):
        with get_db_cursor() as cursor:
            cursor.execute('SELECT * FROM expenses WHERE expense_date=%s',(expense_date,))
            expenses=cursor.fetchall()
            return expenses
    
    def insert_expense(expense_date,amount,category,notes):
        with get_db_cursor(commit=True) as cursor:
            cursor.execute('INSERT into expenses (expense_date,amount,category,notes) VALUES (%s,%s,%s,%s)',(expense_date,amount,category,notes))

    def delete_expenses_for_date(expense_date):
        with get_db_cursor(commit=True) as cursor:
            cursor.execute('DELETE FROM expenses WHERE expense_date=%s',(expense_date,))

    def fetch_expense_summary(start_date,end_date):
        with get_db_cursor() as cursor:
            cursor.execute('SELECT category, SUM(amount) as total FROM expenses WHERE expense_date BETWEEN %s and %s GROUP by category',(start_date,end_date))
            expenses=cursor.fetchall()
            return expenses
        
    if __name__=='__main__':
        expenses=fetch_expense_summary('2024-08-01','2024-08-05')
        for expense in expenses:
            print(expense)