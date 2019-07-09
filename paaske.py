from datetime import date, timedelta

def calculate_easter(year):
    a = divmod(year, 19)[1]
    b,c = divmod(year, 100)
    d,e = divmod(b, 4)
    f = divmod(b + 8, 25)[0]
    g = divmod(b - f + 1, 3)[0]
    h = divmod(19*a + b - d - g + 15, 30)[1]
    i, k = divmod(c, 4)
    l = divmod(32 + 2*e + 2*i - h - k, 7)[1]
    m = divmod(a + 11*h + 22*l, 451)[0]
    n, o = divmod(h + l - 7*m + 114, 31)

    day = o + 1
    month = n
    return date(year, month, day)

def get_holidays(year):
    easter = calculate_easter(year)
    return sorted([
        # Nytaarsdag
        date(year, 1, 1),
        # Skaertorsdag
        easter - timedelta(days=3),
        # Langfredag
        easter - timedelta(days=2),
        # Paaskedag
        easter,
        # Anden easterdag
        easter + timedelta(days=1),
        # Store bededag
        easter + timedelta(days=26),
        # Kristi Himmelfart
        easter + timedelta(days=39),
        # Pinsedag
        easter + timedelta(days=49),
        # Anden pinsedag
        easter + timedelta(days=50),
        # Grundlovsdag
        date(year, 6, 5),
        # Juleaften
        date(year, 12, 24),
        # Foerste juledag
        date(year, 12, 25),
        # Anden juledag
        date(year, 12, 26),
        # Nytaarsaftens dag
        date(year, 12, 31),
    ])
