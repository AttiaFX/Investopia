![big-data-risk-management-in-financial-markets](https://user-images.githubusercontent.com/47541895/131925749-3a8e2089-655c-47cb-bf49-cdb13865da0a.jpeg)

Investopia consists of two applications:  1) Digital Asset Signal Service (DASS) &
                                          2) ETH Network Gas Fee Analytics Tool


# Digital Asset Signal Service (DASS)

## Description
This application is a relative strength comparison tool for financial assets. 
DASS helps to quickly identify the best opporunities for profit potential! 
Investopia can trawl through millions of data-points across global markets and quickly identify the weakest and strongest assets from a custom basket of financial instruments.

## Inputs
* Time Frame setting (1h by default)
* Moving Average period setting (200 SMA by default)
* email address of signal recipient

## Digital Asset Pairs
1. BTC/USD
1. ETH/USD
1. ADA/USD
1. ETH/BTC
1. ADA/BTC
1. ADA/ETH

## Relative Strength Comparison Logic
|     | USD  | BTC  |  ETH | ADA  |
| --- | ---- | ---- | ---- | ---- |
| USD |  x   |  1   |  1   |   1  |
| BTC |  -1  |  x   |  -1  |   1  |
| ETH |  -1  |  1   |  x   |   1  |
| ADA |  -1  |  -1  |  -1  |  x   |
|  Σ  |  -3  |  1   |  -1  |  3   |

## Rankings Example
1. ADA (+3)
1. BTC (+1)
1. ETH (-1)
1. USD (-3)

# ETH Network Gas Fee Analytics Tool

## Description
Investopia's Gas Fee Tracker uses real-time API data directly from global leaders in blockchain metrics to deliver execution timing suggestions and email alerts to help the user eliminate costly network fees while trading.
