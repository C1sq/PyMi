import openpyxl as xl


def tabl(way: str) -> [list]:
    table = xl.open(way).active
    row = []
    for i in range(table.max_column):
        a = []
        for j in range(1, table.max_row + 1):
            if table[j][i].value:
                a += [table[j][i].value]
        row.append(a)
    return row


if __name__ == '__main__':
    print(tabl('12.xlsx'))
