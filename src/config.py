import os
from os.path import join, dirname
from dotenv import load_dotenv
# from src.MyEncryptUtil import *
import datetime
import time

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

def getMnemonicPhrase():
    return os.environ.get("mnemonic")
    # cls = MyEncryptUtil()
    # return cls.decrypt(os.environ.get("key").encode(), os.environ.get("mnemonic").encode())

def getNetworkURL(chain):
    if chain == "ETH":
        network_url = os.environ.get("MAINNET")
    elif chain == "ROPSTEN":
        network_url = os.environ.get("ROPSTEN")
    elif chain == "RINKEBY":
        network_url = os.environ.get("RINKEBY")
    elif chain == "BSC":
        network_url = os.environ.get("BSC")
    elif chain == "POLYGON":
        network_url = os.environ.get("POLYGON")
    elif chain == "MUMBAI":
        network_url = os.environ.get("MUMBAI")
    elif chain == "MCHV":
        network_url = "https://rpc.oasys.mycryptoheroes.net/"
    elif chain == "SKALE":
        network_url = "https://mainnet.skalenodes.com/v1/green-giddy-denebola/"
    else:
        network_url = ""
    return network_url

class TokenAddress():
    SKALE_miningAddr = "0xE9d487B950A5075D8eaB084e2E04971340765b86"
    
def startAddressIndex():
    group = int(os.environ.get("group", 1))
    start = int(os.environ.get("startAddressIndex", -1))
    if start == -1:
        return (group - 1) * 10 + 1
    return start

def maxAddressIndex():
    group = int(os.environ.get("group", 1))
    max = int(os.environ.get("maxAddressIndex", -1))
    if max == -1:
        return group * 10
    return max

def airdropInterval():
    return float(os.environ.get("airdropInterval", 0.1))
