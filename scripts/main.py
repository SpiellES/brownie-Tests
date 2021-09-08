#!/usr/bin/python3

from brownie import Deposit, accounts

def main():
    return Deposit.deploy({'from': accounts[0]})