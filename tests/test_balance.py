#!/usr/bin/python3
import pytest

from brownie import accounts

#ошибка в getBalance при балансе контракта <1 eth
def test_error(deposit, accounts):
    accounts[0].transfer(deposit, "0.3 ether")
    bal = deposit.getBalance({'from': accounts[0]})
    assert bal > 0

def test_right(deposit, accounts):
    accounts[0].transfer(deposit, "2 ether")
    bal = deposit.getBalance({'from': accounts[0]})
    assert bal == 2


