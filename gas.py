import requests
import os
import psycopg2
import datetime


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


