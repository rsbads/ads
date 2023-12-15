from data.download import download_data
from plotnine import (
    ggplot, aes,
    geom_line,
    ggtitle,
    xlab, ylab
)

def plot_line(ticker:str) -> ggplot:
    """_summary_

    Args:
        ticker (str): _description_

    Returns:
        ggplot: _description_
    """

    data = download_data(ticker)
    
    fig = ggplot (
        data = data.reset_index(),
        mapping = aes(x = 'Date', y = 'Close')
    ) +\
        geom_line() +\
        ggtitle('Dados historicos do {ticker}') +\
        xlab('Data') +\
        ylab('Fechamento')

    return fig