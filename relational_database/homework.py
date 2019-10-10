from typing import List


def task_1_add_new_record_to_db(con) -> None:
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        con: psycopg connection

    Returns: 92 records

    """

    cursor = con.cursor ()
    cursor.execute("""insert into Customers(CustomerName,ContactName,Address,City,PostalCode,Country) 
    values ('Thomas','David','Some Address','London','774','Singapore')""")
    con.commit()


def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """

    cur.execute("delete from Customers where CustomerName = 'Thomas' and ContactName = 'David'")
    cur.execute("select * from Customers")
    return cur.fetchall()


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute("select * from Customers where Country = 'Germany'")
    return cur.fetchall()


def task_4_update_customer(con):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        cur: psycopg cursor

    Returns: 91 records with updated customer

    """
    cur = con.cursor()
    cur.execute("update Customers set CustomerName = 'Johnny Depp' where CustomerName = (select CustomerName from Customers limit 1)")
    con.commit()
    results = cur.execute("select * from Customers")
    return results


def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    cur = con.cursor()
    cur.execute("delete from Customers where CustomerID=(select max(CustomerID) from Customers)")
    con.commit()
    result_del = cur.execute("select * from Customers")
    return result_del

def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    cur.execute("select Country from Suppliers")
    return cur.fetchall()


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    cur.execute("select Country from Suppliers order by Country desc")
    return cur.fetchall()


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """
    cur.execute("select Count(City), City from Customers group by City order by Count(City) desc")
    return cur.fetchall()

def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    cur.execute("select Count(City), City from Customers group by City having Count(City) > 10")
    return cur.fetchall()


def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    cur.execute("select * from Customers limit 10")
    return cur.fetchall()


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute("select * from Customers where CustomerId > 11")
    return cur.fetchall()



def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    cur.execute("""select SupplierID, SupplierName, ContactName, City, Country from Suppliers 
    where Country = 'USA' OR Country = 'UK' OR Country = 'Japan'""")
    return cur.fetchall()


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """

    cur.execute("""select ProductName from Products inner join Suppliers 
    on Products.SupplierID=Suppliers.SupplierID where Country = 'Sweden'""")
    return cur.fetchall()


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    cur.execute("""select ProductID, ProductName, Unit, Price, Country, City, SupplierName 
    from Products inner join Suppliers on Products.SupplierID=Suppliers.SupplierID""")
    return cur.fetchall()


def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    cur.execute("""select Customers.CustomerName, Customers.ContactName, Customers.Country, Orders.OrderID 
    from Customers left join Orders on Customers.CustomerID = Orders.CustomerID""")
    return cur.fetchall()

def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    cur.execute("""select Customers.CustomerName, Customers.Address, Customers.Country as CustomerCountry, 
    Suppliers.Country as SupplierCountry, Suppliers.SupplierName 
    from Customers full join Suppliers on Customers.Country = Suppliers.Country order by Customers.Country, Suppliers.Country""")
    return cur.fetchall()