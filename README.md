
# NP - Veselin Andric

## Opis projekta

Projekat predstavlja Python program za obradu hotelskih rezervacija.

Podaci o rezervacijama čuvaju se u listi rječnika. Svaka rezervacija sadrži ime gosta, broj noćenja i cijenu jednog noćenja.

Implementirana je funkcija `prosjecna_cijena()` koja računa prosječnu cijenu jednog noćenja za sve rezervacije.

## Korišćene tehnologije

- Python 3.12.1
- Visual Studio Code
- Ruff 0.17.4
- Pytest 9.2.0

## Struktura projekta

- `rezervacije.py` - glavni Python program i funkcija za računanje prosječne cijene.
- `test_rezervacije.py` - automatski testovi.
- `requirements.txt` - spisak instaliranih Python biblioteka.
- `.gitignore` - fajlovi i folderi koje Git ignoriše.
- `README.md` - dokumentacija projekta.

## Instalacija

Kreiranje virtuelnog okruženja:

```bash
python -m venv .venv
```

Aktivacija na Windowsu:

```bash
.venv\Scripts\activate
```

Instalacija biblioteka:

```bash
pip install -r requirements.txt
```

## Pokretanje programa

```bash
python rezervacije.py
```

## Testiranje

```bash
pytest -v
```

Rezultat: 2 uspješno izvršena testa.

## Provjera kvaliteta koda

Provjera pomoću Ruff-a:

```bash
ruff check .
```

Formatiranje:

```bash
ruff format .
```

## AI asistencija

Za implementaciju funkcije korišćen je AI asistent (ChatGPT).

### Upotrijebljeni upit

"Na osnovu postojećeg Python programa za obradu hotelskih rezervacija implementiraj funkciju prosjecna_cijena koja računa prosječnu cijenu noćenja. Obradi slučaj prazne liste rezervacija i napiši odgovarajući Pytest test koji provjerava ispravnost funkcije i ponašanje za praznu listu."

### Uočeni nedostaci generisanog koda

1. Pojam prosječne cijene može imati različita značenja. Implementirano rješenje računa prosječnu cijenu jednog noćenja, a ne prosječan ukupan iznos rezervacije.
2. Funkcija ne provjerava da li su svi podaci u rječnicima ispravnog tipa.
3. Funkcija pretpostavlja da svaka rezervacija sadrži ključ `cijena_noci`.
4. Generisani kod je potrebno pregledati i testirati, jer AI ne garantuje da je svaki rezultat ispravan.

### Zaključak

Projekat demonstrira upotrebu Python funkcija, listi, rječnika, list comprehensions, virtuelnog okruženja, Ruff-a i Pytest-a.

Korišćen je AI asistent za pomoć pri implementaciji, a generisani kod je pregledan i testiran.
