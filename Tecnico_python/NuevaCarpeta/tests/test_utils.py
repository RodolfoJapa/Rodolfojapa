from tecnico_python.src.utils import media, varianza

def test_media():
    assert media([2, 4, 6]) == 4


def test_varianza():
    assert varianza([2, 4, 6]) == 2.6666666666666665
