import os
import pandas as pd
import yfinance as yf
import pandas_ta as pta
import mplfinance as mpf
import math
import datetime
from dateutil.relativedelta import relativedelta
import numpy as np
import pandas_datareader.data as web

# --------------------------------------------------------------------------------------
# VARIABLES
stocks_dow = ['AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'CSCO', 'CVX', 'DIS', 'DOW', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH', 'V', 'VZ', 'WBA', 'WMT']
stocks_spy = ['A', 'AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABT', 'ACGL', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADSK', 'AEE', 'AEP', 'AES', 'AFL', 'AIG', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN', 'ALK', 'ALL', 'ALLE', 'AMAT', 'AMCR', 'AMD', 'AME', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANET', 'ANSS', 'AON', 'AOS', 'APA', 'APD', 'APH', 'APTV', 'ARE', 'ATO', 'ATVI', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AZO', 'BA', 'BAC', 'BALL', 'BAX', 'BBWI', 'BBY', 'BDX', 'BEN', 'BF-B', 'BIIB', 'BIO', 'BK', 'BKNG', 'BKR', 'BLK', 'BMY', 'BR', 'BRK-B', 'BRO', 'BSX', 'BWA', 'BXP', 'C', 'CAG', 'CAH', 'CARR', 'CAT', 'CB', 'CBOE', 'CBRE', 'CCI', 'CCL', 'CDAY', 'CDNS', 'CDW', 'CE', 'CEG', 'CF', 'CFG', 'CHD', 'CHRW', 'CHTR', 'CI', 'CINF', 'CL', 'CLX', 'CMA', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF', 'COO', 'COP', 'COST', 'CPB', 'CPRT', 'CPT', 'CRL', 'CRM', 'CSCO', 'CSGP', 'CSX', 'CTAS', 'CTLT', 'CTRA', 'CTSH', 'CTVA', 'CVS', 'CVX', 'CZR', 'D', 'DAL', 'DD', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DISH', 'DLR', 'DLTR', 'DOV', 'DOW', 'DPZ', 'DRI', 'DTE', 'DUK', 'DVA', 'DVN', 'DXC', 'DXCM', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'ELV', 'EMN', 'EMR', 'ENPH', 'EOG', 'EPAM', 'EQIX', 'EQR', 'EQT', 'ES', 'ESS', 'ETN', 'ETR', 'ETSY', 'EVRG', 'EW', 'EXC', 'EXPD', 'EXPE', 'EXR', 'F', 'FANG', 'FAST', 'FCX', 'FDS', 'FDX', 'FE', 'FFIV', 'FIS', 'FISV', 'FITB', 'FLT', 'FMC', 'FOX', 'FOXA', 'FRC', 'FRT', 'FSLR', 'FTNT', 'FTV', 'GD', 'GE', 'GEHC', 'GEN', 'GILD', 'GIS', 'GL', 'GLW', 'GM', 'GNRC', 'GOOG', 'GOOGL', 'GPC', 'GPN', 'GRMN', 'GS', 'GWW', 'HAL', 'HAS', 'HBAN', 'HCA', 'HD', 'HES', 'HIG', 'HII', 'HLT', 'HOLX', 'HON', 'HPE', 'HPQ', 'HRL', 'HSIC', 'HST', 'HSY', 'HUM', 'HWM', 'IBM', 'ICE', 'IDXX', 'IEX', 'IFF', 'ILMN', 'INCY', 'INTC', 'INTU', 'INVH', 'IP', 'IPG', 'IQV', 'IR', 'IRM', 'ISRG', 'IT', 'ITW', 'IVZ', 'J', 'JBHT', 'JCI', 'JKHY', 'JNJ', 'JNPR', 'JPM', 'K', 'KDP', 'KEY', 'KEYS', 'KHC', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KR', 'L', 'LDOS', 'LEN', 'LH', 'LHX', 'LIN', 'LKQ', 'LLY', 'LMT', 'LNC', 'LNT', 'LOW', 'LRCX', 'LUMN', 'LUV', 'LVS', 'LW', 'LYB', 'LYV', 'MA', 'MAA', 'MAR', 'MAS', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'META', 'MGM', 'MHK', 'MKC', 'MKTX', 'MLM', 'MMC', 'MMM', 'MNST', 'MO', 'MOH', 'MOS', 'MPC', 'MPWR', 'MRK', 'MRNA', 'MRO', 'MS', 'MSCI', 'MSFT', 'MSI', 'MTB', 'MTCH', 'MTD', 'MU', 'NCLH', 'NDAQ', 'NDSN', 'NEE', 'NEM', 'NFLX', 'NI', 'NKE', 'NOC', 'NOW', 'NRG', 'NSC', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NVR', 'NWL', 'NWS', 'NWSA', 'NXPI', 'O', 'ODFL', 'OGN', 'OKE', 'OMC', 'ON', 'ORCL', 'ORLY', 'OTIS', 'OXY', 'PARA', 'PAYC', 'PAYX', 'PCAR', 'PCG', 'PEAK', 'PEG', 'PEP', 'PFE', 'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKG', 'PKI', 'PLD', 'PM', 'PNC', 'PNR', 'PNW', 'POOL', 'PPG', 'PPL', 'PRU', 'PSA', 'PSX', 'PTC', 'PWR', 'PXD', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'RE', 'REG', 'REGN', 'RF', 'RHI', 'RJF', 'RL', 'RMD', 'ROK', 'ROL', 'ROP', 'ROST', 'RSG', 'RTX', 'SBAC', 'SBNY', 'SBUX', 'SCHW', 'SEDG', 'SEE', 'SHW', 'SIVB', 'SJM', 'SLB', 'SNA', 'SNPS', 'SO', 'SPG', 'SPGI', 'SRE', 'STE', 'STLD', 'STT', 'STX', 'STZ', 'SWK', 'SWKS', 'SYF', 'SYK', 'SYY', 'T', 'TAP', 'TDG', 'TDY', 'TECH', 'TEL', 'TER', 'TFC', 'TFX', 'TGT', 'TJX', 'TMO', 'TMUS', 'TPR', 'TRGP', 'TRMB', 'TROW', 'TRV', 'TSCO', 'TSLA', 'TSN', 'TT', 'TTWO', 'TXN', 'TXT', 'TYL', 'UAL', 'UDR', 'UHS', 'ULTA', 'UNH', 'UNP', 'UPS', 'URI', 'USB', 'V', 'VFC', 'VICI', 'VLO', 'VMC', 'VRSK', 'VRSN', 'VRTX', 'VTR', 'VTRS', 'VZ', 'WAB', 'WAT', 'WBA', 'WBD', 'WDC', 'WEC', 'WELL', 'WFC', 'WHR', 'WM', 'WMB', 'WMT', 'WRB', 'WRK', 'WST', 'WTW', 'WY', 'WYNN', 'XEL', 'XOM', 'XRAY', 'XYL', 'YUM', 'ZBH', 'ZBRA', 'ZION', 'ZTS']
stocks_prefered = ['AAPL', 'AMD', 'AMZN', 'ANET', 'CASY', 'CMG', 'CNI', 'COST', 'CRWD', 'CSX', 'DIS', 'FHI', 'GOOG', 'GXO', 'HAS', 'HD', 'IBKR', 'KDP', 'KMI', 'KO', 'LUV', 'MA', 'MCD', 'MCK', 'MDLZ', 'META', 'MSFT', 'NFLX', 'NKE', 'NVDA', 'PAYC', 'PG', 'PYPL', 'ROL', 'SBUX', 'SHOP', 'SHW', 'SNOW', 'TSLA', 'TTWO', 'TXRH', 'UNH', 'UPS', 'V', 'VZ', 'WFC', 'WMT', 'WSM', 'WSO', 'XOM', 'XPO']
# --------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------
# Beta Calculations
def downloadData(ticker):
    start, end = datetime.datetime.now() - relativedelta(years=5), datetime.datetime.now()
    data = web.DataReader(ticker, 'yahoo', start, end)
    data.reset_index(inplace=True)
    data.set_index("Date", inplace=True)
    return data

