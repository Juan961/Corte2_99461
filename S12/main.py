import json

def main():

    # with open("matrizAsignacion.txt", "r") as f:
    #     content = f.read()
    #     print(content)

    file = open("matrizAsignacion.txt", "r")

    lines = file.readlines()

    matrix = []

    for line in lines:
        new_line = line.replace("\n", "")

        elements = new_line.split(",")

        row = list(map(lambda el: int(el), elements))

        matrix.append(row)

    file.seek(0)



    file.close()


def json_value():

    file = open("db.json", "r")

    f = json.loads(file.read())

    print(f)

    file.close()


    print()

if __name__ == "__main__":
    main()
    # json_value()
