url="Http://tyrionyu.github.io/"
'''删除前缀'''
simple_url=url.removeprefix("Http://")  #完全匹配才会删除
print(simple_url)
'''删除后缀'''
simple_url_back=simple_url.removesuffix('/')
print(simple_url_back)