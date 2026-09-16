# top

## Specific behavior in Python

### mathematical modulo

Python uses mathematical modulo (also called floored division).
The formula Python follows is:<br>
`a % b = a - floor(a / b) * b`

1. Case: `-2 % 5`

`-2 / 5 = -0.4`<br>
`floor(-0.4) = -1` (floor rounds down)<br>
`-2 - (-1)*5 = -2 + 5 = 3`<br>

So: `-2 = -1 * 5 + 3` → remainder is 3 (positive)↳ 2. Case: `-2 % -5`

`-2 / -5 = 0.4`<br>
`floor(0.4) = 0`<br>
`-2 - 0*(-5) = -2`<br>

So: `-2 = 0 * (-5) + (-2)` → remainder is -2↳<br>
Key Rule in Python:<br>
The sign of the result matches the sign of the divisor (the right number).↳<br>

If divisor is positive → result is positive (or zero)<br>
If divisor is negative → result is negative (or zero)<br>

Comparison with Other Languages<br>

| Expression | Python | C++ / Java / JavaScript / Go |
| ---------- | ------ | ---------------------------- |
| `-2 % 5`   | 3      | -2                           |
| `-2 % -5`  | -2     | -2                           |

**C++/Java/JS:** Remainder has the sign of the dividend (left number). They use truncated division instead of floored.<br>

**Summary**<br>
Python: `-2 % 5 = 3` because it wants the remainder to be non-negative when the divisor is positive.<br>
This is mathematically elegant and useful in many algorithms (e.g., circular indexing, positive remainders).<br>
