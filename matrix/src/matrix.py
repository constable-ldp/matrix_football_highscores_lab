class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self):
        row_strings = self.matrix_string.split("\n")
        rows = [row_string.split(" ") for row_string in row_strings]
        for index in range(len(rows)):
            rows[index] = [int(number) for number in rows[index]]
        return rows


    # def column(self):
    #     rows = self.row()
    #     columns = rows
    #     for index in range(len(rows)):
    #         print(index)
    #         columns[index] = [rows[number][index] for number in range(len(rows))]
    #     return columns

    def column(self):
        rows = self.row()
        columns = []
        for index in range(len(rows[0])):
            column = [(row[index]) for row in rows]
            columns.append(column)
            column = []
        return columns
