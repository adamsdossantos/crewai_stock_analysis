#!/usr/bin/env python
import sys
import warnings
import pandas as pd
import os

from crew import Yfinance

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

tickers = pd.read_csv('C:\\Users\\adams\\Desktop\\machine_learning\\porfolio_crewai\\ai_stock_analyst\\crewai\\yfinance\\src\\yfinance\\ticker.csv', header=None)


def run():
    """
    Run the crew.

    """


    input = [{'ticker': ticker[0]} for ticker in tickers.values]
    Yfinance().crew().kickoff_for_each(inputs=input)

    #input = {'ticker': 'NVDA'}
    #Yfinance().crew().kickoff(inputs=input)


if __name__ == "__main__":
    run()


    



