import csv
import random

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


with open('trades.psv', 'r', newline='') as input_file:
    with open('enriched_trades.psv', 'w', newline='') as output_file:
        trades = csv.reader(input_file, delimiter='|')
        output = csv.writer(output_file, delimiter='|')
        output.writerow(next(trades, None))
        for row in trades:
            row.pop(0)
            price = float(row[1]) * 100
            while price < 1:
                price = price * 10
            if price > 1000.0:
                price = price * 0.01

            output.writerow([random.choice(stocks), price, int(float(row[0]) * 1000), row[2], row[3], row[4], row[5]])
            if random.random() > 0.2:
                print("need to add more data")
                for i in range(random.randint(1, 5)):
                    random.random()

