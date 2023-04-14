# Stock Analysis Suite
<h3> This python file contains a tool that can be used to backtest stocks current day based on a trading strategy centered around the MACD of a stock. </h3>

  * MACD stands for Moving Average Convergence Divergence and is measured in the difference between the 12 and 26 exponential moving averages.
  * And is a simple indicator to find possible enter and exit positions.

<hr>

<h3> Specifically, the program includes: </h3>

* A QuickFilter to check a list of stock Tickers for a successful indication
  * Printing a list of stocks starting from the most recent indication. 
  * The user has the option to write this output to results.csv
* A Backtester to check how well the strategy works across a certain number of months (can go up to the entire history of the stock with little delay)
  * Outputs a Dataframe that you have the option to write to results.csv
* A Plot function (over a time period of months)
  * Outputs an mplfinance plot with multiple pannels showing a variety of indicators
* An Analyze Function to decide whether to see the current status of single stock 
  * Outputs the status of the MACD of the stock as well as the action according to the strategy (not financial advice) 
<hr>
<h5> This is by no means financial advice and is simply meant for you to add your own strategy to. </h5>
