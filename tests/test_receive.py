#!/usr/bin/python3
import brownie

def test_withdraw(deposit, accounts):
    before = accounts[0].balance()
    accounts[0].transfer(deposit, "1 ether")
    after = accounts[0].balance()
    assert before == after