def processBeta(stockData, marketData, year, frequency, adjustment = 0):
    stockData, marketData = shortenData(stockData, marketData, year)
    stockData = stockData['Close'].resample(frequency).last().pct_change()
    marketData = marketData['Close'].resample(frequency).last().pct_change()
    stockData = stockData[stockData.index.isin(marketData.index)]
    marketData = marketData[marketData.index.isin(stockData.index)]        
    beta = calculateBeta(stockData, marketData)
    return adjustBeta(beta, adjustment)

def shortenData(stockData, marketData, year):
    if year == 5:
        return stockData, marketData
    array1 = stockData.index > datetime.datetime.now() - relativedelta(years=year)
    array2 = marketData.index > datetime.datetime.now() - relativedelta(years=year)
    stockData = stockData[[x for x in array1]]
    marketData = marketData[[x for x in array2]]
    return stockData, marketData

def calculateBeta(stockData, marketData):
    covariance = np.cov(stockData[1:], marketData[1:])
    variance = np.var(marketData[1:])
    return covariance[0,1] / variance

def adjustBeta(beta, adjustment):
    for i in range(adjustment):
        beta = 0.67 * beta + 0.33
    return beta

def beta(ticker_df, market_df = '^GSPC', adjusted = 0):
    beta1m5y = processBeta(ticker_df, market_df, 5, '1M', adjusted)
    beta1m3y = processBeta(ticker_df, market_df, 3, '1M', adjusted)
    beta1w5y = processBeta(ticker_df, market_df, 5, '1W', adjusted)
    beta1w3y = processBeta(ticker_df, market_df, 3, '1W', adjusted)
    beta1w1y = processBeta(ticker_df, market_df, 1, '1W', adjusted)
    beta1d1y = processBeta(ticker_df, market_df, 1, '1D', adjusted)

    #print(f'''{tickers[i]} Betas:\nMonthly 5 Years {beta1m5y}\nMonthly 3 Years {beta1m3y}\nWeekly 5 Years {beta1w5y}\nWeekly 3 Years {beta1w3y}\nWeekly 1 Year {beta1w1y}\nDaily 1 Year {beta1d1y}''')

    return [beta1m5y, beta1m3y, beta1w5y, beta1w3y, beta1w1y, beta1d1y]
