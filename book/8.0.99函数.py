# def get_f_name(f_name,l_name,m_name=''):
#     if m_name:
#         full_name=f'{f_name}{m_name}{l_name}'
#     else:
#         full_name=f'{f_name}{l_name}'
#     return full_name.title()
# M=get_f_name('zhenjia','yu')
# print(M)

"""名字"""
# def build_preson(f_name,l_name):
#     person={'first':f_name,'last':l_name}
#     return person
# L=build_preson('zhengjia','yu')
# print(L)
# print(type(L))

""

"""加入年龄"""
# def build_preson(f_name,l_name,age=None):
#     person={'first':f_name,'last':l_name}
#     if age:
#         person['age']=age
#     return person
# A=build_preson('zhengjia','yu',29)
# print(A)

"""名字加循环"""

def get_f_name(f_name, l_name):
    full_name = f"{f_name} {l_name}"
    return full_name.title()


while True:
    print(f"\nPlease tell me your name:")
    print(f"(enter 'q' at any time to quit!")

    f_name = input("First name:")
    if f_name == "q":
        break

    l_name = input("Last name:")
    if l_name == "q":
        break
    M = get_f_name(f_name, l_name)

    print(f"\nHello,{M}")
