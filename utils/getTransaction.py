import sqlite3


def get_transaction(loja):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    cursor.execute(
        """
    SELECT * FROM transactions 
    WHERE loja = ?
    """,
        (loja,),
    )

    saldo = 0
    for linha in cursor.fetchall():

        if linha[0] in ("2", "3", "9"):
            saldo -= linha[2]
        else:
            saldo += linha[2]
        print(linha)
        print(saldo)
    return saldo

    conn.close()
