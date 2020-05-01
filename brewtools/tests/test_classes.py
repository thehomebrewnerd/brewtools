import brewtools as bt


def test_gravity_creation():
    og = bt.Gravity(1.050, 85)
    fg = bt.Gravity(1.012, 74, 68)
    assert og.raw_value == 1.050
    assert og.temp == 85
    assert str(og) == 'Gravity: 1.050 at 85 degF\nCorrected: 1.053 at 59 degF'
    assert str(fg) == 'Gravity: 1.012 at 74 degF\nCorrected: 1.013 at 68 degF'
    assert repr(og) == 'Gravity(1.05, 85, 59)'
    assert repr(fg) == 'Gravity(1.012, 74, 68)'
