from brewtools.calculators import calculate_abv, correct_gravity


def test_gravity_correction():
    og = 1.045
    reading_temp = 89
    cal_temp = 59
    expected_result = 1.049

    result = correct_gravity(og, reading_temp, cal_temp)
    assert round(result, 3) == expected_result


def test_abv_calculator():
    og = 1.057
    fg = 1.012
    expected_result = 131.25 * (og - fg)

    result = calculate_abv(og, fg)
    assert round(result, 3) == round(expected_result, 3)
