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

def test_member_reward(deposit, accounts):
    accounts[0].transfer(deposit, "98 ether")
    before = accounts[0].balance()
    time.sleep(20)
    accounts[0].transfer(deposit, "0.0001 ether")
    after = accounts[0].balance()
    assert after > before + 39*10**18

def test_withdraw_function(deposit, accounts):
    accounts[1].transfer(deposit, "4 ether")
    before = accounts[0].balance()
    deposit.withdraw(3, {'from': accounts[0]})
    after = accounts[0].balance()
    assert after > before + 2*10**18