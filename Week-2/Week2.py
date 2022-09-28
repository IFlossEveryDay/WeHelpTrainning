# Request-1
# =========================================

print("Request-1")


def calculate(min, max, step):
    # 請用你的程式補完這個函式的區塊
    for cal in [min, max, step]:
        if ((min + step) < max) and (min > 0) and (step != max):
            print(min + max + (max - step))
            break
        elif ((min + step) < max) and (min < 0):
            print(min + (min+step))
            break
        else:
            print(min)
            break


calculate(1, 3, 1)  # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2)  # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2)  # 你的程式要能夠計算 -1+1，最後印出 0

# Request-2
# =========================================

print("Request-2")


def avg(data):
    # 請用你的程式補完這個函式的區塊
    i = data["employees"]
    sum = 0
    personal = 0
    count = 0
    for x in i:
        # print(x["manager"])
        if x["manager"] == False:
            personal = (x["salary"])
            sum = sum + personal
            count = count + 1
    print(sum / count)


avg({
    "employees": [
        {
            "name": "John",
            "salary": 30000,
            "manager": False
        },
        {
            "name": "Bob",
            "salary": 60000,
            "manager": True
        },
        {
            "name": "Jenny",
            "salary": 50000,
            "manager": False
        },
        {
            "name": "Tony",
            "salary": 40000,
            "manager": False
        }
    ]
})  # 呼叫 avg 函式

# Request-3
# =========================================

print("Request-3")


def func(a):
    # 請用你的程式補完這個函式的區塊
    def f(b, c):
        print(a + (b * c))
    return f


func(2)(3, 4)  # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5)  # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9)  # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果


# Request-4
# =========================================
print("Request-4")


def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    if len(nums) < 2:
        print("無法相乘")
    result = -1000000000

    for x in nums:
        for y in nums:
            if x != y:
                multiply = x * y
                if multiply >= result:
                    result = multiply
    print(result)


maxProduct([5, 20, 2, 6])  # 得到 120
maxProduct([10, -20, 0, 3])  # 得到 30
maxProduct([10, -20, 0, -3])  # 得到 60
maxProduct([-1, 2])  # 得到 -2
maxProduct([-1, 0, 2])  # 得到 0
maxProduct([5, -1, -2, 0])  # 得到 2
maxProduct([-5, -2])  # 得到 10


# Request-5
# =========================================
print("Request-5")


def twoSum(nums, target):
    # your code here
    for x in range(len(nums)):
        indi = target - nums[x]
        for y in range(x + 1, len(nums)):
            if indi == nums[y]:
                return [x, y]


result = twoSum([2, 11, 7, 15], 9)
print(result)  # show [0, 2] because nums[0]+nums[2] is 9

# Optional
# =========================================
print("Optional")


def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊
    zeroCount = 0
    zeroSum = 0
    for i in nums:
        if i == 0:
            zeroCount += 1
        else:
            zeroCount = 0
        if zeroCount > zeroSum:
            zeroSum = zeroCount
    print(zeroSum)


maxZeros([0, 1, 0, 0])  # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])  # 得到 4
maxZeros([1, 1, 1, 1, 1])  # 得到 0
maxZeros([0, 0, 0, 1, 1])  # 得到 3
