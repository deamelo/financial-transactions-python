import json


def read_cnab(path) -> list[str]:
    with open(path, "r") as f:

        return f.readlines()


def read_tipo(l):
    return l[:1]


def read_data(l):
    dt = l[1:9]
    year = int(dt[:4])
    month = int(dt[4:6])
    day = int(dt[6:8])
    return f"{year}-{month}-{day}"


def read_valor(l):
    vl = int(l[9:19])
    vl = vl / 100
    return vl.__float__()


def read_cpf(l):
    return l[19:30]


def read_cartao(l):
    return l[30:42]


def read_hora(l):
    hr = l[42:48]
    horas = int(hr[:2])
    minutos = int(hr[2:4])
    segundos = int(hr[4:6])
    return f"{horas}:{minutos}:{segundos}"


def read_dono(l):
    return l[48:62].strip()


def read_loja(l):
    return l[62:80].strip()


response = []
for l in read_cnab("cnab.txt"):
    data = {}
    data["tipo"] = read_tipo(l)
    data["data"] = read_data(l)
    data["valor"] = read_valor(l)
    data["cpf"] = read_cpf(l)
    data["cartao"] = read_cartao(l)
    data["hora"] = read_hora(l)
    data["dono"] = read_dono(l)
    data["loja"] = read_loja(l)
    response.append(data)


def write_json(path) -> list[dict]:
    with open(path, "w") as f:
        json.dump(response, f, indent=2, ensure_ascii=False)


def read_json(path: str) -> list[dict]:
    with open(path, "r") as file:
        return json.load(file)
