# Словари повторение
d = {}
# print(d)
# d["David"] = "dell"
# d["Pavel"] = "sam"
# d.update({"Julia": "asus", "Svetlana":"hp"})
# print(d["Svetlana"])
# print(d.items())
# print(d.keys())
# print(d.values())
# for k, v in d.items():
#     print(v, k) # меняет местами

my_list = [42, 43]
my_dict = {
   'foo': {
      'a':12,
      'b': (1, 2, 3, 4, my_list)
   },
   'bar': {
      'c':12,
      'd': {5, 6, 7, 8}
   },
   'moo': {
      'e':12,
      'f': {'Lol': ['L', 'o', 'l']}
   },
}
print(my_dict['foo'])
print(my_dict['foo']['b'])
my_list.append(44)
print(my_dict['foo']['b'])
print(my_dict['bar']['d'])