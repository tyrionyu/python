guest=["张三","李四",'王五']

name=guest[0]
print(f"{name},邀请你和我一起晚餐")

name=guest[1]
print(f"{name},邀请你和我一起晚餐")

name=guest[2]
print(f"{name},邀请你和我一起晚餐")

name=guest[1]
print(f"{name},没有办法来参加晚餐")

del(guest[1])
guest.insert(1,"老六")
name=guest[1]
print(f"{name},邀请你和我一起晚餐")
print(guest)