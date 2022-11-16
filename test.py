
from web3 import Web3
import json
import requests
from decimal import *

web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/460f40a260564ac4a4f4b3fffb032dad'))


if  web3.isConnected() == True:
    print("web3 connected...\n")
else :
    print("error connecting...")

account_1 = "0xc9fb7A911158336838D6c7A8a28E75Dee2925B15" ## add public key from first account (sender)
account_2 = "0x1a0cd5A94F4f52755E2EB869eD500371d459Ec62" ## add public key from second account (reciver)
private_key = "0x4795e3bc29f55c52f7aeaf020447844438e46e9f77f539a6748270beb2769a87" ## add ETH private key from first account (sender)

balance = 0
gas_fee = 21000*35
gas_fee = Decimal(gas_fee)
gas_fee = web3.fromWei(gas_fee,'Gwei')


#Get balance account
balance = web3.eth.getBalance(account_1)
balance = web3.fromWei(balance, "ether") #convert to ether value

balance = balance-gas_fee
# print(balance)
# print(balance)
# print(web3.fromWei(balance, "ether"))


#get nonce number
nonce = web3.eth.getTransactionCount(account_1)

#build transaction
tx = {
    'nonce':nonce,
    'to':account_2,
    'value':web3.toWei(balance,'ether'),
    'gas':21000,
    'gasPrice':web3.toWei('35','gwei')
}

#sign transaction with private key
signed_tx = web3.eth.account.signTransaction(tx,private_key)

#send Transaction
tx_hash= web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(web3.toHex(tx_hash))
