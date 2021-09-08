#!/usr/bin/python3

from brownie import Deposit, accounts

def main():
    t=Deposit.deploy({'from': accounts[0]})
    print(t)
    return