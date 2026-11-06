def prosjecna_cijena(rezervacije: list[dict]) -> float:
    """Racuna prosjecnu cijenu jednog nocenja."""
    if not rezervacije:
        raise ValueError("Lista rezervacija ne smije biti prazna.")

    ukupno = sum(r["cijena_noci"] for r in rezervacije)
    return ukupno / len(rezervacije)


if __name__ == "__main__":
    rezervacije = [
        {"gost": "Ana", "noci": 3, "cijena_noci": 80},
        {"gost": "Marko", "noci": 5, "cijena_noci": 65},
        {"gost": "Ivana", "noci": 2, "cijena_noci": 120},
    ]

    # Eksplicitna petlja
    ukupno = 0

    for r in rezervacije:
        ukupno += r["noci"] * r["cijena_noci"]

    # Ekvivalent pomocu izraza
    iznosi = [r["noci"] * r["cijena_noci"] for r in rezervacije]

    skupe = [r["gost"] for r, i in zip(rezervacije, iznosi) if i > 250]

    print(ukupno, sum(iznosi))
    print(skupe)
    print("Prosjecna cijena:", prosjecna_cijena(rezervacije))