# --------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------
# QUICKFILTER

def check_quickfilter(stock_df):
    stock_stat = {
        'status':False,
        'date':0
    }
    # MACD
    macd = pd.DataFrame()
    macd['ema_slow'] = stock_df['Close'].ewm(span=12).mean()
    macd['ema_fast'] = stock_df['Close'].ewm(span=26).mean()
    macd['macd'] = macd['ema_slow'] - macd['ema_fast']
    macd['signal'] = macd['macd'].ewm(span=9).mean()
    macd['diff'] = macd['macd'] - macd['signal']
    macd['bar_positive'] = macd['diff'].map(lambda x: x if x > 0 else 0)
    macd['bar_negative'] = macd['diff'].map(lambda x: x if x < 0 else 0)
    if macd['diff'].iloc[[-1]].max() > 0:
        stock_stat['status'] = True
        i = 0
        while True:
            i += 1
            if macd['diff'].iloc[[-i]].max() > 0:
                stock_stat['date'] += 1
            else:
                break
    return stock_stat

def filter():
    print("(1) Prefered Stocks\n(2) S&P500\n(3) Dow Jones Industrial Average")
    file_num = int(input(":  "))
    if file_num == 1:
        stocks = stocks_prefered
    elif file_num == 2:
        stocks = stocks_spy
    elif file_num == 3:
        stocks = stocks_dow

    scores = pd.DataFrame(columns=['Ticker', 'Cycle Length', '5 Year Monthly Beta'])
    market_df = yf.download('SPY', period='60mo')
    for i in range(len(stocks)):
        df = yf.download(stocks[i], period='60mo')
        result = check_quickfilter(df)
        
        if result['status'] == True:
            scores.loc[len(scores)] = [stocks[i], result['date'], beta(df, market_df)[0]]
    scores.sort_values(by='Cycle Length', inplace=True, ignore_index=True)

    print("\nRESULTS\n")
    print(scores)
    write_data = input('\nWrite data to results.csv (y/n):  ')
    if write_data == 'y':
        scores.to_csv('results.csv')
# --------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------
# PLOT

