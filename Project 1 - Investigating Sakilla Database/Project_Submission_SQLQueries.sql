/*
Question 1
We want to understand more about the movies that families are watching.
The following categories are considered family movies: Animation, Children, Classics, Comedy, Family and Music.
Create a query that lists each movie, the film category it is classified in, and the number of times it has been rented out.

Query 1 */

WITH t1 AS
  (
  SELECT f.title AS Film_Title, c.name AS Category_Name, r.rental_id AS Rental_Id
  FROM film f
  JOIN film_category fc
  ON f.film_id = fc.film_id
  JOIN category c
  ON fc.category_id = c.category_id
  JOIN inventory i
  ON f.film_id = i.film_id
  JOIN rental r
  On i.inventory_id = r.inventory_id
  WHERE c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family','Music') )

SELECT Film_Title, Category_Name , COUNT(Rental_Id) AS Rental_Count
FROM t1
GROUP BY 1,2
ORDER BY 3 DESC


/* Question 2. Now we need to know how the length of rental duration of these family-friendly movies compares to the
duration that all movies are rented for. Can you provide a table with the movie titles and divide them into
4 levels (first_quarter, second_quarter, third_quarter, and final_quarter) based on the quartiles (25%, 50%, 75%)
of the rental duration for movies across all categories?
Make sure to also indicate the category that these family-friendly movies fall into
Query 2 */


WITH

t1 AS
  (
  SELECT f.title AS Film_Title, c.name AS Category_Name, f.rental_duration AS Rental_Duration
  FROM film f
  JOIN film_category fc
  ON f.film_id = fc.film_id
  JOIN category c
  ON fc.category_id = c.category_id
  WHERE c.name IN ('Animation', 'Children','Classics','Comedy','Family','Music'))

  SELECT Film_Title, Category_Name, Rental_Duration,
         NTILE(4) OVER (ORDER BY Rental_Duration)
  FROM t1

/* Question 3 :
We want to find out how the two stores compare in their count of rental orders during every month
for all the years we have data for. Write a query that returns the store ID for the store, the year and month
and the number of rental orders each store has fulfilled for that month. Your table should include a column
for each of the following: year, month, store ID and count of rental orders fulfilled during that month.
Query 3 */


  WITH
  t1 AS
        (SELECT DATE_PART('month', r.rental_date) AS Rental_month,
         DATE_PART('year', r.rental_date) AS Rental_Year,
         i.store_Id AS Store_Id,
         COUNT(i.film_id) OVER (PARTITION BY DATE_TRUNC('month' , rental_date) ORDER BY Store_Id) as Temp_Rental_Count
  FROM rental r
  JOIN inventory i
  ON r.inventory_id = i.inventory_id)

  SELECT Rental_month, Rental_Year, Store_Id, COUNT(Temp_Rental_Count) AS Rental_Count
  FROM t1
  GROUP BY 1,2,3
  ORDER BY 4 DESC

/* Question 4
We would like to know who were our top 10 paying customers, how many payments they made on a monthly basis during 2007,
and what was the amount of the monthly payments. Can you write a query to capture the customer name,
month and year of payment, and total payment amount for each month by these top 10 paying customers?
Query 4 */


SELECT DATE_TRUNC('month', p.payment_date) Pay_Month,
       c.first_name || ' ' || c.last_name AS Full_Name,
       COUNT(p.amount) AS pay_countpermon,
       SUM(p.amount) AS Pay_Amount
FROM customer c
JOIN payment p
ON p.customer_id = c.customer_id
WHERE c.first_name || ' ' || c.last_name IN

    (SELECT t1.full_name
    FROM
        (SELECT c.first_name || ' ' || c.last_name AS full_name,
                SUM(p.amount) as amount_total
        FROM customer c
        JOIN payment p
        ON p.customer_id = c.customer_id
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 10) t1)

AND (p.payment_date BETWEEN '2007-01-01' AND '2008-01-01')
GROUP BY 2, 1
ORDER BY 2, 1, 3
