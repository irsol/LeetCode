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
### Explanation
# Used `INNER JOIN` to compare `table` Weather with itself. 

# Write your MySQL query statement below

SELECT table1.Id as 'Id'
FROM Weather as table1
INNER JOIN Weather as table2