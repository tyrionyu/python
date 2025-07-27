d = {
    'Alice': 45,
    'Bob': 60,
    'Candy': 75,
    'David': 86,
    'Ellena': 49
}
old_score = d.get('Alice')
d['Alice'] = 60
print(old_score)