from utils.cnab import read_cnab, write_json


PATH = "cnab.txt"
FILEPATH = "cnab.json"


def main():
    read_cnab(PATH)

    write_json(FILEPATH)


if __name__ == "__main__":
    main()
