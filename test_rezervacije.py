import pytest

from rezervacije import prosjecna_cijena


def test_prosjecna_cijena():
    rezervacije = [
        {"gost": "Ana", "noci": 3, "cijena_noci": 80},
        {"gost": "Marko", "noci": 5, "cijena_noci": 65},
        {"gost": "Ivana", "noci": 2, "cijena_noci": 120},
    ]

    rezultat = prosjecna_cijena(rezervacije)

    assert rezultat == pytest.approx(88.3333333333)


def test_prazna_lista():
    with pytest.raises(ValueError):
        prosjecna_cijena([])
