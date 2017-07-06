GENRES_LIST = sorted(["simulador", "tiro", "role-playing", "stealth", "party", "xbox one", "esporte", "guerra", "casual", "social", "adventure", "para pc rpg", "rpg", "danca", "xbox 360", "systems", "para pc esporte", "para pc acao", "indie", "action", "a??o", "acesso antecipado", "acao", "simuladores", "musicais", "arp", "racioc?nio", "terror", "para pc de tiro", "para pc arcade", "luta", "aventura", "fighting", "corrida", "survival", "estrategia", "platform", "estrat?gia", "fps", "None","variados","multijogador massivo online (mmo)", "coletanea", "para pc estrat?gia"])


def get_coverage(preferences, games):
    pass

def get_precision(preferences, games):
    pass

def get_f_measure(precision, coverage):
    pass

def get_clean_price(price):
    clean_price = price.split(' ')[1]
    clean_price = clean_price.replace(".", "")
    clean_price = clean_price.replace(",", ".")
    return clean_price

def get_price_interval(price):
    if price <= 40.0:
        return "1"

    if price > 40 and price <= 80.0:
        return "2"

    if price > 80.0 and price <= 120.0:
        return "3"

    if price > 120:
        return "4"

    return False
