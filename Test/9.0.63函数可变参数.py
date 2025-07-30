def info(**kwargs):
    names = kwargs['names']
    gender_list = kwargs['gender']
    age_list = kwargs['age']
    index = 0
    for name in names:
        gender = gender_list[index]
        age = age_list[index]
        print('name: {}, gender: {}, age: {}'.format(name, gender, age))
        index += 1

info(names = ['Alice', 'Bob', 'Candy'], gender = ['girl', 'boy', 'girl'], age = [16, 17, 15])