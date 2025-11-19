# Chapter 6: Complements

_Originally created 5 February, 2021 by Maxwell Hauser — Updated 6 October, 2025_

_Builds upon material from Chapter 5: Conversions._

---

## Complements

In a binary number:
- The first bit from the left is called the **Most Significant Bit (MSB)**.
- The first bit from the right is called the **Least Significant Bit (LSB)**.

```
MSB → 1 0 0 1 0 ← LSB
```

In a decimal number:
- The first digit from the left is called the **Most Significant Digit (MSD)**.
- The first digit from the right is called the **Least Significant Digit (LSD)**.

```
MSD → 3 5 6 ← LSD
```
In a number system with base $r$, the $r$'s complement of a number $N$ with $n$ digits is defined as:

$r^n - N$

For example, in binary (base 2):
- The 2's complement of 101 (3 bits) is:

    $2^3 - 101 = 8 - 5 = 3 = 011$
    
---

The $(r-1)$'s complement of a number $N$ with $n$ digits is defined as:

$(r - 1) * r^{n-1} + (r - 1) * r^{n-2} + ... + (r - 1) * r^{0} - N$

For example, in binary (base 2):
- The 1's complement of 101 (3 bits) is:

    $(2 - 1) * 2^{2} + (2 - 1) * 2^{1} + (2 - 1) * 2^{0} - 101 = 7 - 5 = 2 = 010$

---

Another way to think about it is that the $(r-1)$'s complement of a number is found by subtracting each digit from $r-1$.

---

## Complements in Binary

This course focuses primarily on the binary number system, so we will focus on the **1's complement** and **2's complement**.

#### One's Complement
The 1's complement of a binary number is found by inverting all bits (changing 0s to 1s and 1s to 0s).

Example 1.8: The 1's complement of 101101 is 010010.

Example 1.9: The 1's complement of 000000 is 111111.

---

#### Two's Complement
The 2's complement of a binary number is found by adding 1 to the 1's complement of the number.

Example 1.10: The 2's complement of 101101 is 010011.

Example 1.11: The 2's complement of 000000 is 000001.

---

#### Subtraction of Unsigned Numbers using Two’s Complement

The following procedure may be used to subtract:

$B = b_5 b_4 b_3 b_2 b_1 b_0$ from $A= a_5 a_4 a_3 a_2 a_1 a_0$

1. Find the 2's complement of $B$.
2. Add the 2's complement of $B$ to $A$.
3. If there is a carry out, discard the carry and the result is positive.
4. If there is no carry out, take the 2's complement of the result and the result is negative.

Example 1.12:

Subtract $B=101010$ from $A=110101$

1. Compute two’s complement of $B$.

    $= 010110$

2. Add 2’s complement of $B$ to $A$.

    ```
        010110
    +   110101
    -----------------
       1001011
    ```

3. Since we have a 7th bit carry, we discard the carry and the result is +001011.

---

Example 1.13:

Subtract $B = 110101$ from $A = 101010$

1. Compute two’s complement of $B$.

    $= 001011$

2. Add 2’s complement of $B$ to $A$.

    ```
        001011
    +   101010
    -----------------
        110101
    ```

3. As we can see, these two numbers sum to another six bit number. There is no carry, so we just take the two’s complement of the result and the result is negative:

    $= -001011$

### Summary
| Operation | Method |
|-----------|--------|
| 1's Complement | Invert all bits |
| 2's Complement | 1's Complement + 1 |
| Subtraction | Add 2's Complement of B to A |
| Positive Result | Discard carry |
| Negative Result | Take 2's Complement |
