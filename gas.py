import requests
import os

if __name__ == "__main__":
    # api_token = "7D8W6IGNBH967ECR2IN1K5VV2Q1IP9R5U6"
    api_token = os.environ["ETHERSCAN_API_TOKEN"]
    url = f"https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={api_token}"
    response = requests.get(url)
    data = response.json()
    fee = data["result"]["suggestBaseFee"]
    print(fee)