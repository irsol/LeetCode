-- 176. Second Highest Salary
/*
Write a SQL query to get the second highest salary from the Employee table.
Alias Salary as SecondHighestSalary.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the second highest salary is 200.
If there is no second highest salary, then the query should return null.

Write your MySQL query statement below
*/

-- Runtime: 514 ms, faster than 12.85% of MySQL online submissions for Second Highest Salary.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.

select max(Salary) as "SecondHighestSalary"
from Employee
where Salary < (
    select max(Salary)
    from Employee
    );
