import pandas as pd

class CSVHelper:
    @staticmethod
    def read_csv_to_dataframe(file_path):
        """
        Reads a CSV file and returns a DataFrame.
        
        :param file_path: Path to the CSV file
        :return: DataFrame containing the CSV data
        """
        return pd.read_csv(file_path)

    @staticmethod
    def write_dataframe_to_csv(dataframe, file_path):
        """
        Writes a DataFrame to a CSV file.
        
        :param dataframe: DataFrame to write to CSV
        :param file_path: Path to the output CSV file
        """
        dataframe.to_csv(file_path, index=False)