# HCF and LCM Calculator

This Python program calculates the Highest Common Factor (HCF) and Lowest Common Multiple (LCM) of a list of numbers.

## [Python Code](https://github.com/itskuldipsingh/Math/blob/main/LCM%20and%20HCF/Python/script.py)

```python
def main():
    arr = []
    print("Enter numbers separated by spaces:")
    input_numbers = input().split()
    
    for num in input_numbers:
        arr.append(int(num))

    if len(arr) < 2:
        print("At least two numbers are required for HCF and LCM calculation.")
        return

    find_hcf = arr[0]
    find_lcm = arr[0]

    for i in range(1, len(arr)):
        find_hcf = hcf(find_hcf, arr[i])
        find_lcm = lcm(find_lcm, arr[i])

    print(f"HCF of the numbers is: {find_hcf}")
    print(f"LCM of the numbers is: {find_lcm}")

if __name__ == "__main__":
    main()
```
Run above code in python ide and it will ask for enter numbers seprated by space(blank)
```
Enter numbers separated by spaces:
```
Now enter numbers which you want to find lcm and hcf and press enter. For example: LCM and HCF of 12, 18 and 24 
```
12 18 24
HCF of the numbers is: 6
LCM of the numbers is: 72
```
