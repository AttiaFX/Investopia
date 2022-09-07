import yfinance 
import time
import yagmail


usd_score = 0
btc_score = 0
eth_score = 0
ada_score = 0

time_frame = '1h'
moving_average_value = 200
alert_recipient = "20086638@mail.wit.ie"
pw_email = ""



def is_stronger(pair):
    # True if the first currency is stronger than the second one
    # E.g. True if BTC/USD price is above the moving average
    current_pair = yfinance.download(pair, interval=time_frame, period='7mo').Close
    current_pair = current_pair.sort_index(ascending=False) 
    current_pair = current_pair[1:] 
    current_pair = current_pair[:moving_average_value] 
    price = current_pair[0] 
    ma_value = current_pair.sum()/moving_average_value
    is_stronger = price > ma_value
    return is_stronger

if __name__ == "__main__":
    print("Digital Asset Signal Service (DASS)")
    print("Version. 1.1")
    time.sleep(1)

    time_frame = input("Enter desired Time-Frame setting(15m, 30m, 60m, 1d):")
    pw_email = input("What is your email password?")

    print(f"Time-Frame setting: {time_frame}")
    print(f"Moving Average period setting : {moving_average_value}")
    time.sleep(1)
    print(f"Ranking the top digital currencies ...")
    time.sleep(1)
    
    # btc-usd
    if is_stronger('btc-usd'):
        btc_score = btc_score + 1
        usd_score = usd_score - 1
    else:
        btc_score = btc_score - 1
        usd_score = usd_score + 1
    # eth-usd
    if is_stronger('eth-usd'):
        eth_score = eth_score + 1
        usd_score = usd_score - 1
    else:
        eth_score = eth_score - 1
        usd_score = usd_score + 1
    # ada-usd
    if is_stronger('ada-usd'):
        ada_score = ada_score + 1
        usd_score = usd_score - 1
    else:
        ada_score = ada_score - 1
        usd_score = usd_score + 1
    # eth-btc
    if is_stronger('eth-btc'):
        eth_score = eth_score + 1
        btc_score = btc_score - 1
    else:
        eth_score = eth_score - 1
        btc_score = btc_score + 1
    # ada-btc
    if is_stronger('ada-btc'):
        ada_score = ada_score + 1
        btc_score = btc_score - 1
    else:
        ada_score = ada_score - 1
        btc_score = btc_score + 1
    # ada-eth
    if is_stronger('ada-eth'):
        ada_score = ada_score + 1
        eth_score = eth_score - 1
    else:
        ada_score = ada_score - 1
        eth_score = eth_score + 1

    # Assessing which asset is the strongest/weakest
    each_asset_score_dictionary = {"USD": usd_score, "BTC": btc_score, "ETH": eth_score, "ADA": ada_score} 
    asset_to_buy = max(each_asset_score_dictionary, key=each_asset_score_dictionary.get)
    asset_to_sell = min(each_asset_score_dictionary, key=each_asset_score_dictionary.get)

    print(f"Relative strength scores are shown below: ")
    print(f"USD: {usd_score}")
    print(f"BTC: {btc_score}")
    print(f"ETH: {eth_score}")
    print(f"ADA: {ada_score}")
    print(f"ADVICE: Buy {asset_to_buy} and Sell {asset_to_sell}")

    # Sending the investment advice as an alert via email
    print(f"Current investment advice is being sent to {alert_recipient} ... ")
    alert_body = f"Hi Investor, based on a relative strength comparision using the {time_frame} Time-Frame and {moving_average_value} Moving Average; the strongest asset is {asset_to_buy} while the weakest asset is {asset_to_sell}, hence current market dynamics suggest a position to BUY {asset_to_buy} while selling {asset_to_sell}"
    email = yagmail.SMTP(alert_recipient, pw_email)
    email.send(to=alert_recipient,subject="Relative Strength Measurement Tool - Investment Signal", contents=alert_body)
    print("Done !")
