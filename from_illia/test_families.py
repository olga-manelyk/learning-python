from from_illia.theatre import amount_of_families


def test_amount_of_families():
    assert amount_of_families("", 1) == 2
    assert amount_of_families("1A 1B 1C 1D 1E 1F 1G 1H 1J 1K", 1) == 0
    assert amount_of_families("1A 1B 1C 1H 1J 1K", 1) == 1
    assert amount_of_families("1A 1F 1G 1H 1J 1K", 1) == 1
    assert amount_of_families("1A 1B 1C 1D 1E 1K", 1) == 1
    assert amount_of_families("", 20) == 40
    assert amount_of_families("15D", 20) == 39
