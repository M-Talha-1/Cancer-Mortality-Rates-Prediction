import pandas as pd
import seaborn as sn

class DataIngestion:
    """
    Class for ingesting the cancer mortality data from the CSV file.
    """

    def __init__(self, file_path) -> None:
        """
        Initialize the class with the file path.
        :param file_path: The path to the CSV file
        :type file_path: str
        """
        self.file_path = file_path

    def load_data(self) ->pd.DataFrame:
        """
        Load the data from the CSV file.
        :return: A Pandas DataFrame, data loaded from the CSV file
        """
        try:
            df = pd.read_csv(self.file_path, encoding='utf-8')
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(self.file_path, encoding='latin1')
            except UnicodeDecodeError:
                try:
                    df = pd.read_csv(self.file_path, encoding='iso-8859-1')
                except UnicodeDecodeError:
                    df = pd.read_csv(self.file_path, encoding='cp1252')
        return df