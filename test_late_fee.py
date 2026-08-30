from late_fee import calculate_late_fee

def test_on_due_date():
    assert calculate_late_fee(0)==0

def test_three-days_late():
    assert calculate_late_fee(3)==30

def test_cap_applies():
    assert calculate_late_fee(100)==500
