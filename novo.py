from datetime import date, time


def read_cnab(path):
    with open(path, "r") as f:

        return f.readlines()


def read_tipo(l):
    return l[:1]


def read_data(l):
    dt = l[1:9]
    year = int(dt[:4])
    month = int(dt[4:6])
    day = int(dt[6:8])
    return date(year, month, day)


def read_valor(l):
    vl = int(l[9:19])
    vl = vl / 100
    return float(vl)


def read_cpf(l):
    return l[19:30]


def read_cartao(l):
    return l[30:42]


def read_hora(l):
    hr = l[42:48]
    hora = int(hr[:2])
    minuto = int(hr[2:4])
    seg = int(hr[4:6])
    return time(hora, minuto, seg)


def read_owner(l):
    return l[48:62].strip()


def read_loja(l):
    return l[62:80].strip()


if __name__ == "__main__":
    response = []
    for l in read_cnab("cnab.txt"):
        data = {}
        data["tipo"] = read_tipo(l)
        data["data"] = read_data(l)
        data["valor"] = read_valor(l)
        data["cpf"] = read_cpf(l)
        data["cartao"] = read_cartao(l)
        data["hora"] = read_hora(l)
        data["dono"] = read_owner(l)
        data["loja"] = read_loja(l)
        response.append(data)

    print(response)
