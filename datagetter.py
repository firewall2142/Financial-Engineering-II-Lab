from yahoofinancials import YahooFinancials
import sys

# nse
# stocks = ['HDFC.NS', 'ITC.NS', 'ONGC.NS', 'SUNPHARMA.NS', 'GAIL.NS', 'COALINDIA.NS', 'GRASIM.NS', 'HEROMOTOCO.NS', 'TCS.NS', 'NTPC.NS']
# stocks = ['^NSEI']

# bo
# stocks = ['^BSESN']
stocks = ['ASIANPAINT.BO', 'BHARTIARTL.BO', 'BAJAJ-AUTO.BO', 'DRREDDY.BO', 'HCLTECH.BO', 'ICICIBANK.BO', 'INFY.BO', 'ITC.BO', 'LT.BO', 'NESTLEIND.BO']

# non indexed
# stocks = ['ASHOKLEY.NS', 'DABUR.BO', 'EDELWEISS.NS', 'GODREJPROP.BO', 'HONAUT.NS', 'IPCALAB.BO', 'OMAXE.NS', 'MRF.NS', 'PVR.BO', 'PFIZER.NS']
# stocks = stocks[:10]


yfstocks = YahooFinancials(stocks)

data = yfstocks.get_historical_price_data('2014-01-01', '2019-01-01', 'monthly')
print('recieved:: ', data, file=sys.stderr)
s = ""
print(','.join(['Date'] + stocks))
for i in range(len(data[stocks[0]]['prices'])):
    date = data[stocks[0]]['prices'][i]['formatted_date']
    s = date +',' + ','.join(list(map(str, [data[stk]['prices'][i]['adjclose'] for stk in stocks])))
    print(s)