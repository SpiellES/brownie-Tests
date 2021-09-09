#!/usr/bin/python3
import pytest

import brownie
from brownie import accounts


# ошибка в getBalance при балансе контракта <1 eth
def test_balance_less_1eth(deposit):
    accounts[0].transfer(deposit, "0.3 ether")
    bal = deposit.getBalance({'from': accounts[0]})

    assert bal > 0


def test_balance_1eth(deposit):
    accounts[0].transfer(deposit, "1 ether")
    bal = deposit.getBalance({'from': accounts[0]})

    assert bal == 1


def test_balance_more_1eth(deposit):
    accounts[0].transfer(deposit, "2.6 ether")
    bal = deposit.getBalance({'from': accounts[0]})

    assert bal == 2


def test_balance_not_owner(deposit):
    accounts[1].transfer(deposit, "3 ether")
    with brownie.reverts("Caller is not owner"):
        deposit.getBalance({'from': accounts[4]})