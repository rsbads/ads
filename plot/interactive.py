import plotly.express as px
from data.download import download_data

def plot_line_i(ticker:str):
    """_summary_

    Args:
        ticker (str): ticker financial asset.

    Returns:
        _type_: graphic interactive.
    """

    data= download_data('BBAS3.SA')

    fig= px.line(
            data.reset_index(),
            x= 'Date', y= 'Close', title= 'ticker',
            labels={'Close': 'Fechamento', 'Date': 'Data'} 
        )

    return fig