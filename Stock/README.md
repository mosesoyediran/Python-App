# Stock Portfolio Management

This repository contains a Python module for modeling a stock portfolio. It provides classes to represent individual stocks, positions within a portfolio, and the portfolio itself.

## Overview

The module includes the following classes:

- **Stock**: Represents an individual stock with attributes like ticker, price, dividend, and dividend frequency.
- **Position**: Represents a position within a portfolio, which contains a specific stock and a number of shares.
- **Portfolio**: Represents a portfolio composed of multiple positions, with methods to calculate the total value and yield.

## Classes and Attributes

### Stock
- `ticker`: The stock's ticker symbol.
- `price`: The current price of the stock.
- `dividend`: The dividend per period.
- `dividend_frequency`: The number of dividend distributions per year.

The `Stock` class has a property `annual_dividend` that returns the total annual dividend based on the dividend and its frequency.

### Position
- `stock`: The `Stock` object for this position.
- `share`: The number of shares in this position.

Position implements comparison operations (`__lt__` and `__eq__`) to enable comparisons based on the total value (stock price times the number of shares).

### Portfolio
- `holdings`: A list of `Position` objects in the portfolio.

The `Portfolio` class has the following properties:
- `value`: Calculates the total value of all positions in the portfolio.
- `portfolio_yield`: Calculates the portfolio's yield as the ratio of total dividends to the total value of the portfolio.

## Usage

To create and manage a portfolio:

```python
from stock_portfolio import Stock, Position, Portfolio

# Create some stocks
apple = Stock(ticker="AAPL", price=150.00, dividend=0.82, dividend_frequency=4)
microsoft = Stock(ticker="MSFT", price=250.00, dividend=0.56, dividend_frequency=4)

# Create positions
position1 = Position(stock=apple, share=10)  # 10 shares of Apple
position2 = Position(stock=microsoft, share=5)  # 5 shares of Microsoft

# Create a portfolio
my_portfolio = Portfolio(holdings=[position1, position2])

# Get the total value of the portfolio
portfolio_value = my_portfolio.value
print(f"Portfolio value: ${portfolio_value:.2f}")

# Get the portfolio's yield
portfolio_yield = my_portfolio.portfolio_yield
print(f"Portfolio yield: {portfolio_yield:.6f}")


License

This project is licensed under the MIT License. Feel free to use, modify, and distribute according to the license term



This README file outlines the module's purpose, details about the classes, attributes, and how to use them, along with a code example demonstrating its usage. It also includes a section for licensing information.
