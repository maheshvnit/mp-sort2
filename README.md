mp-sort2
=======

Python - Read CSV files data and sort by columns

Consider Share prices for a N number of companies given for each month since year 1990 in a CSV file.  
Format of the file is as below with first line as header.
 
Year,Month,Company A, Company B,Company C, .............Company N

1990, Jan, 10, 15, 20, , ..........,50

1990, Feb, 10, 15, 20, , ..........,50

.

.

.

.

2013, Sep, 50, 10, 15............500

 

The solution mp-sort2 - List for each Company year and month in which the share price was highest.

Class : MP_Sort from mahesh_prasad_sort.py - sort the share prices of csv file

Class : Test_MP_Sort from test_mahesh_prasad_sort.py - test class to test MP_Sort class


Test Run Logs:


E:\Python27\script\mp-sort2>python mahesh_prasad_sort.py

E:\Python27\script\mp-sort2>python test_mahesh_prasad_sort.py
test_readCSV (__main__.Test_MP_Sort) ... ok
test_readHD (__main__.Test_MP_Sort) ... ok
test_sortData (__main__.Test_MP_Sort) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.004s

OK

E:\Python27\script\mp-sort2>

