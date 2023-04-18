'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stuck then read the hint                     ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')


class Item:
    def __init__(self, type, description, amount: float, quantity: int):
        self.type = type
        self.description = description
        self._amount = amount
        self._quantity = quantity

    @property
    def amount(self):
        return self._clamp(self._amount, -1e6, 1e6)

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def quantity(self):
        return self._clamp(self._quantity, 0, 100)

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @staticmethod
    def _clamp(n, minn, maxn):
        return max(min(maxn, n), minn)


def validorder(order: Order):
    net = 0
    
    for item in order.items:
        if item.type == 'payment':
            net += item.amount
        elif item.type == 'product':
            net -= item.amount * item.quantity
        else:
            return("Invalid item type: %s" % item.type)
    
    if (net - 0.0) < 0.0:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
