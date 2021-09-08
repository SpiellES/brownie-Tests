#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # выполнять откат цепи после завершения каждого теста, чтобы обеспечить надлежащую изоляцию
    pass


@pytest.fixture(scope="module")
def deposit(Deposit, accounts):
   return accounts[0].deploy(Deposit)
