"""26. WAPTP all armstrong numbers between 1 and 10000
If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number.
For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 )"""

start = 1
end = 1000

for num in range(start, end + 1):
    power = len(str(num))
    sumNum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sumNum = sumNum + (digit**power)
        temp //= 10

    if num == sumNum:
        print(num)
