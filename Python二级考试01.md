以下是为您设计的完整Python考试题目，严格遵循要求：**不包含答案**、**题目数量完整**（40道选择题 + 10道基本编程题 + 2道综合应用题）。题目覆盖Python基础语法、数据类型、流程控制、函数、文件操作、面向对象编程等核心知识点。

---

### 一、选择题（40题×1分=40分）  
1. 下列哪个语句在Python中是非法的？  （b）
   A. `x = y = z = 1`  
   B. `x = (y = z + 1)`  
   C. `x, y = y, x`  
   D. `x += y`  

2. 关于Python变量命名规则，错误的是？  （b）
   A. `_name`  
   B. `3hours`  
   C. `user_name`  
   D. `count2`  

3. 以下哪个不是Python的关键字？  （a）
   A. `cout`  
   B. `not`  
   C. `or`  
   D. `lambda`  

4. 表达式 `4 ** 2` 的结果是？  （c）
   A. 6  
   B. 8  
   C. 16  
   D. 12  

5. 若 `a = [1, 2, 3]`，执行 `a[1] = 10` 后，`a` 的值是？  （a）
   A. `[1, 10, 3]`  
   B. `[1, 2, 3]`  
   C. `[10, 2, 3]`  
   D. 错误  

6. 以下哪个表示元组？  （c）
   A. `[1, 2, 3]`  
   B. `{1, 2, 3}`  
   C. `(1, 2, 3)`  
   D. `{1: "a"}`  

7. 字符串 `"hello"[0]` 的值是？  （a）
   A. `"h"`  
   B. `"e"`  
   C. `"hello"`  
   D. 错误  

8. 下列哪个方法用于删除列表中的元素？  （c）
   A. `add()`  
   B. `append()`  
   C. `pop()`  
   D. `insert()`  

9. 集合操作中，`intersection()` 表示？  （c）
   A. 并集  
   B. 差集  
   C. 交集  
   D. 对称差集  

10. 函数 `type(None)` 的返回值类型是？  （b）
    A. `int`  
    B. `NoneType`  
    C. `str`  
    D. `bool`  

11. 以下关于注释的描述，错误的是？  （c）
    A. 单行注释以 `#` 开头  
    B. 多行注释可用三引号  
    C. 注释参与程序执行  
    D. 注释用于解释代码用途  

12. 若 `x = [1, 2, 3]`，切片 `x[1:3]` 的结果是？  （c）
    A. `[1]`  
    B. `[2]`  
    C. `[2, 3]`  
    D. `[1, 2]`  

13. 以下哪个函数用于获取用户输入？  （b）
    A. `print()`  
    B. `input()`  
    C. `read()`  
    D. `get()`  

14. 表达式 `10 + 5 // 3` 的值是？  （b）
    A. 5  
    B. 11  
    C. 12  
    D. 15  

15. 下列数据类型中，Python不支持的是？  （a）
    A. `char`  
    B. `int`  
    C. `list`  
    D. `dict`  

16. 字典的键（Key）必须是？  （a）
    A. 可哈希类型  
    B. 整数类型  
    C. 字符串类型  
    D. 列表类型  

17. 以下代码的输出结果是？  （a）
    ```python  
    s = "Python"  
    print(s[1:4])  
    ```  
    A. `yth`  
    B. `Pyt`  
    C. `thon`  
    D. `ytho`  

18. 以下哪个表达式返回 `True`？  （b）
    A. `3 > 3`  
    B. `"a" in "apple"`  
    C. `[] is None`  
    D. `7 == "7"`  

19. 关于文件操作，以下描述错误的是？  （C）
    A. `open()` 函数用于打开文件  
    B. `"w"` 模式会覆盖文件原有内容  
    C. `readline()` 读取整篇文件  
    D. `close()` 用于关闭文件  

20. 以下哪个模块用于数学运算？  （b）
    A. `random`  
    B. `math`  
    C. `sys`  
    D. `os`  

21. 异常处理中，`finally` 块的作用是？  （A）
    A. 无论是否发生异常都会执行  
    B. 仅当发生异常时执行  
    C. 仅当无异常时执行  
    D. 替代 `except` 块  

