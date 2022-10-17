import json
import sqlite3


def upload_data(path):
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE if not exists transactions(
        tipo VARCHAR(1) NOT NULL,
        data DATE NOT NULL,
        valor FLOAT NOT NULL,
        cpf VARCHAR(11) NOT NULL,
        cartao VARCHAR(12) NOT NULL,
        hora TIME NOT NULL,
        dono VARCHAR(14) NOT NULL,
        loja VARCHAR(19) NOT NULL
    );
        """
    )

    traffic = json.load(open(path))
    columns = ["tipo", "data", "valor", "cpf", "cartao", "hora", "dono", "loja"]
    for row in traffic:
        keys = tuple(row[c] for c in columns)
        cursor.execute(
            "INSERT INTO transactions VALUES(?,?,?,?,?,?,?,?)", keys
        )

    connection.commit()
    connection.close()
