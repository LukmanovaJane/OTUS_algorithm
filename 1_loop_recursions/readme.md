## Topic:  Loops and Recursion


## Task: 
1. Make a system to check your solution. Initial task in `<file>.in` and answer in `<file>.out`
2. Solve a task with "lucky" numbers
3. Solve a task with "magic words"

## Results

#### Validate report from `character_counter.py`
```
Testing function name: count_character_with_loop
------------------------------------------------------------------------------------------------
Task     | Result   | Answer   | Status   | File_Task       | File_Answer     | Duration        |
------------------------------------------------------------------------------------------------
12345678 | 8        | 8        | True     | test.0.in       | test.0.out      | 0:00:00.000004  |
------------------------------------------------------------------------------------------------
123456.. | 64       | 64       | True     | test.1.in       | test.1.out      | 0:00:00.000004  |
------------------------------------------------------------------------------------------------
         | 0        | 0        | True     | test.2.in       | test.2.out      | 0:00:00.000001  |
------------------------------------------------------------------------------------------------
$        | 1        | 1        | True     | test.3.in       | test.3.out      | 0:00:00.000002  |
------------------------------------------------------------------------------------------------
abcdef.. | 25       | 26       | False    | test.4.in       | test.4.out      | 0:00:00.000003  |
================================================================================================
Result: FAIL	 total time: 0:00:00.000752

Testing function name: count_character_build_in
------------------------------------------------------------------------------------------------
Task     | Result   | Answer   | Status   | File_Task       | File_Answer     | Duration        |
------------------------------------------------------------------------------------------------
12345678 | 8        | 8        | True     | test.0.in       | test.0.out      | 0:00:00.000002  |
------------------------------------------------------------------------------------------------
123456.. | 64       | 64       | True     | test.1.in       | test.1.out      | 0:00:00.000002  |
------------------------------------------------------------------------------------------------
         | 0        | 0        | True     | test.2.in       | test.2.out      | 0:00:00.000002  |
------------------------------------------------------------------------------------------------
$        | 1        | 1        | True     | test.3.in       | test.3.out      | 0:00:00.000002  |
------------------------------------------------------------------------------------------------
abcdef.. | 25       | 26       | False    | test.4.in       | test.4.out      | 0:00:00.000002  |
================================================================================================
Result: FAIL	 total time: 0:00:00.000465

```
#### Validate report from `lucky_numbers.py`
```
Testing function name: count_lucky_numbers_with_formula
------------------------------------------------------------------------------------------------
Task     | Result   | Answer   | Status   | File_Task       | File_Answer     | Duration        |
------------------------------------------------------------------------------------------------
1        | 10       | 10       | True     | test.0.in       | test.0.out      | 0:00:00.000019  |
------------------------------------------------------------------------------------------------
2        | 670      | 670      | True     | test.1.in       | test.1.out      | 0:00:00.000050  |
------------------------------------------------------------------------------------------------
3        | 55252    | 55252    | True     | test.2.in       | test.2.out      | 0:00:00.000635  |
------------------------------------------------------------------------------------------------
4        | 4816030  | 4816030  | True     | test.3.in       | test.3.out      | 0:00:00.009325  |
------------------------------------------------------------------------------------------------
5        | 432457.. | 432457.. | True     | test.4.in       | test.4.out      | 0:00:00.108096  |
------------------------------------------------------------------------------------------------
6        | 395811.. | 395811.. | True     | test.5.in       | test.5.out      | 0:00:01.082469  |
------------------------------------------------------------------------------------------------
7        | 367133.. | 367133.. | True     | test.6.in       | test.6.out      | 0:00:11.826146  |
================================================================================================
Result: SUCCESS	 total time: 0:00:13.034519
```