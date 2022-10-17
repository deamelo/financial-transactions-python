from utils import uploadData, cnab, getTransaction


PATH = "cnab.txt"
FILEPATH = "cnab.json"
DATA = "BAR DO JOÃO"


def main():
    cnab.read_cnab(PATH)

    cnab.write_json(FILEPATH)

    cnab.read_json(FILEPATH)

    uploadData.upload_data(FILEPATH)

    getTransaction.get_transaction(DATA)


if __name__ == "__main__":

    main()
