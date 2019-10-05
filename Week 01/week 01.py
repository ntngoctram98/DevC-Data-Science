#%% connect database
import sqlite3
conn = sqlite3.connect('chinook.db')

import pandas as pd
data = pd.read_sql_query('SELECT * FROM albums;', conn)
data.head() 

#%% Find a list of all countries where customers live in
pd.read_sql_query('SELECT DISTINCT(COUNTRY) FROM CUSTOMERS',conn)

#%% Find the top 5 cheapest bill
pd.read_sql_query('SELECT * FROM INVOICE_ITEMS ORDER BY UNITPRICE * QUANTITY ASC LIMIT 5',conn)

#%% Find the next five invoice 
pd.read_sql_query('SELECT * FROM INVOICE_ITEMS LIMIT 5 OFFSET 5',conn)

#%% List all cities in Germany where the company has customers
pd.read_sql_query("""
  SELECT CITY 
  FROM CUSTOMERS 
  WHERE COUNTRY = 'Germany'
""", conn)

#%% Order all customers in the USA by their first name
pd.read_sql_query("""
  SELECT *
  FROM CUSTOMERS
  WHERE COUNTRY = 'USA'
  ORDER BY FIRSTNAME ASC
""", conn)

#%% List three most expensive bill in Boston, USA
pd.read_sql_query("""
  SELECT *
  FROM 
    INVOICE_ITEMS JOIN INVOICES
  WHERE BILLINGCITY = 'Boston'
  ORDER BY UNITPRICE * QUANTITY DESC
  LIMIT 3
""", conn)

#%%
# List the third and fourth most expensive bill in 2012
pd.read_sql_query("""
  SELECT *
  FROM INVOICE_ITEMS JOIN INVOICES
  WHERE strftime("%Y", INVOICEDATE) = "2012"
  ORDER BY UNITPRICE * QUANTITY DESC
  LIMIT 2
  OFFSET 2
""", conn)

#%%
# List first 10 tracks and its album's title order by track's name
pd.read_sql_query("""
  SELECT DISTINCT(TRACKS.NAME), ALBUMS.TITLE
  FROM TRACKS JOIN ALBUMS
  ON TRACKS.ALBUMID = ALBUMS.ALBUMID
  ORDER BY TRACKS.NAME ASC
  LIMIT 10
""", conn)

#%%
# List all employees and who they report to
pd.read_sql_query("""
  SELECT EMPLOYEES.FIRSTNAME, EMPLOYEES.TITLE, MANAGER.FIRSTNAME, MANAGER.TITLE
  FROM
    EMPLOYEES JOIN EMPLOYEES MANAGER
    ON EMPLOYEES.REPORTSTO = MANAGER.EMPLOYEEID
""", conn)

#%%
# List the first five customers order by their supporter's first name in descending order
pd.read_sql_query("""
  SELECT CUSTOMERS.FIRSTNAME, EMPLOYEES.FIRSTNAME
  FROM
    CUSTOMERS JOIN EMPLOYEES
    ON CUSTOMERS.SUPPORTREPID = EMPLOYEES.EMPLOYEEID
  ORDER BY EMPLOYEES.FIRSTNAME DESC
""", conn)

#%%
# Find all tracks that couldn't be sold (null invoice_items)
pd.read_sql_query("""
  SELECT TRACKS.NAME
  FROM 
    TRACKS LEFT OUTER JOIN INVOICE_ITEMS
    ON TRACKS.TRACKID = INVOICE_ITEMS.TRACKID
  WHERE INVOICE_ITEMS.INVOICELINEID IS NULL
""", conn)

#%%
# List all genres and the distinct media types in each genre
pd.read_sql_query("""
  SELECT DISTINCT(GENRES.NAME), MEDIA_TYPES.NAME
  FROM
    MEDIA_TYPES JOIN TRACKS
    ON MEDIA_TYPES.MEDIATYPEID = TRACKS.MEDIATYPEID
    JOIN GENRES
    ON TRACKS.GENREID = GENRES.GENREID
""", conn)

#%%
# Find the revenue of 2013
pd.read_sql_query("""
  SELECT SUM(INVOICE_ITEMS.UNITPRICE * INVOICE_ITEMS.QUANTITY)
  FROM
    INVOICE_ITEMS JOIN INVOICES
    ON INVOICE_ITEMS.INVOICEID = INVOICES.INVOICEID
  WHERE
    STRFTIME("%Y", INVOICES.INVOICEDATE) = "2013"
""", conn)

#%%
# Find the number of tracks belong to the genre Rock
pd.read_sql_query("""
  SELECT COUNT(*)
  FROM 
    GENRES JOIN TRACKS
    ON GENRES.GENREID = TRACKS.GENREID
""", conn)

#%%
# Find the number of customers each employee has supported
pd.read_sql_query("""
  SELECT EMPLOYEES.FIRSTNAME, COUNT(*) AS NUMBER_OF_CUSTOMERS
  FROM
    CUSTOMERS RIGHT JOIN EMPLOYEES
    ON CUSTOMERS.SUPPORTREPID = EMPLOYEES.EMPLOYEEID
""", conn)

#%%
# Find the customer who paid the most
pd.read_sql_query('''___ ''', conn)

#%%
# Find the richest artist
pd.read_sql_query('''___''', conn)

#%%
pd.read_sql_query("""
  SELECT * FROM EMPLOYEES
""", conn)

#%%
