# create relations
RELATION Customer "(Id num 4, Fname char 15, Lname char 15, Address char 30, Phone num 10)"
RELATION Pizza "(Id num 4, Toppings char 100)"
RELATION Order "(Id num 4, Cust_Id num 4, Order_date datetime  10, Pizza_Id num 4, Base_price num 5, Cost num 5)"
RELATION Topping "(Id num 4, Topping char 20, Price num 4)"
# insert Customer (Id, Fname, Lname, Address, Phone)
INSERT Customer 1000 John Smith '731 Fondren, Houston TX' 9857651234
INSERT Customer 1001 Franklin Wong '638 Voss, Houston TX' 9855552234
INSERT Customer 1002 Alicia Zelaya '3321 Castle, Spring TX' 5045559876
INSERT Customer 1003 Jennifer Wallace '291 Berry, Bellaire TX' 5048675309
INSERT Customer 1004 Ramesh Narayan '975 Fire Oak, Humble TX' 2555558764
INSERT Customer 1005 Joyce English '5631 Rice, Houston TX' 9855556734
# insert Pizza (Id, Toppings)
INSERT Pizza 3000 'Pepperoni,Cheese';
INSERT Pizza 3001 'Pineapple,Mushrooms';
INSERT Pizza 3002 'Anchovies';
INSERT Pizza 3003 'Cheese,Sausage';
INSERT Pizza 3004 'Cheese';
INSERT Pizza 3005 'Pepperoni,Mushrooms';
INSERT Pizza 3006 'Pineapple,Pepperoni,Anchovies,Cheese';
# insert Order (Id, Cust_Id, Order_date, Pizza_Id, Cost) */
INSERT Order 4001 1002 2014-12-21 3000 13.00;
INSERT Order 4002 1005 2015-01-07 3001 14.75;
INSERT Order 4003 1003 2015-02-26 3002 10.75;
INSERT Order 4004 1004 2015-03-24 3003 13.00;
INSERT Order 4005 1000 2015-09-13 3004 11.00;
INSERT Order 4006 1001 2016-10-01 3005 13.50;
INSERT Order 4007 1005 2017-01-29 3006 17.00;
# insert Topping (Id, Topping, Price) */
INSERT Topping 2000 'Cheese' 1.00;
INSERT Topping 2001 'Pepperoni' 2.00;
INSERT Topping 2002 'Sausage' 2.00;
INSERT Topping 2003 'Mushrooms' 1.50;
INSERT Topping 2004 'Pineapple' 3.25;
INSERT Topping 2005 'Anchovies' 0.75;