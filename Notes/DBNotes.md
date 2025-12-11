# Databases
    1 Relational
    2 Non-Relational
    3 Cloud Databases

## 1 Relational
        Relational databases store data in tables with rows and columns

        -language

        * DML - Data Manipulation Language
        * DDL - Data Definition Language
        * DCL - Data Control Language
        * DQl - Data Query Language
        * TCL - Transaction Control Language

    Tables 
        - Rows | Records | tuples 
        - Columns | Attributes | Fields

    Constants
        - Primary Key = No Dublicates & Null Values
        - Foreign Key = primary key from another table
        - check = condition to be met
        - Not Null = No Null Values
        - Unique Key = No Dublicates values

    DQL :
        select - retrieve data from database
        projection - the process of retriving specific columns from a table.
        selection - the process of retriving specific rows from a table based on a condition.
        joins - combining data from multiple tables based on a common column.


# Operators
        - Arithmetic Operators
            - Addition           +
            - Subtraction        -
            - Multiplication     *
            - Division           / 
        - concadination 
                                ||
            eg: 
            SELECT 'First Name' || 'Last Name' AS Full_Name FROM     customers;
        - Comparison Operators
            - Equal to          =   
            - Not Equal to      != or <>
        - relational Operators
            - Greater than                  >
            - Less than                     <
            - Greater than or equal to      >=
            - Less than or equal to         <=
        - Logical Operators
            - AND   
            - OR
            - NOT 
    

# Special Opreators:
    1 IN               - It is multivalue operator which can take multiple values            - eg: WHERE country IN ('USA', 'Canada', 'UK');
    2 NOT IN           - It is multivalue operator which can take multiple values            - eg: WHERE country NOT IN ('USA', 'Canada', 'UK');
    3 IS               - It is used to compare a value with NULL                             - eg: WHERE column_name IS NULL;
    4 IS NOT           - It is used to compare a value with NOT NULL                         - eg: WHERE column_name IS NOT NULL;   
    5 BETWEEN          - It is used to filter the result set within a certain range          - eg: WHERE column_name BETWEEN value1 AND value2;
    6 NOT BETWEEN      - It is used to filter the result set outside a certain range         - eg: WHERE column_name NOT BETWEEN value1 AND value2;
    7 LIKE             - It is used to search for a specified pattern | %, _                 - eg: WHERE column_name LIKE | A%, _b%; 
    8 NOT LIKE         - It is used to search for a specified pattern not matching | %, _    - eg: WHERE column_name NOT LIKE | A%, _b%;


# Joins
    - Inner Join
        select Entity1.col_name, Entity2.col_name
        from Entity1, Inner Join Entity2
        on Entity1.id = Entity2.id;
    - Left Join
    - Right Join
    - Full other Join
