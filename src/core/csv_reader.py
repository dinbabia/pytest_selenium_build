from pathlib import Path
import csv


class CSVHeaders:
    
    def __init__(self, filename) -> None:
        # Read Excel and its specific sheetname
        self._ROOT_DIR = Path(__file__).parent.parent
        self._FILE_PATH = f"{self._ROOT_DIR}\\src\\dataset\\{filename}"
        self.data = self.get_data_from_csv()
    
    def get_data_from_csv(self):
        '''Returns a list for how many items in the csv.
        Each item in the list is a dictionary.
        The dictionary will have a key from the headers while value are the values under the column/headers.'''
        # Container of each row of data inside the csv
        data = []
        # Open file
        with open(self._FILE_PATH) as f:
            # Returns a dictionary. Header columns will act as keys to each row of data.
            reader = csv.DictReader(f)
            # Read each row of data as dictionary
            for row in reader:
                # key will be header names, value will be the specific row data under specific column
                for key, value in row.items():
                    if "|" in str(value):
                        row[key] = str(value).split("|")
                data.append(row)
        return data

class CSVKeyValue(CSVHeaders):

    def __init_subclass__(cls) -> None:
         return super().__init_subclass__()
    
    def get_data_from_csv(self):
        '''Returns dictionary. First column will be the key while the second column will be the value.'''
        # Container of each row of data inside the csv
        data = {}
        # Open file
        with open(self._FILE_PATH) as f:
            # Returns a dictionary. Header columns will act as keys to each row of data.
            reader = csv.reader(f)
            # Read each row of data as dictionary
            for row in reader:
                if "|" in row[1]:
                    row[1] = str(row[1]).split("|")
                data[row[0]] = row[1]
        return data

class CSVKeyKeyValue(CSVHeaders):

    def __init_subclass__(cls) -> None:
         return super().__init_subclass__()
    
    def get_data_from_csv(self):
        '''Returns a dictionary within a dictionary.
        The key will be the first column.
        The value will be the inner dictionary.
        Inner dictionary key is the left side of "|"
        Value will be the one on the right side.
        Else, if no "|", then True'''
        # Container of each row of data inside the csv
        data = {}
        # Open file
        with open(self._FILE_PATH) as f:
            # Returns a dictionary. Header columns will act as keys to each row of data.
            reader = csv.reader(f)
            # Read each row of data as dictionary
            for row in reader:
                # Container of inner dictionary
                attrs = {}
                for attr in row:
                    # Skip the first column since this is the key of the external dictionary
                    if attr == row[0] : continue
                    # The left part is the key, while the right part will be the value separated by '|'
                    if "|" in attr:
                        attr = str(attr).split("|")
                        attrs[attr[0]] = attr[1]
                    # If no '|', then key is the one placed one the csv, and value is True
                    else:
                        attrs[attr] = True
                data[row[0]] = attrs
        return 