22. 若 `s = {1, 2, 3}`，执行 `s.add(2)` 后，`s` 的值是？  （A）
    A. `{1, 2, 3}`  
    B. `{1, 2, 2, 3}`  
    C. 报错  
    D. `{1, 3}`  

23. 以下代码的输出结果是？  （A）
    ```python  
    def func(x):  
        return x * 2  
    print(func("ab"))  
    ```  
    A. `"abab"`  
    B. `"aabb"`  
    C. 报错  
    D. `2`  

24. 列表推导式 `[x**2 for x in range(5)]` 的结果是？  （A）
    A. `[0, 1, 4, 9, 16]`  
    B. `[1, 4, 9, 16, 25]`  
    C. `[0, 1, 2, 3, 4]`  
    D. `[1, 2, 3, 4, 5]`  

25. 以下关于类和对象的描述，正确的是？  （C）
    A. 类是对象的实例  
    B. 对象是类的模板  
    C. 方法必须包含 `self` 参数  
    D. 属性不能动态添加  

26. 以下代码的输出结果是？  （A）
    ```python  
    for i in range(3):  
        print(i, end=",")  
    ```  
    A. `0,1,2,`  
    B. `0,1,2`  
    C. `1,2,3`  
    D. `1,2,3,`  

27. 表达式 `bool("0")` 的值是？  （b）
    A. `False`  
    B. `True`  
    C. `0`  
    D. 报错  

28. 以下哪个函数用于生成随机整数？  （b）
    A. `random()`  
    B. `randint()`  
    C. `choice()`  
    D. `shuffle()`  

29. 若 `x = 10`，执行 `y = x` 后，`id(x) == id(y)` 的结果是？  （A）
    A. `True`  
    B. `False`  
    C. 报错  
    D. 不确定  

30. 以下代码的输出结果是？  （A）
    ```python  
    print("Python".replace("t", "T"))  
    ```  
    A. `"PyThon"`  
    B. `"Python"`  
    C. `"PytHon"`  
    D. 报错  

31. 以下关于模块的描述，错误的是？  （d）
    A. 模块是 `.py` 文件  
    B. `import math` 引入数学模块  
    C. `__name__` 表示当前模块名  
    D. 模块不能包含类定义  

32. 以下代码的输出结果是？  （b）
    ```python  
    a = [1, 2]  
    b = a  
    b.append(3)  
    print(a)  
    ```  
    A. `[1, 2]`  
    B. `[1, 2, 3]`  
    C. `[3]`  
    D. 报错  

33. 以下哪个表达式将字符串转换为整数？  （b）
    A. `str(10)`  
    B. `int("10")`  
    C. `float("10")`  
    D. `list("10")`  

34. 以下代码的输出结果是？  （b）
    ```python  
    t = (1,)  
    print(type(t))  
    ```  
    A. `<class 'int'>`  
    B. `<class 'tuple'>`  
    C. `<class 'list'>`  
    D. `<class 'set'>`  

35. 以下关于 `lambda` 函数的描述，正确的是？  （D）
    A. 可包含多个表达式  
    B. 必须有函数名  
    C. 用于定义复杂函数  
    D. 匿名函数  

36. 以下代码的输出结果是？  （A）
    ```python  
    s = "hello"  
    print(s.find("l"))  
    ```  
    A. `2`  
    B. `3`  
    C. `-1`  
    D. `1`  

37. 以下哪个方法用于向文件写入多行？  （b）
    A. `write()`  
    B. `writelines()`  
    C. `readlines()`  
    D. `append()`  

38. 表达式 `[1, 2] + [3, 4]` 的结果是？  （A）
    A. `[1, 2, 3, 4]`  
    B. `[4, 6]`  
    C. `[1, 3, 2, 4]`  
    D. 报错  

39. 以下代码的输出结果是？  （b）
    ```python  
    x = 10  
    def func():  
        global x  
        x = 20  
    func()  
    print(x)  
    ```  
    A. `10`  
    B. `20`  
    C. 报错  
    D. `None`  

40. 以下关于迭代器的描述，正确的是？  （b）
    A. 列表不是可迭代对象  
    B. `iter()` 函数创建迭代器  
    C. 迭代器不支持 `next()`  
    D. 字典键不可迭代  

---

