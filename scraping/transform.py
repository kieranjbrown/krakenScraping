import csv
import random
from decimal import Decimal

stocks = ['AAPL', 'MSFT', 'AMZN', 'FB', 'GOOG',
          'GOOGL', 'INTC', 'CMCSA', 'CSCO', 'PEP',
          'ADBE', 'AMGN', 'NFLX', 'NVDA', 'COST',
          'PYPL', 'AVGO', 'TXN', 'CHTR', 'SBUX',
          'QCOM', 'GILD', 'BKNG', 'FISV', 'MDLZ',
          'ADP', 'ISRG', 'INTU', 'TMUS', 'TSLA',
          'CSX', 'VRTX', 'BIIB', 'WBA', 'AMAT',
          'MU', 'ILMN', 'MAR', 'EXC', 'AMD',
          'ROST', 'ATVI', 'ADI', 'REGN', 'ADSK',
          'LRCX', 'KHC', 'CTSH', 'ORLY', 'BIDU',
          'MNST', 'NXPI', 'SIRI', 'XEL', 'PAYX',
          'JD', 'EBAY', 'EA', 'WDAY', 'MELI',
          'PCAR', 'LULU', 'CTAS', 'KLAC', 'ALXN',
          'WLTW', 'VRSK', 'UAL', 'XLNX', 'NTES',
          'CERN', 'VRSN', 'MCHP', 'ALGN', 'DLTR',
          'IDXX', 'SNPS', 'FAST', 'INCY', 'ASML',
          'CDNS', 'CHKP', 'SWKS', 'TCOM', 'NLOK',
          'MXIM', 'WDC', 'CTXS', 'BMRN', 'NTAP',
          'EXPE', 'TTWO', 'ULTA', 'WYNN', 'HAS',
          'AAL', 'JBHT', 'FOXA', 'HSIC', 'MYL']


def get_price(original_price):
    new_price = float(original_price) * 100
    while new_price < 1:
        new_price = new_price * 10
    if new_price > 1000.0:
        new_price = new_price * 0.01
    return round(new_price, 4)


with open('trades.psv', 'r', newline='') as input_file:
    with open('enriched_trades.psv', 'w', newline='') as output_file:
        trades = csv.reader(input_file, delimiter='|')
        output = csv.writer(output_file, delimiter='|')
        output.writerow(["version", *next(trades, None)])
        for row in trades:
            stock = random.choice(stocks)
            stock_quantity = int(float(row[1]) * 1000)
            price = get_price(row[2])

            output.writerow(
                [1, stock, price, stock_quantity, row[3], row[4], row[5], row[6]])
            if random.random() > 0.2:
                for i in range(random.randint(1, 5)):
                    if random.randint(0, 1) == 1:
                        price_change = round(Decimal(random.uniform(-0.1, 0.1)), 2)
                        price = round(price_change.fma(Decimal(price), Decimal(price)), 4)

                    stock_change = round(Decimal(random.uniform(-0.1, 0.1)), 2)
                    stock_quantity = round(stock_change.fma(stock_quantity, stock_quantity), 0)
                    # TODO: modify timestamp for trade modifications
                    output.writerow(
                        [2 + i, stock, price, stock_quantity, row[3], row[4], row[5], row[6]])

