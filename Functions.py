# def find_total(expenses):
#     '''
#     This function takes expenses list as input and returns a total sum of that list
#     :param expenses: list of input expenses
#     :return: total expense
#     '''
#     total = 0
#     for expense in expenses:
#         total += expense
#     return total
#
# expenses_sergey = [30, 45, 70, 90]
# expenses_sundar = [40, 23, 10, 85]
#
# total = find_total(expenses_sergey)
#
# print("Sergey's total expense: ", total)
#
#
# total = find_total(expenses_sundar)
#
#
# print("Sundar's toal expense: ", total)

def find_cylinder_volume(radius, height):
    print("radius:", radius)
    print("height:", height)
    volume = 3.14 *(radius**2)*height
    return volume

r = 5
h = 10

print(find_cylinder_volume(radius=r, height=h))
























