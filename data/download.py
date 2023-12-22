import yfinance as yf
import pandas as pd

def download_data (ticker:str) -> pd.DataFrame:
    """_summary_

    Args:
        ticker (str): the ticker of financil asset.

    Returns:
        pd.DataFrame: a dataframe retrive from Yahoo Finance.
    """
    data = yf.download(ticker)

    return data