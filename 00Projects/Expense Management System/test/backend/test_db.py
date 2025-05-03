from backend import db

def test_fetch_expenses_for_date():
    expenses=db.fetch_expenses_for_date('2024-08-15')
    assert len(expenses)==1
    assert expenses[0]['amount']==10.0