def MACD(df, ticker):
    long_df = yf.download(ticker, period='{}mo'.format(math.ceil(len(df)/22) + 5))
    macd = pd.DataFrame()
    macd['ema_slow'] = long_df['Close'].ewm(span=12).mean()
    macd['ema_fast'] = long_df['Close'].ewm(span=26).mean()
    macd['macd'] = macd['ema_slow'] - macd['ema_fast']
    macd['signal'] = macd['macd'].ewm(span=9).mean()
    macd['diff'] = macd['macd'] - macd['signal']
    macd['bar_positive'] = macd['diff'].map(lambda x: x if x > 0 else 0)
    macd['bar_negative'] = macd['diff'].map(lambda x: x if x < 0 else 0)
    while len(macd) != len(df):
        macd.drop(labels=macd.index[0], axis=0, inplace=True)
    return macd

def Stochastic(df):
	stochastic = pd.DataFrame()
	stochastic['%K'] = ((df['Close'] - df['Low'].rolling(14).min()) / (df['High'].rolling(14).max() - df['Low'].rolling(14).min())) * 100
	stochastic['%D'] = stochastic['%K'].rolling(3).mean()
	stochastic['%SD'] = stochastic['%D'].rolling(3).mean()
	stochastic['UL'] = 80
	stochastic['DL'] = 20
	return stochastic

def price_channel(df, day):
	price_channel = pd.DataFrame(df['Close'])
	price_channel.columns = ['max']
	price_channel.insert(1, 'min', pd.DataFrame(df['Close']))
	used_list = []
	for i in range(day):
		# Account for weekends in this using the number of entries and the number of days that they want. Number $day cannot exceed the number of entries 
		used_list.append(i)
		price_channel['max'].iloc[[max(used_list)]] = df['Close'].iloc[used_list].max()
		price_channel['min'].iloc[[max(used_list)]] = df['Close'].iloc[used_list].min()
	for i in range(len(price_channel) - day):
		used_list.pop(0)
		used_list.append(i + day)
		price_channel['max'].iloc[[max(used_list)]] = df['Close'].iloc[used_list].max()
		price_channel['min'].iloc[[max(used_list)]] = df['Close'].iloc[used_list].min()
	return price_channel
	
def plot(symbol, time):
	df = yf.download(symbol, period="{}mo".format(time))

	macd = MACD(df, symbol)
	stochastic = Stochastic(df)
	# min_max = price_channel(df, min_max_day)
	rsi = pta.rsi(df['Close'], length = 14)

	plots  = [
		#mpf.make_addplot((min_max), panel=0, secondary_y=False),
		mpf.make_addplot((rsi), panel=3, ylabel='RSI'),
		mpf.make_addplot((macd['macd']), color='#606060', panel=1, ylabel='MACD (12,26,9)', secondary_y=False),
	    mpf.make_addplot((macd['signal']), color='#1f77b4', panel=1, secondary_y=False),
	    mpf.make_addplot((macd['bar_positive']), type='bar', color='#4dc790', panel=1),
	    mpf.make_addplot((macd['bar_negative']), type='bar', color='#fd6b6c', panel=1),
	    mpf.make_addplot((stochastic[['%D', '%SD', 'UL', 'DL']]), ylim=[0, 100], panel=2, ylabel='Stoch (14,3)')
	]
        
	mpf.plot(df, type='candle', style='yahoo', volume=False, addplot=plots, panel_ratios=(6,2.5,2.5,2.5), mav=(20,55), title="{} Valuation Over {} Months".format(symbol, time))
	# mav=(20,55) is an option in the plot to activate SMAs of 20 and 55 days
# --------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------
# ANALYZE

