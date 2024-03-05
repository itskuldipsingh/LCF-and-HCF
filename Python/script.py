def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // hcf(a, b)

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
