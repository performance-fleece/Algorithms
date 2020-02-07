#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # define
    last_price = len(prices)
    cur_max_profit = prices[1] - prices[0]
    # get differences for each pairing
    for i in range(1, last_price):
        cur_min_price = i - 1
        check_price = i

        while check_price <= last_price and prices[check_price] - prices[cur_min_price] > cur_max_profit:

            new_max_profit = prices[check_price] - prices[cur_min_price]

            cur_max_profit = new_max_profit

            check_price += 1

    return cur_max_profit

    # save positive - discard negative

    # sort results
    # return highest


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
