# Chapter 6: Complements

## Overview

This chapter covers complement systems used in binary arithmetic, specifically one's complement and two's complement. These are fundamental techniques for representing negative numbers and performing subtraction in digital computers.

## Key Concepts

### Why Complements?

**Problem:** Digital circuits are designed to add, not subtract. How do we perform subtraction?  
**Solution:** Convert subtraction into addition using complements!

```
A - B = A + (-B)
```

Complements allow us to:
- Represent negative numbers
- Perform subtraction using addition circuits
- Simplify hardware design
- Eliminate the need for separate subtraction logic

### One's Complement (1's Complement)

#### Definition
The one's complement of a binary number is obtained by flipping all bits (0→1, 1→0).

#### How to Find One's Complement
**Method:** Invert every bit
```
Original:        10110100
One's Complement: 01001011
```

#### Properties
- **Two representations of zero:** +0 (00000000) and -0 (11111111)
- **Range (n bits):** -(2^(n-1) - 1) to +(2^(n-1) - 1)
- **Sign bit:** MSB = 0 (positive), MSB = 1 (negative)
- **Easy to calculate:** Simple bit inversion
- **Disadvantage:** Two zeros complicate arithmetic

#### Example: 8-bit One's Complement
```
+5:  00000101
-5:  11111010  (flip all bits)

+0:  00000000
-0:  11111111  (problem: two zeros!)
```

### Two's Complement (2's Complement)

#### Definition
The two's complement is obtained by:
1. Finding the one's complement (flip all bits)
2. Adding 1 to the result

**Formula:** Two's Complement = One's Complement + 1

#### How to Find Two's Complement

**Method 1: Flip and Add 1**
```
Original:          10110100
One's Complement:  01001011
Add 1:           +        1
Two's Complement:  01001100
```

**Method 2: Copy from Right Until First 1, Then Flip**
```
Original:         10110100
                        ↑ (first 1 from right)
Copy up to first 1: ....0100
Flip remaining:     01001100
```

#### Properties
- **Single zero:** Only one representation: 00000000
- **Range (n bits):** -2^(n-1) to +(2^(n-1) - 1)
  - 8 bits: -128 to +127
  - 16 bits: -32,768 to +32,767
  - 32 bits: -2,147,483,648 to +2,147,483,647
- **Sign bit:** MSB = 0 (positive), MSB = 1 (negative)
- **Asymmetric range:** One more negative number than positive
- **Industry standard:** Used in virtually all modern computers

#### Example: 8-bit Two's Complement
```
+5:  00000101
-5:  11111011  (flip bits: 11111010, then add 1)

+127: 01111111  (largest positive)
-128: 10000000  (largest negative, no positive equivalent!)
   0: 00000000  (only one zero)
```

### Sign Bit (Most Significant Bit)

In both complement systems:
- **MSB = 0:** Number is positive or zero
- **MSB = 1:** Number is negative

```
8-bit examples:
0xxxxxxx = positive (0 to 127)
1xxxxxxx = negative (-128 to -1 in two's complement)
```

## Comparison: One's vs Two's Complement

| Feature | One's Complement | Two's Complement |
|---------|------------------|------------------|
| **Calculation** | Flip all bits | Flip all bits + 1 |
| **Zero Representation** | Two (±0) | One (0) |
| **8-bit Range** | -127 to +127 | -128 to +127 |
| **Symmetry** | Symmetric | Asymmetric (one extra negative) |
| **Addition** | Needs end-around carry | Direct addition |
| **Hardware** | Slightly more complex | Simpler |
| **Usage** | Rare (some legacy systems) | Universal standard |
| **Subtraction** | A - B = A + 1's(B) + carry | A - B = A + 2's(B) |

## Converting Between Representations

### Decimal to Two's Complement

**For Positive Numbers:** Simple binary conversion
```
+42₁₀ → 00101010₂ (8-bit)
```

**For Negative Numbers:**
1. Convert absolute value to binary
2. Find two's complement

```
-42₁₀:
1. |−42| = 42 → 00101010
2. Flip bits:    11010101
3. Add 1:      + 00000001
4. Result:       11010110
```

### Two's Complement to Decimal

**If MSB = 0 (positive):** Direct binary to decimal conversion

**If MSB = 1 (negative):**
1. Find two's complement (to get magnitude)
2. Convert to decimal
3. Apply negative sign

```
11010110₂:
1. MSB = 1, so it's negative
2. Two's complement: 00101010
3. 00101010₂ = 42₁₀
4. Result: -42₁₀
```

## Arithmetic with Two's Complement

### Addition
Just add normally and discard any carry beyond the word size!

```
  5:  00000101
+ 3:  00000011
  ─────────────
  8:  00001000 ✓

  5:  00000101
+ -3: 11111101
  ─────────────
  2: 100000010 → 00000010 (discard carry) ✓
```

### Subtraction
Convert to addition: A - B = A + two's complement of B

```
  5 - 3 = 5 + (-3):
  5:   00000101
+ -3:  11111101
  ──────────────
  2:  100000010 → 00000010 ✓
```

### Overflow Detection

**Overflow occurs when:**
- Positive + Positive = Negative result (impossible!)
- Negative + Negative = Positive result (impossible!)

**Overflow does NOT occur when:**
- Positive + Negative (result is always valid)
- Signs differ

