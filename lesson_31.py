# До баз данных полторы - 2 недели

# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         "tel": tel
#     }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = {}
#
#     data.append(person_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person()[0], gen_person()[1])

# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#     while len(name) != 7:
#         name += choice(letters)
#     while len(tel) != 10:
#         tel += choice(nums)
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person, tel
#
#
# def write_json(person_dict, num):
#     try:
#         data = json.load(open('persons1.json'))
#     except FileNotFoundError:
#         data = {}
#     data[num] = person_dict
#     with open('persons1.json', 'w') as f:
#         json.dump(data, f, indent=2, ensure_ascii=False)
#
#
# for i in range(5):
#     write_json(gen_person()[0], gen_person()[1])

# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         # st = ''
#         # for i in self.marks:
#         #     st += str(i) + ', '
#         # return f"{self.name}: {st[:-2]}"
#         st = ', '.join(map(str, self.marks))
#         return f"{self.name}: {st}"
#
#     def add_mark(self, new_mark):
#         self.marks.append(new_mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return sum(self.marks) / len(self.marks)
#
#     # пересмотреть что-то упустил
#     def dump_to_json(self, file_name):
#         data = {"name": self.name, "marks": self.marks}
#         with open(file_name, "w") as f:
#             json.dump(data, f, indent=2)
#
#     def load_from_file(self, file_name):
#         with open(file_name, "r") as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         st = ''
#         for i in self.students:
#             st += str(i) + '\n'
#         return f"Группа:{self.group}\n{st}"
#         # st = '\n'.join(map(str, self.students))
#         # return f"{st}"
#
#     @staticmethod
#     def change_group(gr1, gr2, index):
#         return gr2.add_student(gr1.remove_student(index))
#
#     def add_student(self, new_student):
#         self.students.append(new_student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     def dump_group(self, file_name):
#         with open(file_name, "w") as f:
#             stud_list = []
#             for i in self.students:
#                 stud_list.append([i.name, i.marks])
#             json.dump(stud_list, f, indent=2)
#
#     def jornal_groups(self, file_name):
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = []
#
#         with open(file_name, "w") as f:
#             stud_list = []
#             for i in self.students:
#                 stud_list.append([i.name, i.marks])
#             data.append(stud_list)
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def upload_group(file_name):
#         with open(file_name, "r") as f:
#             print(json.load(f))
#
#
# # st1 = Student(name:'Bodnya', marks: [5, 4, 3, 4, 5, 3]) ???
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(2)
# # print(st1)
# # st1.edit_mark(4, 4)
# # print(st1)
# # print(st1.average_mark())
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 4, 2])
# st3 = Student('Birkov', [3, 5, 3, 2, 5, 4])
# sts1 = [st1, st2]
# group1 = Group(sts1, "GK Python")
# group1.add_student(st3)
# # print(group1)
# group1.remove_student(1)
# print(group1)
# sts2 = [st2]
# group2 = Group(sts2, "GK Web")
# print(group2)
# print()
# Group.change_group(group1, group2, 0)
# print(group1)
# print(group2)
# # file = "student.json"
# # st1.dump_to_json(file)
# # st1.load_from_file(file)
# # file = "group 1.json"
# # group1.dump_group(file)
# # group1.upload_group(file)
# #
# # file2 = "group 2.json"
# # group2.dump_group(file2)
# # group2.upload_group(file2)
#
# # files_group = "journal.json"
# # # group1.jornal_groups(files_group)
# # group2.jornal_groups(files_group)

#Дальше идет начало домашки, досмотреть последние пол часа