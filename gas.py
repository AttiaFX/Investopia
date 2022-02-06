import requests
import os
import psycopg2
import datetime
import yagmail

def save_value(safe_gas_price, propose_gas_price, suggest_base_fee):
    #Establishing the connection
    #Remember to set these variables using export in the terminal
    conn = psycopg2.connect(
        database=os.environ["DB_NAME"], 
        user=os.environ["DB_USER"], 
        password=os.environ["DB_PASSWORD"], 
        host=os.environ["DB_HOST"], 
        port=os.environ["DB_PORT"]
    )

    #Setting auto commit false
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Add values to database
    sql=f"INSERT INTO gas (safe_gas_price, propose_gas_price, suggest_base_fee, date) VALUES ({safe_gas_price}, {propose_gas_price}, {suggest_base_fee}, '{datetime.datetime.now()}');"
    cursor.execute(sql)

    # Commit your changes in the database
    conn.commit()
    print(f"safe_gas_price:{safe_gas_price}, propose_gas_price:{propose_gas_price}, suggest_base_fee:{suggest_base_fee}")

    #Closing the connection
    conn.close()

def send_email_alert(gas):
    # Alert the user of the occurance of optimum gas fees by email
    alert_recipient = "20086638@mail.wit.ie" 
    if gas < 85:
        print(f"Sending Gas Fee alerts to {alert_recipient} ... ")
        alert_body = f"ETH Fees have reached a cost-effective rate of {propose_gas_price} at {datetime.datetime.now()}"
        email = yagmail.SMTP(alert_recipient)
        email.send(
            to=alert_recipient,
            subject="ETH Gas Fee Tracker - Threshold Hit!",
            contents=alert_body
        )
        print("Alert Sent!")

if __name__ == "__main__":    
    # remember to set the ETHERSCAN_API_TOKEN variable
    api_token = os.environ["ETHERSCAN_API_TOKEN"]
    url = f"https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={api_token}"
    response = requests.get(url)
    data = response.json()
    safe_gas_price = data["result"]["SafeGasPrice"]
    propose_gas_price = data["result"]["ProposeGasPrice"]
    suggest_base_fee = data["result"]["suggestBaseFee"]
    save_value(safe_gas_price, propose_gas_price, suggest_base_fee)
    send_email_alert(int(propose_gas_price))
    print(f"High {safe_gas_price}, Medium {propose_gas_price}, Low {suggest_base_fee} ... ")
