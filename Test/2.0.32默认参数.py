def greet(name, msg="Hello"):
    """使用指定的问候语和名字生成问候消息"""
    return f"{msg}, {name}!"


# 示例调用
print(greet("Alice"))  # 输出: Hello, Alice!
print(greet("Bob", "Hi"))  # 输出: Hi, Bob!