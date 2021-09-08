#!/usr/bin/python3
import pytest

from brownie import accounts

#ошибка в getBalance при балансе контракта <1 eth
def test_balance_Less_1Eth(deposit, accounts):
    accounts[0].transfer(deposit, "0.3 ether")
    bal = deposit.getBalance({'from': accounts[0]})
    assert bal > 0

def test_balance_More_1Eth(deposit, accounts):
    accounts[0].transfer(deposit, "2.6 ether")
    bal = deposit.getBalance({'from': accounts[0]})
    assert bal == 2


def test_balance_1Eth(deposit, accounts):
    accounts[0].transfer(deposit, "1 ether")
    bal = deposit.getBalance({'from': accounts[0]})
    assert bal == 1