### 二、基本编程题（10题×3分=30分）  
1. **数值计算**：输入两个整数，计算并输出它们的和、差、积、商（整除）。  
```python
try:
    # 输入两个整数（空格分隔）
    a, b = map(int, input("请输入两个整数（用空格分隔）: ").split())
    
    # 计算和、差、积
    sum_result = a + b
    difference = a - b
    product = a * b
    
    # 计算整除商（需检查除数非零）
    if b != 0:
        quotient = a // b  # 整除运算
    else:
        raise ZeroDivisionError("除数不能为零")
    
    # 输出结果
    print(f"和: {sum_result}")
    print(f"差: {difference}")
    print(f"积: {product}")
    print(f"商（整除）: {quotient}")

except ValueError:
    print("输入错误：请确保输入的是两个整数，用空格分隔")
except ZeroDivisionError as e:
    print(f"计算错误：{e}")
```
2. **字符串反转**：输入一个字符串，输出其反转后的结果（如 `"hello"` → `"olleh"`）。  
```python
text='hello'
print(text[::-1])
```
3. **列表去重**：输入一个包含重复元素的列表，输出新列表（元素顺序不限）。 
```python
def remove_duplicates(input_list):
    return list(set(input_list))
# 示例
input_list = [3, 1, 2, 2, 4, 3, 5, 4]
print(remove_duplicates(input_list))  # 可能输出 [1, 2, 3, 4, 5]（顺序随机）
```
5. **字典统计**：输入一个字符串，统计每个字符出现的次数，输出字典（如 `"apple"` → `{'a':1, 'p':2, 'l':1, 'e':1}`）。
```python
def count_characters(input_string):
    """
    统计字符串中每个字符出现的次数
    
    参数:
        input_string: 要统计的字符串
        
    返回:
        包含字符及其出现次数的字典
    """
    char_count = {}
    
    for char in input_string:
        # 方法1: 使用条件判断
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
        # 方法2: 使用get方法 (更简洁)
        # char_count[char] = char_count.get(char, 0) + 1
        
    return char_count

# 使用示例
user_input = input("请输入要统计的字符串：")
result = count_characters(user_input)
print("字符统计结果：", result)
```  
6. **文件读写**：创建一个文件 `data.txt`，写入内容 `"Python Programming"`，然后读取并打印内容。  
```python
# 写入文件
with open('data.txt', 'w') as file:
    file.write("Python Programming")

# 读取文件
with open('data.txt', 'r') as file:
    content = file.read()

# 打印文件内容
print("文件内容:", content)
``` 
7. **阶乘计算**：编写函数 `factorial(n)`，用递归计算并返回 `n!`（如 `5! = 120`）。  
```python
def factorial(n):
    """递归计算n的阶乘"""
    if n == 0 or n == 1:  # 基本情况
        return 1
    else:
        return n * factorial(n - 1)  # 递归调用

# 测试函数
print(factorial(5))  # 输出: 120
print(factorial(0))  # 输出: 1
print(factorial(1))  # 输出: 1
print(factorial(10))  # 输出: 3628800
``` 
8. **素数判断**：输入一个整数，判断是否为素数，输出 `True` 或 `False`。  
```python
def is_prime(n):
    """判断一个整数是否为素数"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # 只需检查到平方根即可
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# 测试函数
print(is_prime(2))    # 输出: True
print(is_prime(17))    # 输出: True
print(is_prime(15))    # 输出: False
print(is_prime(1))     # 输出: False
print(is_prime(97))    # 输出: True
print(is_prime(100))   # 输出: False
``` 
9.  **日期格式化**：获取当前日期和时间，格式化为 `YYYY-MM-DD HH:MM:SS` 并输出。  
```python
from datetime import datetime

# 获取当前日期时间
now = datetime.now()

# 格式化为指定字符串
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

# 输出结果
print("当前日期时间:", formatted_time)
``` 
10. **集合运算**：输入两个集合，求它们的交集、并集和差集。  
```python
# 输入两个集合
set1 = set(input("请输入第一个集合（元素用空格分隔）: ").split())
set2 = set(input("请输入第二个集合（元素用空格分隔）: ").split())

# 计算集合运算
intersection = set1 & set2  # 或 set1.intersection(set2)
union = set1 | set2         # 或 set1.union(set2)
difference1 = set1 - set2   # 或 set1.difference(set2)
difference2 = set2 - set1   # 或 set2.difference(set1)

# 输出结果
print(f"集合1: {set1}")
print(f"集合2: {set2}")
print(f"交集: {intersection}")
print(f"并集: {union}")
print(f"差集（set1 - set2）: {difference1}")
print(f"差集（set2 - set1）: {difference2}")
``` 
11. **回文数检测**：输入一个整数，判断是否为回文数（正序与倒序相同，如 `121`）。  
```python
def is_palindrome(num):
    """判断一个整数是否为回文数"""
    # 处理负数情况（负数不可能是回文数）
    if num < 0:
        return False
    
    # 将数字转换为字符串进行比较
    num_str = str(num)
    return num_str == num_str[::-1]

# 测试函数
print(is_palindrome(121))    # 输出: True
print(is_palindrome(12321))  # 输出: True
print(is_palindrome(123))    # 输出: False
print(is_palindrome(-121))   # 输出: False
print(is_palindrome(0))      # 输出: True
``` 

