from brewtools.utils import correct_gravity


def test_gravity_correction():
    og = 1.045
    reading_temp = 89
    cal_temp = 59
    expected_result = 1.049

    result = correct_gravity(og, reading_temp, cal_temp)
    assert round(result, 3) == expected_result
