Python 中格式化字符串的方法有几种，以下是一些常见的字符串格式化技术：

### 1. 百分号（%）格式化
使用 `%` 符号和格式化字符串，可以插入变量或值。

```python
name = "Kimi"
age = 23
greeting = "Hello, %s. You are %d years old." % (name, age)
print(greeting)  # 输出: Hello, Kimi. You are 23 years old.
```

### 2. `str.format()` 方法
使用 `format()` 方法，可以在字符串中使用花括号 `{}` 作为占位符。

```python
name = "Kimi"
age = 23
greeting = "Hello, {}. You are {} years old.".format(name, age)
print(greeting)  # 输出: Hello, Kimi. You are 23 years old.
```

你还可以通过关键字参数来提高可读性：

```python
greeting = "Hello, {name}. You are {age} years old.".format(name=name, age=age)
```

### 3. f-string（格式化字符串字面量，Python 3.6+）
使用以 `f` 或 `F` 开头的字符串字面量，可以方便地嵌入表达式。

```python
name = "Kimi"
age = 23
greeting = f"Hello, {name}. You are {age} years old."
print(greeting)  # 输出: Hello, Kimi. You are 23 years old.
```

f-string 还支持更复杂的表达式：

```python
total = 100
part1 = 30
part2 = 50
percentage = f"Part1: {(part1 / total * 100):.2f}%, Part2: {(part2 / total * 100):.2f}%"
print(percentage)  # 输出: Part1: 30.00%, Part2: 50.00%
```

### 4. `%` 操作符的高级用法
`%` 操作符还可以用于更复杂的格式化，如指定宽度、填充字符、对齐等。

```python
value = 123456.789
formatted_value = "Value: %10.2f" % value  # 宽度为10，保留两位小数
print(formatted_value)  # 输出: Value:  123456.79
```

### 5. 使用模板字符串
Python 的 `string` 模块提供了 `Template` 类，允许使用 `$` 符号进行字符串替换。

```python
from string import Template

t = Template('Hello, $name. You are $age years old.')
result = t.substitute(name='Kimi', age=23)
print(result)  # 输出: Hello, Kimi. You are 23 years old.
```

