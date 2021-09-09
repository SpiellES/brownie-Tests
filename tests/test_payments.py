#!/usr/bin/python3

import pytest
import brownie
from brownie import accounts
from brownie.network.transaction import TransactionReceipt


@pytest.mark.parametrize('i', [1, 5])
def test_many_payments(deposit, i):
    all_value = 0

    for j in range(i):
        tx = accounts[0].transfer(deposit, i*10**18)
        value, time = deposit.getPayments(accounts[0].address, j)
        if j == 0:
            before = tx.timestamp

        assert before <= time      # "=" тк выполнение за милисекунды на локальном сервере
        assert value == i*10**18

        before = time              # далее сами payments сравниваем
        all_value += value

    assert all_value == deposit.getDeposit(accounts[0].address)


def test_send_less_than_min_eth(deposit):
    with brownie.reverts("Minimum 0.1 ETH"):
        accounts[0].transfer(deposit, "0.01 ether")