---

### 三、综合应用题（2题×15分=30分）  
1. **学生成绩管理系统**  
   - **要求**：  
     - 定义 `Student` 类，包含属性：姓名（`name`）、学号（`id`）、三门成绩（`math`, `english`, `python`）。  
     - 类方法包括：  
       - 计算总分（`total_score`）  
       - 计算平均分（`average_score`）  
       - 输出学生信息（`display_info`）  
     - 创建至少两个学生对象，调用方法输出每个学生的总分、平均分及完整信息。  
```python
class Student:
    def __init__(self, id, name, math, english, python):
        self.id = id
        self.name = name
        self.math = math
        self.english = english
        self.python = python
    
    def get_total_score(self):
        return self.math + self.english + self.python
    
    def get_average_score(self):
        return self.get_total_score() / 3
    
    def display_info(self):
        print(f"学号: {self.id}, 姓名: {self.name}")
        print(f"成绩: 数学={self.math}, 英语={self.english}, Python={self.python}")
        print(f"总分: {self.get_total_score()}, 平均分: {self.get_average_score():.2f}\n")

# 创建学生对象
stu1 = Student("S001", "张三", 85, 90, 92)
stu2 = Student("S002", "李四", 78, 88, 95)
stu1.display_info()
stu2.display_info()
``` 

2. **股票价格波动分析**  
   - **要求**：  
     - 从文件 `stock.txt` 读取数据（每行一个交易日的收盘价）。  
     - 计算以下指标：  
       - 最长连续上涨/下跌天数  
       - 最高价和最低价  
       - 价格波动率（标准差）  
     - 将结果写入新文件 `report.txt`，包含原始数据和计算结果。  
```python
def analyze_stock(file_path):
    with open(file_path, "r") as f:
        prices = [float(line.strip()) for line in f]
    
    # 计算统计指标
    total = sum(prices)
    avg = total / len(prices)
    max_price = max(prices)
    min_price = min(prices)
    
    # 计算最长连续上涨/下跌
    up_days = down_days = current_up = current_down = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            current_up += 1
            current_down = 0
        else:
            current_down += 1
            current_up = 0
        up_days = max(up_days, current_up)
        down_days = max(down_days, current_down)
    
    # 写入结果文件
    with open("report.txt", "w") as f:
        f.write(f"原始数据: {prices}\n")
        f.write(f"总和: {total:.2f}\n")
        f.write(f"平均值: {avg:.2f}\n")
        f.write(f"最高价: {max_price:.2f}\n")
        f.write(f"最低价: {min_price:.2f}\n")
        f.write(f"最长连续上涨天数: {up_days}\n")
        f.write(f"最长连续下跌天数: {down_days}\n")

analyze_stock("stock.txt")
``` 
---  
题目设计参考标准：  
- 选择题覆盖语法基础、数据类型、运算符、控制结构、函数、文件、异常、OOP等核心内容。  
- 编程题注重基础操作能力（输入输出、字符串、列表、字典、文件）。  
- 综合应用题结合数据分析和OOP，考察问题分解和代码组织能力。