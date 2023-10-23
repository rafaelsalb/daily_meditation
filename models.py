class BookPassages:
    name = "BookPassages"
    columns = {
                "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
                "title": "VARCHAR(100) NOT NULL",
                "author": "VARCHAR(100)",
                "passage": "VARCHAR(500) NOT NULL",
                "chapter": "VARCHAR(100)",
                "pub_date": "DATETIME"
            }
    
    def create_columns_to_str(self):
        output = ""

        for key in self.columns:
            output += f"{str(key)} {str(self.columns[key])},"
        output = output[:-1]

        return output

    def columns_to_str(self):
        output = ""

        for key in self.columns:
            output += f"{str(key)} ,"
        output = output[:-1]

        return output

    def __len__(self):
        return 1


class Test:
    name = "test"
    columns = {
                "test": "TEXT"
            }
    
    def create_columns_to_str(self):
        output = ""

        for key in self.columns:
            output += f"{str(key)} {str(self.columns[key])},"
        output = output[:-1]

        return output

    def columns_to_str(self):
        output = ""

        for key in self.columns:
            output += f"{str(key)} ,"
        output = output[:-1]

        return output

    def __len__(self):
        return 1
