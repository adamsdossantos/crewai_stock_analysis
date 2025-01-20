from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import yfinance as yf

class YFinanceStockAnalysisInput(BaseModel):
    """Input schema for MyCustomTool."""
    ticker: str = Field(..., description="stock ticker symbol.")

class YFinanceStockAnalysisTool(BaseTool):
    name: str = "YFinance Stock Analysis Tool"
    description: str = (
        "fetch and analyse stocks for a given ticker usgin yfinance."
    )
    args_schema: Type[BaseModel] = YFinanceStockAnalysisInput

    def _run(self, ticker: str) -> str:
        # Implementation goes here
        stock = yf.Ticker(ticker)
        info = stock.info
        history = stock.history(period='5y')
        week_52_high = history['High'].tail(260).max()
        week_52_low = history['Low'].tail(260).min()
        financials = stock.financials
        if not financials.empty and 'Total Revenue' in financials.index:
            revenue_5y = financials.loc['Total Revenue'].iloc[:5]
            revenue_growth = revenue_5y.iloc[0] / revenue_5y.iloc[-1] ** (1/5) if len(revenue_5y) >= 5 else None
        else:
            revenue_growth = None
    
        analysis = {
            "ticker symbol": ticker,
            "company name": info.get('longName', "N/A"),
            "current price": info.get('currentPrice', 'N/A'),
            "52-week  high":round(week_52_high, 2),
            "52-week low":round(week_52_low, 2),
            "market cap":info.get('marketCap', 'N/A'),
            "P/E ratio":info.get('trailingPE', 'N/A'),
            "P/B ration":info.get('priceToBook', 'N/A'),
            "Debt-to-equity ratio":info.get('debtToEquity', 'N/A'),
            "Current ratio":info.get('currentRatio', 'N/A'),
            "Dividend yield (%)": info.get('dividendYield', 'N/A'),
            "5-year revenue growth rate (%)":revenue_growth,
            "Free cash flow":info.get('freeCashflow', 'N/A'),
            "Profit margin": info.get('profitMargins', 'N/A'),
            "Operating margin": info.get('operatingMargins', 'N/A'),
            "Earning growth":info.get('earningsGrowth', 'N/A'),
            "Revenue growth":info.get('revenueGrowth', 'N/A'),
            "Analyst target price":info.get('targetMedianPrice', 'N/A'),
            "Beta":info.get('beta', 'N/A'),
            "5 year average return on equity (%)":info.get('returnOnEquity', 'N/A')
        }

        for key in ['Dividend yield (%)', '5-year revenue growth rate (%)', 'Profit margin', 'Operating margin', 'Earning growth', 'Revenue growth', '5 year average return on equity (%)']:
            if analysis[key] not in ['N/A', None]:
                analysis[key] = round(analysis[key] * 100, 2)
        
        output = "\n".join([f"{key}: {value}" for key, value in analysis.items()])

        return output

