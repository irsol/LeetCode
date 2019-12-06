# Given a Weather table, write a SQL query to find all dates
# Ids with higher temperature compared to its previous (yesterdays) dates.

# +---------+------------+------------------+
# | Id(INT) | Date(DATE) | Temperature(INT) |
# +---------+------------+------------------+
# |       1 | 2015-01-01 |               10 |
# |       2 | 2015-01-02 |               25 |
# |       3 | 2015-01-03 |               20 |
# |       4 | 2015-01-04 |               30 |
# +---------+------------+------------------+

# For example, return the following Ids for the above Weather table:
# +----+
# | Id |
# +----+
# |  2 |
# |  4 |
# +----+
#
#
# Approach: Using ```INNER JOIN``` and ```DATEDIFF()``` function
# Runtime: 615 ms, faster than 30.34% of MySQL online submissions for Rising Temperature.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rising Temperature.
#
# Write your MySQL query statement below

SELECT tb1.Id as 'Id'
FROM Weather as tb1
INNER JOIN Weather as tb2
ON datediff(tb1.RecordDate, tb2.RecordDate) = 1 and tb1.Temperature > tb2.Temperature;