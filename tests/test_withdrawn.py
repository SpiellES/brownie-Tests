#!/usr/bin/python3
import time
import brownie
from brownie import Wei
from brownie import accounts


# ошибка из-за обнуления witdrawn в deposit()
def test_with_new_deposit(deposit):
    accounts[0].transfer(deposit, "2 ether")
    time.sleep(5)
    accounts[0].transfer(deposit, "0.0001 ether")
    accounts[0].transfer(deposit, "1 ether")
    after = deposit.getWithdrawn(accounts[0])   # members[_member].withdrawn

    assert after > 0


def test_without_new_deposit(deposit):
    accounts[0].transfer(deposit, "2 ether")
    time.sleep(5)
    accounts[0].transfer(deposit, "0.0001 ether")
    after = deposit.getWithdrawn(accounts[0])

    assert after > 0


def test_member_reward(deposit):
    accounts[0].transfer(deposit, "98 ether")
    before = accounts[0].balance()
    time.sleep(20)
    accounts[0].transfer(deposit, "0.0001 ether")
    after = accounts[0].balance()

    assert after > before + Wei("39 ether")


def test_withdraw_function(deposit):
    accounts[1].transfer(deposit, "4 ether")
    before = accounts[0].balance()
    deposit.withdraw(3, {'from': accounts[0]})
    after = accounts[0].balance()

    assert after > before + Wei("2 ether")


def test_revert_withdraw_function(deposit):
    accounts[1].transfer(deposit, "4 ether")
    with brownie.reverts():
        deposit.withdraw(5, {'from': accounts[0]})