import csv
import random
from decimal import Decimal
from datetime import datetime, timedelta
import uuid

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
    while new_price > 1000.0:
        new_price = new_price * 0.1
    return round(new_price, 4)


def write(output, id, version, stock, price, stock_quantity, time, buy_sell, market_limit):
    output.write("('{}', {}, '{}', {}, {}, '{}', '{}', '{}')".format(id, version, stock, price, stock_quantity, time, buy_sell, market_limit))
    output.write(",")
    output.write("\n")


with open('trades.psv', 'r', newline='') as input_file:
    with open('V1.0.1__data.sql', 'w', newline='') as output:
        trades = csv.reader(input_file, delimiter='|')
        next(trades, None)
        output.write("insert into reporting.trade_data (trade_id, version, stock, price, volume, valid_time_start, buy_sell_flag, market_limit_flag) values ")
        #TODO: figure out putting in valid_time_end for those with edits
        #TODO: figure out adding system time stamps
        for row in trades:
            stock = random.choice(stocks)
            stock_quantity = int(float(row[1]) * 1000)
            price = get_price(row[2])
            time = datetime.utcfromtimestamp(float(row[3]))
            id = uuid.uuid4()

            write(output, id, 1, stock, price, stock_quantity, time, row[4], row[5])
            if random.random() > 0.2:
                for i in range(1, random.randint(1, 5)):
                    if random.randint(0, 1) == 1:
                        price_change = round(Decimal(random.uniform(-0.1, 0.1)), 2)
                        price = round(price_change.fma(Decimal(price), Decimal(price)), 4)

                    time += timedelta(hours=random.randint(1, 5), minutes=random.randint(1, 30))
                    if random.randint(0, 1) == 1:
                        time += timedelta(days=random.randint(1, 3))

                    stock_change = round(Decimal(random.uniform(-0.1, 0.1)), 2)
                    stock_quantity = round(stock_change.fma(stock_quantity, stock_quantity), 0)
                    write(output, id, 1 + i, stock, price, stock_quantity, time, row[4], row[5])
        output.write(";")
