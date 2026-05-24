from tip_calculator import calculate_tip, split_bill


def test_calculate_tip_twenty_percent():
    assert calculate_tip(50, 20) == 10.0


def test_calculate_tip_zero():
    assert calculate_tip(50, 0) == 0.0


def test_calculate_tip_rounds_to_cents():
    assert calculate_tip(33.33, 15) == 5.0


def test_split_bill_evenly():
    assert split_bill(60, 4) == 15.0


def test_split_bill_two_people():
    assert split_bill(45, 2) == 22.5
