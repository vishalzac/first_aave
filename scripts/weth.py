from brownie import interface, network, config, config
from scripts.helpful import get_account

# 0.1 * 10**18 = 1ether


def main():
    weth()


def weth():
    account = get_account()
    dep = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = dep.deposit({"from": account, "value": 0.1 * 10**18})
    tx.wait(1)
    print("received 0.1  weth")
    return tx