def analyze(ticker):
    df = yf.download(ticker, period='60mo')
    macd = pd.DataFrame()
    macd['ema_slow'] = df['Close'].ewm(span=12).mean()
    macd['ema_fast'] = df['Close'].ewm(span=26).mean()
    macd['macd'] = macd['ema_slow'] - macd['ema_fast']
    macd['signal'] = macd['macd'].ewm(span=9).mean()
    macd['diff'] = macd['macd'] - macd['signal']
    macd['bar_positive'] = macd['diff'].map(lambda x: x if x > 0 else 0)
    macd['bar_negative'] = macd['diff'].map(lambda x: x if x < 0 else 0)
    all_derivative = [0]
    for i in range(len(macd) - 1):
        all_derivative.append((macd['diff'].iloc[[i+1]].max() - macd['diff'].iloc[[i]].max()) / 2)
    macd['derivative'] = all_derivative

    # MACD Separation
    upline = macd['macd'].iloc[[-1]].max()
    downline = macd['signal'].iloc[[-1]].max()
    macd_change = (upline - downline)
    macd_change /= abs(downline)
    macd_change *= 100

    # MACD Changes
    macd_movements = []
    for i in range(5):
        macd_movements.append((macd['derivative'].iloc[[-1 - i]].max()/abs(macd['diff'].iloc[[-1 - i]].max()))*100)
    macd_change_sum = 0
    for i in range(5):
        if macd_movements[i] <= 0:
            macd_change_sum += 1

    # Length of MACD
    i = 0
    macd_days = 0
    while True:
        i += 1
        if macd['diff'].iloc[[-i]].max() > 0:
            macd_days += 1
        else:
            break
    
    # BETA Value
    betas = beta(df, yf.download('SPY', period='60mo'))

    if macd['diff'].iloc[[-1]].max() <= 0:
        print('MACD is negative by a margin of {}%\nDo not buy new trade and sell current trade'.format(round(macd_change, 4)))
        print("\nMACD Changes:  ")
        for i in range(5):
            print("{}:  {}%".format(macd.index[-5 + i], round(macd_movements[i], 3)))
        print("\nBeta Value:  {}".format(betas[0]))
    elif macd_change_sum == 5:
        print('MACD is positive by a margin of {}%\nBuy new trade or sell current trade'.format(round(macd_change, 4)))
        print('\nThe MACD cycle has continued for {} days\n'.format(macd_days))
        print("MACD Changes:  ")
        for i in range(5):
            print("{}:  {}%".format(macd.index[-5 + i], round(macd_movements[i], 3)))
        print("\nBeta Value:  {}".format(betas[0]))
    else:
        print('MACD is positive by a margin of {}%\nBuy new trade and do not sell current trade'.format(round(macd_change, 4)))
        print('\nThe MACD cycle has continued for {} days\n'.format(macd_days))
        print("MACD Changes:  ")
        for i in range(5):
            print("{}:  {}%".format(macd.index[-5 + i], round(macd_movements[i], 3)))
        print("\nBeta Value:  {}".format(betas[0]))
# --------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------
# BACKCHECKER

def transaction(macd, stock_df, time):
    if macd['diff'].iloc[[time]].max() < 0:
        return [0, 0, 0, 'N']
    else:
        price_bought = stock_df['Close'].iloc[time].max()
        count = 0
        sell = False
        while sell == False:
            count +=1

            if (len(stock_df)-3) < (count+time):
                price_sell = stock_df['Close'].iloc[count+time].max()
                sell = True
            elif macd['diff'].iloc[[time+count]].max() <= 0:
                price_sell = stock_df['Close'].iloc[count+time].max()
                sell = True

        return [price_bought, price_sell, time+count, 'Y']

