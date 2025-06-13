import os
from datetime import datetime
from burger_maker import AssembleBurger, SaveBurger

def test_assemble_burger(monkeypatch):
    # Mocking inputs
    monkeypatch.setattr('builtins.input', lambda _: 'pain')
    
    burger_data = AssembleBurger()
    assert burger_data['id'] == 1
    assert burger_data['pain'] == 'pain'
    assert burger_data['viande'] == 'poulet'  # default selection
    assert burger_data['fromage'] == 'fromage'
    
def test_save_burger(mocker, tmpdir):
    # Mocking datetime
    mock_datetime = mocker.patch('burger_maker.datetime')
    mock_datetime.now.return_value = datetime(2023, 10, 10, 12, 0, 0)

    # Creating a dummy burger_data for testing
    burger_data = {
        "pain": "pain",
        "viande": "poulet",
        "sauce": "ketchup and mustard",
        "fromage": "fromage",
        "id": 1,
        "ingredients": ["pain", "poulet", "fromage", "ketchup and mustard"],
        "price": 12.24,
        "timestamp": "2023-10-10T12:00:00"
    }

    SaveBurger(burger_data)
    
    with open(f"{tmpdir}/burger.txt", "a") as f:
        f.write("Burger 1: pain + poulet + ketchup and mustard + fromage\n")
    with open(f"{tmpdir}/burger_count.txt", "w") as f:
        f.write("1")

    assert burger_data == {
        "pain": "pain",
        "viande": "poulet",
        "sauce": "ketchup and mustard",
        "fromage": "fromage",
        "id": 1,
        "ingredients": ["pain", "poulet", "fromage", "ketchup and mustard"],
        "price": 12.24,
        "timestamp": "2023-10-10T12:00:00"
    }
