"""
This module contains classes for modeling a stock portfolio, including individual stocks, positions within a portfolio, and the portfolio itself.

Classes:
    - Stock: Represents an individual stock with ticker, price, dividend, and dividend frequency.
    - Position: Represents a position within a portfolio, containing a stock and a number of shares.
    - Portfolio: Represents a portfolio composed of multiple positions.

Details:
    - Stock provides information on individual stocks and calculates the annual dividend based on the dividend and frequency.
    - Position allows comparison between different positions based on the total value.
    - Portfolio provides methods to calculate the total value and portfolio yield.
"""

from dataclasses import dataclass, field
from functools import total_ordering
from typing import List


@dataclass(frozen=True)
class Stock:
    """
    Represents a stock with a ticker, price, dividend, and dividend frequency.

    Attributes:
        ticker (str): The stock's ticker symbol.
        price (float): The stock's current price.
        dividend (float): The dividend per period.
        dividend_frequency (int): The number of dividend distributions per year.

    Property:
        annual_dividend (float): The annual dividend for the stock, calculated as dividend times dividend frequency.
    """
    ticker: str = field(compare=True)
    price: float = field(compare=True, hash=False)
    dividend: float = field(default=0, compare=True)
    dividend_frequency: int = field(default=4, compare=True)

    @property
    def annual_dividend(self):
        """
        Calculates the annual dividend based on the dividend and frequency.

        Returns:
            float: The annual dividend for this stock.
        """
        return self.dividend * self.dividend_frequency


@dataclass
@total_ordering
class Position:
    """
    Represents a position in a portfolio, with a specific stock and number of shares.

    Attributes:
        stock (Stock): The stock for this position.
        share (int): The number of shares in this position.

    Methods:
        __lt__(other): Compares this position with another based on total value.
        __eq__(other): Checks if this position is equal to another based on total value.
    """
    stock: Stock
    share: int = field(compare=True, hash=False)

    def __lt__(self, other):
        """
        Compares this position with another based on the total value.

        Args:
            other (Position): Another position to compare.

        Raises:
            TypeError: If other is not an instance of Position.

        Returns:
            bool: True if this position's value is less than the other's, False otherwise.
        """
        if type(other) != Position:
            raise TypeError("Can only compare instance of Position")

        return self.stock.price * self.share < other.stock.price * other.share

    def __eq__(self, other):
        """
        Checks if this position is equal to another based on total value.

        Args:
            other (Position): Another position to compare.

        Raises:
            TypeError: If other is not an instance of Position.

        Returns:
            bool: True if both positions have the same total value, False otherwise.
        """
        if type(other) != Position:
            raise TypeError("Can only compare instance of Position")

        return self.stock.price * self.share == other.stock.price * other.share


@dataclass
class Portfolio:
    """
    Represents a portfolio with multiple positions.

    Attributes:
        holdings (List[Position]): A list of positions in the portfolio.

    Properties:
        value (float): The total value of the portfolio.
        portfolio_yield (float): The yield of the portfolio, calculated as total dividends divided by total value.
    """
    holdings: List[Position]

    @property
    def value(self):
        """
        Calculates the total value of the portfolio.

        Returns:
            float: The total value of all positions in the portfolio.
        """
        total_value = sum(
            [position.stock.price * position.share for position in self.holdings])
        return total_value

    @property
    def portfolio_yield(self):
        """
        Calculates the portfolio's yield based on total dividends and total value.

        Returns:
            float: The yield, calculated as total dividends divided by total value.
        """
        total_dividends = sum(
            [position.stock.annual_dividend * position.share for position in self.holdings])
        return round((total_dividends / self.value), 6)