```
Overflow example (8-bit):
  100:  01100100
+ 50:   00110010
  ──────────────
  150:  10010110  ← OVERFLOW! (negative result for positive addition)
```

## Learning Objectives

By the end of this chapter, you should be able to:
- Calculate one's complement of binary numbers
- Calculate two's complement of binary numbers
- Convert decimal to two's complement representation
- Convert two's complement to decimal
- Understand the range of values in complement systems
- Recognize the sign bit (MSB) and its significance
- Explain why two's complement is the industry standard
- Detect overflow in complement arithmetic

## Python Example

Run the interactive example:

```bash
python ch06_complements.py
```

### What the Example Demonstrates

1. **One's Complement:** Flipping all bits
2. **Two's Complement:** Flip + add 1 method
3. **Negative Numbers:** Representing negatives in binary
4. **Range Calculations:** Valid ranges for different bit widths
5. **Decimal Conversions:** To and from two's complement
6. **Comparison:** One's vs two's complement side-by-side
7. **Sign Bit:** Understanding MSB significance
8. **Practical Applications:** Real-world usage

### Sample Output

```
============================================================
CHAPTER 6: Complements (One's and Two's Complement)
============================================================

--- Example 1: One's Complement ---
Original:         01011010 (90 in decimal)
One's Complement: 10100101

--- Example 2: Two's Complement ---
Original:          01011010 (90 in decimal)
One's Complement:  10100101
Add 1:           +        1
Two's Complement:  10100110 (-90 in two's complement)
...
```

## Real-World Applications

### Computer Processors
- **ALU (Arithmetic Logic Unit):** Uses two's complement for all signed integer operations
- **CPU Registers:** Store signed integers in two's complement
- **Integer Arithmetic:** All addition, subtraction, multiplication

### Programming Languages
- **C/C++:** `int`, `short`, `long` types use two's complement
- **Java:** All integer types are two's complement
- **Python:** Unlimited precision, but underlying operations use two's complement
- **Assembly Language:** Direct manipulation of two's complement values

### Data Types
- **int8_t:** -128 to 127 (8-bit two's complement)
- **int16_t:** -32,768 to 32,767 (16-bit)
- **int32_t:** -2,147,483,648 to 2,147,483,647 (32-bit)
- **int64_t:** -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 (64-bit)

### Digital Signal Processing
- **Audio Processing:** Signed samples in two's complement
- **Image Processing:** Pixel manipulation with signed values
- **Control Systems:** Signed sensor readings and control signals

## Common Questions

**Q: Why is two's complement better than one's complement?**  
A: Two's complement has only one zero, simpler arithmetic (no end-around carry), and easier hardware implementation.

**Q: Why is the range asymmetric (-128 to +127 for 8 bits)?**  
A: Because 10000000 represents -128 in two's complement. There's no positive equivalent, giving us one extra negative number.

**Q: How do I know if a number is positive or negative?**  
A: Check the Most Significant Bit (MSB). If MSB=0, it's positive; if MSB=1, it's negative.

**Q: What happens if I two's complement twice?**  
A: You get back the original number! It's a reversible operation.

**Q: Can I use two's complement with hexadecimal?**  
A: Yes! Convert hex to binary, apply two's complement, convert back to hex.

## Key Formulas

```
One's Complement:  Flip all bits
Two's Complement:  One's Complement + 1

Range (n bits):
  Unsigned:        0 to 2^n - 1
  Two's Complement: -2^(n-1) to 2^(n-1) - 1
  
Sign Bit:
  MSB = 0 → Positive
  MSB = 1 → Negative

Subtraction:
  A - B = A + two's_complement(B)
```

## Key Takeaways

- Complements convert subtraction into addition
- 💯 Two's complement is the universal standard in modern computing
- Two's complement = one's complement + 1
- Range is -2^(n-1) to 2^(n-1) - 1 for n-bit two's complement
- Range is asymmetric (one more negative number)
- 🔝 MSB (sign bit) indicates positive (0) or negative (1)
- ➕ Addition works normally; just discard carries beyond word size
- Overflow occurs when result sign contradicts operand signs

## Practice Exercises

1. Find the one's complement of 01101100
2. Find the two's complement of 01101100
3. What is -25 in 8-bit two's complement?
4. Convert 11010110 (8-bit two's complement) to decimal
5. What is the range of 12-bit two's complement integers?
6. Calculate 45 - 30 using two's complement (8-bit)
7. Verify: Two's complement of (two's complement of 01010101) = 01010101
8. Why can't we represent +128 in 8-bit two's complement?
9. Detect if overflow occurred: 01111111 + 00000010 (8-bit two's complement)
10. Convert -100₁₀ to 8-bit two's complement

## Further Study

- Learn about signed magnitude representation (Chapter 7)
- Study binary arithmetic operations (Chapter 8)
- Explore overflow detection and handling
- Investigate saturating arithmetic
- Learn about sign extension when increasing bit width

---

**Course Navigation:**  
← Previous: [Chapter 5 - Number System Conversions](../ch5_conversions/) | Next: [Chapter 7 - Signed Numbers](../ch7_signed_magnitude/) →

---

## Authorship
Authored by Maxwell Hauser on November 19, 2025

## License
MIT License
