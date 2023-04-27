import os
import pandas as pd
import yfinance as yf
import pandas_ta as pta
import mplfinance as mpf
import math
import numpy as np

# --------------------------------------------------------------------------------------
# VARIABLES
stocks_dow = ['AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'CSCO', 'CVX', 'DIS', 'DOW', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH', 'V', 'VZ', 'WBA', 'WMT']
stocks_spy = ['A', 'AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABT', 'ACGL', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADSK', 'AEE', 'AEP', 'AES', 'AFL', 'AIG', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN', 'ALK', 'ALL', 'ALLE', 'AMAT', 'AMCR', 'AMD', 'AME', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANET', 'ANSS', 'AON', 'AOS', 'APA', 'APD', 'APH', 'APTV', 'ARE', 'ATO', 'ATVI', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AZO', 'BA', 'BAC', 'BALL', 'BAX', 'BBWI', 'BBY', 'BDX', 'BEN', 'BF-B', 'BIIB', 'BIO', 'BK', 'BKNG', 'BKR', 'BLK', 'BMY', 'BR', 'BRK-B', 'BRO', 'BSX', 'BWA', 'BXP', 'C', 'CAG', 'CAH', 'CARR', 'CAT', 'CB', 'CBOE', 'CBRE', 'CCI', 'CCL', 'CDAY', 'CDNS', 'CDW', 'CE', 'CEG', 'CF', 'CFG', 'CHD', 'CHRW', 'CHTR', 'CI', 'CINF', 'CL', 'CLX', 'CMA', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF', 'COO', 'COP', 'COST', 'CPB', 'CPRT', 'CPT', 'CRL', 'CRM', 'CSCO', 'CSGP', 'CSX', 'CTAS', 'CTLT', 'CTRA', 'CTSH', 'CTVA', 'CVS', 'CVX', 'CZR', 'D', 'DAL', 'DD', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DISH', 'DLR', 'DLTR', 'DOV', 'DOW', 'DPZ', 'DRI', 'DTE', 'DUK', 'DVA', 'DVN', 'DXC', 'DXCM', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'ELV', 'EMN', 'EMR', 'ENPH', 'EOG', 'EPAM', 'EQIX', 'EQR', 'EQT', 'ES', 'ESS', 'ETN', 'ETR', 'ETSY', 'EVRG', 'EW', 'EXC', 'EXPD', 'EXPE', 'EXR', 'F', 'FANG', 'FAST', 'FCX', 'FDS', 'FDX', 'FE', 'FFIV', 'FIS', 'FISV', 'FITB', 'FLT', 'FMC', 'FOX', 'FOXA', 'FRC', 'FRT', 'FSLR', 'FTNT', 'FTV', 'GD', 'GE', 'GEHC', 'GEN', 'GILD', 'GIS', 'GL', 'GLW', 'GM', 'GNRC', 'GOOG', 'GOOGL', 'GPC', 'GPN', 'GRMN', 'GS', 'GWW', 'HAL', 'HAS', 'HBAN', 'HCA', 'HD', 'HES', 'HIG', 'HII', 'HLT', 'HOLX', 'HON', 'HPE', 'HPQ', 'HRL', 'HSIC', 'HST', 'HSY', 'HUM', 'HWM', 'IBM', 'ICE', 'IDXX', 'IEX', 'IFF', 'ILMN', 'INCY', 'INTC', 'INTU', 'INVH', 'IP', 'IPG', 'IQV', 'IR', 'IRM', 'ISRG', 'IT', 'ITW', 'IVZ', 'J', 'JBHT', 'JCI', 'JKHY', 'JNJ', 'JNPR', 'JPM', 'K', 'KDP', 'KEY', 'KEYS', 'KHC', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KR', 'L', 'LDOS', 'LEN', 'LH', 'LHX', 'LIN', 'LKQ', 'LLY', 'LMT', 'LNC', 'LNT', 'LOW', 'LRCX', 'LUMN', 'LUV', 'LVS', 'LW', 'LYB', 'LYV', 'MA', 'MAA', 'MAR', 'MAS', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'META', 'MGM', 'MHK', 'MKC', 'MKTX', 'MLM', 'MMC', 'MMM', 'MNST', 'MO', 'MOH', 'MOS', 'MPC', 'MPWR', 'MRK', 'MRNA', 'MRO', 'MS', 'MSCI', 'MSFT', 'MSI', 'MTB', 'MTCH', 'MTD', 'MU', 'NCLH', 'NDAQ', 'NDSN', 'NEE', 'NEM', 'NFLX', 'NI', 'NKE', 'NOC', 'NOW', 'NRG', 'NSC', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NVR', 'NWL', 'NWS', 'NWSA', 'NXPI', 'O', 'ODFL', 'OGN', 'OKE', 'OMC', 'ON', 'ORCL', 'ORLY', 'OTIS', 'OXY', 'PARA', 'PAYC', 'PAYX', 'PCAR', 'PCG', 'PEAK', 'PEG', 'PEP', 'PFE', 'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKG', 'PKI', 'PLD', 'PM', 'PNC', 'PNR', 'PNW', 'POOL', 'PPG', 'PPL', 'PRU', 'PSA', 'PSX', 'PTC', 'PWR', 'PXD', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'RE', 'REG', 'REGN', 'RF', 'RHI', 'RJF', 'RL', 'RMD', 'ROK', 'ROL', 'ROP', 'ROST', 'RSG', 'RTX', 'SBAC', 'SBNY', 'SBUX', 'SCHW', 'SEDG', 'SEE', 'SHW', 'SIVB', 'SJM', 'SLB', 'SNA', 'SNPS', 'SO', 'SPG', 'SPGI', 'SRE', 'STE', 'STLD', 'STT', 'STX', 'STZ', 'SWK', 'SWKS', 'SYF', 'SYK', 'SYY', 'T', 'TAP', 'TDG', 'TDY', 'TECH', 'TEL', 'TER', 'TFC', 'TFX', 'TGT', 'TJX', 'TMO', 'TMUS', 'TPR', 'TRGP', 'TRMB', 'TROW', 'TRV', 'TSCO', 'TSLA', 'TSN', 'TT', 'TTWO', 'TXN', 'TXT', 'TYL', 'UAL', 'UDR', 'UHS', 'ULTA', 'UNH', 'UNP', 'UPS', 'URI', 'USB', 'V', 'VFC', 'VICI', 'VLO', 'VMC', 'VRSK', 'VRSN', 'VRTX', 'VTR', 'VTRS', 'VZ', 'WAB', 'WAT', 'WBA', 'WBD', 'WDC', 'WEC', 'WELL', 'WFC', 'WHR', 'WM', 'WMB', 'WMT', 'WRB', 'WRK', 'WST', 'WTW', 'WY', 'WYNN', 'XEL', 'XOM', 'XRAY', 'XYL', 'YUM', 'ZBH', 'ZBRA', 'ZION', 'ZTS']
stocks_prefered = ['AAPL', 'AMD', 'AMZN', 'ANET', 'CASY', 'CMG', 'CNI', 'COST', 'CRWD', 'CSX', 'DIS', 'FHI', 'GOOG', 'GXO', 'HAS', 'HD', 'IBKR', 'KDP', 'KMI', 'KO', 'LUV', 'MA', 'MCD', 'MCK', 'MDLZ', 'META', 'MSFT', 'NFLX', 'NKE', 'NVDA', 'PAYC', 'PG', 'PYPL', 'ROL', 'SBUX', 'SHOP', 'SHW', 'SNOW', 'TSLA', 'TTWO', 'TXRH', 'UNH', 'UPS', 'V', 'VZ', 'WFC', 'WMT', 'WSM', 'WSO', 'XOM', 'XPO']
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
    print("(1) Prefered Stocks\n(2) S&P500\n(3) Dow Jones Industrial Average\n(4) Enter Single Stock")
    file_num = int(input(":  "))
    if file_num == 1:
        stocks = stocks_prefered
    elif file_num == 2:
        stocks = stocks_spy
    elif file_num == 3:
        stocks = stocks_dow
    elif file_num == 4:
        stocks = [input('\nTicker:  ').upper()]

    scores = pd.DataFrame(columns=['Ticker', 'Cycle Length'])
    all_scores = pd.DataFrame(columns=['Ticker', 'MACD', 'Cycle Length'])
    for i in range(len(stocks)):
        df = yf.download(stocks[i], period='12mo')
        result = check_quickfilter(df)
        
        if result['status'] == True:
            scores.loc[len(scores)] = [stocks[i], result['date']]
            all_scores.loc[i] = [stocks[i], result['status'], result['date']]
    scores.sort_values(by='Cycle Length', inplace=True, ignore_index=True)

    print("\nRESULTS\n")
    if len(scores) != 0:
        print(scores)
        write_data = input('\nWrite data to results.csv (y/n):  ')
        if write_data == 'y':
            scores.to_csv('results.csv')
    else:
        print(all_scores)
        write_data = input('\nWrite data to results.csv (y/n):  ')
        if write_data == 'y':
            all_scores.to_csv('results.csv')
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
    df = yf.download(ticker, period='12mo')
    macd = pd.DataFrame()
    macd['ema_slow'] = df['Close'].ewm(span=12).mean()
    macd['ema_fast'] = df['Close'].ewm(span=26).mean()
    macd['macd'] = macd['ema_slow'] - macd['ema_fast']
    macd['signal'] = macd['macd'].ewm(span=9).mean()
    macd['diff'] = macd['macd'] - macd['signal']
    macd['bar_positive'] = macd['diff'].map(lambda x: x if x > 0 else 0)
    macd['bar_negative'] = macd['diff'].map(lambda x: x if x < 0 else 0)

    upline = macd['macd'].iloc[[-1]].max()
    downline = macd['signal'].iloc[[-1]].max()
    macd_change = (upline - downline)
    macd_change /= abs(downline)
    macd_change *= 100

    i = 0
    macd_days = 0
    while True:
        i += 1
        if macd['diff'].iloc[[-i]].max() > 0:
            macd_days += 1
        else:
            break
    
    if macd['diff'].iloc[[-1]].max() <= 0:
        print('MACD is negative by a margin of {}%\nDo not buy new trade and sell current trade'.format(round(macd_change, 4)))
    elif macd_change <= 2:
        print('MACD is positive but by a margin of {}%\nBuy new trade or sell current trade'.format(round(macd_change, 4)))
        print('\nThe MACD cycle has continued for {} days'.format(macd_days))
    else:
        print('MACD is positive and by a margin of {}%\nBuy new trade and do not sell current trade'.format(round(macd_change, 4)))
        print('\nThe MACD cycle has continued for {} days'.format(macd_days))
    
    derivative = (macd['macd'].iloc[[-1]].max() - macd['macd'].iloc[[-2]].max()) / 2
    print("MACD Derivative:  {}".format(derivative))

    total_derivative = 0
    for i in range(len(macd)-1):
        total_derivative += (macd['macd'].iloc[[i+1]].max() - macd['macd'].iloc[[i]].max()) / 2
    total_derivative /= (len(macd) - 1)
    print("Yearly Average Derivative:  {}".format(total_derivative))
  

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
            upline = macd['macd'].iloc[[time+count]].max()
            downline = macd['signal'].iloc[[time+count]].max()
            macd_change = (upline - downline)
            macd_change /= abs(downline)
            macd_change *= 100
            if (len(stock_df)-3) < (count+time):
                price_sell = stock_df['Close'].iloc[count+time].max()
                sell = True
            elif macd['diff'].iloc[[time+count]].max() <= 0 or macd_change <= 0.2:
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

    results = pd.DataFrame(columns=['Ticker', 'Trade % Change', 'Stock % Change','End Money', '% Trade Success', 'Total Trades', 'Min Money', 'Max Money'])

    count = 0
    while count < len(stocks):
        stock = stocks[count]
        df = yf.download(stock, period='{}mo'.format(period))
        long_df = yf.download(stock, period='{}mo'.format(math.ceil(len(df)/22) + 5))

        # MACD
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

        money = 10000
        bought = False
        total_transactions = 0
        profit_transactions = 0
        max_value = 10000
        min_value = 10000

        for i in range(len(df)-2):
            if bought == True:
                if i >= stock_transaction[2]:
                    bought = False
            else:
                time = i
                stock_transaction = transaction(macd, df, time)
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

        results.loc[len(results.index)] = [stock.strip("\n"), round(((money-10000)/10000)*100, 3), round(((df['Close'].iloc[[-1]].max() - df['Close'].iloc[[0]].max())/df['Close'].iloc[[0]].max())*100, 3),money, profit_percent, total_transactions, min_value, max_value]

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
