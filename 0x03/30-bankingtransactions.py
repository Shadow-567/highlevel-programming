#!/usr/bin/python3
""" module that checks for bank transactions"""


transactions = [
    (101, 500, "deposit"),
    (102, 200, "withdrawal"),
    (103, 1000, "deposit"),
    (104, 300, "withdrawal")
]


def deposit(action, account):
    transaction_id, amount, type = action
    account += amount
    return account

def withdrawal(action, account):
    transaction_id, amount, type = action
    history = []
    if account <= amount:
        return "Insufficient Funds"
    else:
        history.append(action)
        account -= amount
    return [data for data in history if data[1] >= 250]

def  transact(actions=[]):
    result = []
    account = 0
    for action in actions:
        if "deposit" in action:
            account += deposit(action, account)
        elif "withdrawal" in action:
            result.extend(withdrawal(action, account))
        else:
            return "Invalid transaction type"
    return result

if __name__ == "__main__":
    result = transact(transactions)
    print(result)