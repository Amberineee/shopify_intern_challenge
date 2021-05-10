# shopify_intern_challenge

Question 1: Given some sample data, write a program to answer the following: 

On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis. 

a. Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. 

AOV is calculated by total revenue divided by the total number of orders. There are some outliers such as order 16 , order 61 and order 161 etc. with a larger value of order amount, that’s why AOV is a lot higher than expected. Instead of average order value, we can use median order value to eliminate the outliers. 

b. What metric would you report for this dataset?

First I will report the median order value for all the orders. More specifically we could look at the median order value per payment method. Also the daily order amount and 7-day rolling average of order amount per day to do more detailed and goal oriented analysis. 
c. What is its value?

The median order value of this dataset is $284.

Question 2: For this question you’ll need to use SQL. Follow this link to access the data set required for the challenge. Please use queries to answer the following questions. Paste your queries along with your final numerical answers below.

a. How many orders were shipped by Speedy Express in total?

SELECT b.ShipperName, count(distinct OrderID) AS num_order FROM [Orders] a 
LEFT JOIN [Shippers] b ON a.ShipperID = b.ShipperID
WHERE b.ShipperName = "Speedy Express";

ANSWER: 54

b. What is the last name of the employee with the most orders?

SELECT LastName, max(num_ord) AS ord from (
SELECT b.LastName, count(distinct OrderID) AS num_ord FROM [Orders] a LEFT JOIN [Employees] b USING (EmployeeID)
GROUP BY 1);

ANSWER: Peacock

c. What product was ordered the most by customers in Germany?

SELECT ProductName, max(quantity) AS quantity FROM (SELECT ProductName, sum(Quantity) AS quantity FROM [Orders] a Left JOIN [OrderDetails] b ON a.OrderID = b.OrderID LEFT JOIN [Products] c ON b.ProductID = c.ProductID LEFT JOIN 
[Customers] d ON a.CustomerID = d.CustomerID
WHERE Country = "Germany"
GROUP BY 1);

ANSWER: Boston Crab Meat
