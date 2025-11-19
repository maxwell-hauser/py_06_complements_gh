#!/usr/bin/env python3
"""
Chapter 6: Complements
Demonstrates one's complement and two's complement operations
"""

def ones_complement(binary_str):
    """Calculate one's complement by flipping all bits"""
    return ''.join('1' if bit == '0' else '0' for bit in binary_str)

def twos_complement(binary_str):
    """Calculate two's complement (one's complement + 1)"""
    ones = ones_complement(binary_str)
    
    # Add 1 to one's complement
    carry = 1
    result = list(ones)
    
    for i in range(len(result) - 1, -1, -1):
        if carry == 0:
            break
        
        if result[i] == '0':
            result[i] = '1'
            carry = 0
        else:
            result[i] = '0'
            # carry continues
    
    return ''.join(result)

def decimal_to_twos_complement(decimal, bits=8):
    """Convert decimal (including negative) to two's complement"""
    if decimal >= 0:
        binary = format(decimal, f'0{bits}b')
    else:
        # Get positive binary, then two's complement
        positive = abs(decimal)
        binary = format(positive, f'0{bits}b')
        binary = twos_complement(binary)
    
    return binary

def twos_complement_to_decimal(binary_str):
    """Convert two's complement binary to decimal"""
    # Check if negative (MSB = 1)
    if binary_str[0] == '1':
        # Find two's complement to get magnitude
        magnitude_binary = twos_complement(binary_str)
        magnitude = int(magnitude_binary, 2)
        return -magnitude
    else:
        return int(binary_str, 2)

def main():
    print("=" * 60)
    print("CHAPTER 6: Complements")
    print("=" * 60)
    
    # Example 1: One's Complement
    print("\n--- Example 1: One's Complement ---")
    binary = "10110011"
    ones = ones_complement(binary)
    print(f"Original:        {binary}")
    print(f"One's complement: {ones}")
    print("(Flip all bits: 0→1, 1→0)")
    
    # Example 2: Two's Complement
    print("\n--- Example 2: Two's Complement ---")
    binary = "01011100"
    ones = ones_complement(binary)
    twos = twos_complement(binary)
    print(f"Original:         {binary}")
    print(f"One's complement: {ones}")
    print(f"Add 1:            {twos}")
    print("(Two's complement = One's complement + 1)")
    
    # Example 3: Representing Negative Numbers
    print("\n--- Example 3: Negative Number Representation ---")
    number = -23
    binary = decimal_to_twos_complement(number, 8)
    print(f"Decimal: {number}")
    print(f"Steps:")
    print(f"  1. Get positive binary: {format(abs(number), '08b')} (23)")
    print(f"  2. One's complement:    {ones_complement(format(abs(number), '08b'))}")
    print(f"  3. Add 1 (Two's comp):  {binary}")
    
    # Verify
    back_to_decimal = twos_complement_to_decimal(binary)
    print(f"Verification: {binary} → {back_to_decimal}")
    
    # Example 4: MSB as Sign Bit
    print("\n--- Example 4: MSB (Most Significant Bit) ---")
    positive = "01100100"  # Positive (MSB=0)
    negative = "11100100"  # Negative (MSB=1)
    
    print(f"Positive number: {positive}")
    print(f"  MSB = {positive[0]} → Positive")
    print(f"  Value: {int(positive, 2)}")
    
    print(f"\nNegative number: {negative}")
    print(f"  MSB = {negative[0]} → Negative")
    print(f"  Value: {twos_complement_to_decimal(negative)}")
    
    # Example 5: Range of Two's Complement
    print("\n--- Example 5: Range for n-bit Two's Complement ---")
    for bits in [4, 8, 16]:
        min_val = -(2 ** (bits - 1))
        max_val = 2 ** (bits - 1) - 1
        print(f"{bits}-bit: {min_val} to {max_val}")
    
    # Example 6: Common Two's Complement Values
    print("\n--- Example 6: Common 8-bit Values ---")
    test_values = [0, 1, -1, 127, -128, 5, -5]
    print("Decimal | 8-bit Two's Complement")
    print("--------|------------------------")
    for val in test_values:
        binary = decimal_to_twos_complement(val, 8)
        print(f" {val:4d}   | {binary}")
    
    print("\n" + "=" * 60)
    print("Key Concepts:")
    print("- One's complement: Flip all bits")
    print("- Two's complement: One's complement + 1")
    print("- MSB = 0 → positive, MSB = 1 → negative")
    print("- Two's complement is standard for negative numbers")
    print("- Range: -(2^(n-1)) to 2^(n-1) - 1")
    print("=" * 60)

if __name__ == "__main__":
    main()
