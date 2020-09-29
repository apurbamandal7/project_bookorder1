# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:29:35 2020

@author: Mandal Apurba
"""




def place_market_order():

    price = int(input("Enter price. It should be greater the limit order: "))
    limit_order = int(input("Enter limit order: "))
    order_book = dict()      
    while(price >= limit_order):
       ask_size = int(input("Enter ask size: "))
       order_book[price] = ask_size
       price = price - 1
       
    print("The order book is")
    print("Price", " " , "Ask size")
    for keys, values in order_book.items():
        print(keys, " ", values)
        
    number_of_bid_size = int(input("Enter the number of bid size: "))
    j = 0
    order_book2 = dict()
    while(j < number_of_bid_size):
        bid_size = int(input("Enter bid size: "))
        price = int(input("Enter price: "))
        order_book2[price] = bid_size
        j = j + 1
    print("The order book is")
    print("Price", " ", "Bid size")
    for keys, values in order_book2.items():
        print(keys," ", values)
        
    return order_book
    return order_book2
        

def cancel_particular_order(order_book1, order_book2):
    the_ask_order = input("Enter the ask size to delete: ")
    for i in order_book1:
        if i == the_ask_order:
            del the_ask_order
    e = input("Do you want to delete a bid size? Y/N")
    while(e):
        the_bid_order = int(input("Enter the bid size to delete: "))
        for j in order_book2:
            if j == the_bid_order:
                del the_bid_order
place_market_order()
