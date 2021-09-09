#!/usr/bin/python3
import pytest

from brownie import accounts


def test_active_refer_with_reward(deposit):
    accounts[1].transfer(deposit, "1 ether")  # активация рефера
    before = accounts[1].balance()
    accounts[0].transfer(deposit, data=accounts[1].address, amount="20 ether")
    acc = deposit.getReferer(accounts[0])

    assert acc == accounts[1].address
    assert accounts.at(acc).balance() == before + 4*10**18


def test_not_active_refer(deposit):
    accounts[0].transfer(deposit, data=accounts[1].address, amount="2 ether")
    acc = deposit.getReferer(accounts[0])

    assert acc == '0x0000000000000000000000000000000000000000'