def backtest(period):
    print("\n(1) Prefered Stocks\n(2) S&P500\n(3) Dow Jones Industrial Average\n(4) Enter Single Stock")
    file_num = int(input(":  "))
    if file_num == 1:
        stocks = stocks_prefered
    elif file_num == 2:
        stocks = stocks_spy
    elif file_num == 3:
        stocks = stocks_dow
    elif file_num == 4:
        stocks = [input('\nTicker:  ').upper()]
    
    stocks.insert(0, "DIA\n")
    stocks.insert(0, "SPY\n")
    stocks.insert(0, "QQQ\n")

    results = pd.DataFrame(columns=['Ticker', 'Trade % Change', 'Stock % Change','End Money', '% Trade Success', 'Total Trades', 'Min Money', 'Max Money', '5 Year Monthly Beta'])

    market_df = yf.download('SPY', period='{}mo'.format(period))

    count = 0
    while count < len(stocks):
        stock = stocks[count]
        stock_df = yf.download(stock, period='{}mo'.format(period))
        beta_value = beta(stock_df, market_df)[0]

        if stock != 'DIA' and beta_value < 1 and file_num != 4:
            pass
        else:
            long_df = yf.download(stock, period='{}mo'.format(math.ceil(len(stock_df)/22) + 5))

            # MACD
            macd = pd.DataFrame()
            macd['ema_slow'] = long_df['Close'].ewm(span=12).mean()
            macd['ema_fast'] = long_df['Close'].ewm(span=26).mean()
            macd['macd'] = macd['ema_slow'] - macd['ema_fast']
            macd['signal'] = macd['macd'].ewm(span=9).mean()
            macd['diff'] = macd['macd'] - macd['signal']
            macd['bar_positive'] = macd['diff'].map(lambda x: x if x > 0 else 0)
            macd['bar_negative'] = macd['diff'].map(lambda x: x if x < 0 else 0)
            while len(macd) != len(stock_df):
                macd.drop(labels=macd.index[0], axis=0, inplace=True)

            money = 10000
            bought = False
            total_transactions = 0
            profit_transactions = 0
            max_value = 10000
            min_value = 10000

            for i in range(len(stock_df)-2):
                if bought == True:
                    if i >= stock_transaction[2]:
                        bought = False
                else:
                    time = i
                    stock_transaction = transaction(macd, stock_df, time)
                    if stock_transaction[3] == 'Y':
                        money += money*((stock_transaction[1]-stock_transaction[0]) / stock_transaction[0])
                        bought = True
                        total_transactions += 1

                    if stock_transaction[1] > stock_transaction[0]:
                        profit_transactions += 1
                    if money > max_value:
                        max_value = money
                    if money < min_value:
                        min_value = money

            if total_transactions != 0:
                profit_percent = round((profit_transactions / total_transactions)*100, 3)
            else:
                profit_percent = 0

            results.loc[len(results.index)] = [stock.strip("\n"), round(((money-10000)/10000)*100, 3), round(((stock_df['Close'].iloc[[-1]].max() - stock_df['Close'].iloc[[0]].max())/stock_df['Close'].iloc[[0]].max())*100, 3),money, profit_percent, total_transactions, min_value, max_value, beta_value]

        count += 1
    ave_profit = 0
    for i in range(len(results)-3):
        ave_profit += results['End Money'].iloc[[i+3]].max()
    ave_profit = ave_profit/(len(results)-3)
    ave_profit -= 10000
    final_success = 0
    total_trades = 0
    for i in range(len(results)-3):
        final_success += (results['% Trade Success'].iloc[[i+3]].max()/100)*results['Total Trades'].iloc[[i+3]].max()
        total_trades += results['Total Trades'].iloc[[i+3]].max()
    final_success /= total_trades
    final_success *= 100
    print("\nRESULTS\n")
    print(results)
    print("\nAverage Profit:  {}%".format(round((ave_profit/100), 3)))
    print("Average Success Rate:  {}%".format(round(final_success, 3)))
    write_data = input('\nWrite data to results.csv (y/n):  ')
    if write_data == 'y':
        results.to_csv('results.csv')
# --------------------------------------------------------------------------------------

while True:
    os.system("cls")
    print(" ----------------------------------------------------------------------------------------------------")
    print("                                        Technical Analysis")
    print(" ----------------------------------------------------------------------------------------------------")
    print(" ")
    print(" (1) QuickFilter Stocks")
    print(" (2) Backtest Stocks")
    print(" (3) Plot Stock")
    print(" (4) Analyze Stock")
    print(" (5) Exit App")
    print(" ")
    choice = input(": ")
    print(": ")
    
    if choice == "1":
        filter()
        input(": ")
    elif choice == "2":
        backtest(int(input("EX) 6, 8, 10, 12...\nOver what time period:  ")))
        input(": ")
    elif choice == "3":
        plot(input("Ticker:  ").upper(), int(input("EX) 2, 3, 6, 12...\nTime Period:  ")))
        input(": ")
    elif choice == "4":
        analyze(input("Ticker:  ").upper())
        input(": ")
    elif choice == "5":
        os._exit(0)
    else:
        pass
