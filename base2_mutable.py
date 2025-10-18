def get_person():
    name = "Shige"
    age = 24
    city = "Osaka"
    return name, age, city


def get_numbers():
    return 1, 2, 4, 5, 56

first, *others, last = get_numbers()


def try_modify_number(num):
    num += 10
    print(f"関数内:{num}")

x = 5
try_modify_number(x)
try_modify_number(x)
print(x)

def modify_list(some_list):
    some_list.append(100)

sample_list = [1, 2, 3]
modify_list(sample_list)
print(sample_list)