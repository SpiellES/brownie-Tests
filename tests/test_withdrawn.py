#!/usr/bin/python3
import time
import brownie

#ошибка из-за обнуления witdrawn в deposit()
def test_with_New_Deposit(deposit, accounts):
    accounts[0].transfer(deposit, "2 ether")
    time.sleep(5)
    accounts[0].transfer(deposit, "0.0001 ether")
    accounts[0].transfer(deposit, "1 ether")
    after = deposit.getWithdrawn(accounts[0])
    assert after > 0

def test_without_New_Deposit(deposit, accounts):
    accounts[0].transfer(deposit, "2 ether")
    time.sleep(5)
    accounts[0].transfer(deposit, "0.0001 ether")
    after = deposit.getWithdrawn(accounts[0])
    assert after > 0