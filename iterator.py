# !-2 misol uchun
# class Malumot:
#     object = []
#     counter=0
#     def __init__(self, f_name):
#         self.f_name = f_name
#         self.object.append(self)
    
    
    
#     def __iter__(self, *args):
#         return self
    

#     def __next__(self, *args):
#         try:
#             object = self.object[self.counter]

#             self.counter += 1
#             return object.f_name
#         except IndexError:
#             counter=0
#             raise StopIteration()
    
# Malumot('salom')
# Malumot('axliddin')
# Malumot('shokirov')
# Malumot('qaleiszzzzsss')\


# for i in Malumot(''):
#     print(i)


# for i in Malumot(''):
#     print(i)

#3-misol

# class Malumot:
#     object = []
#     counter=0
#     def __init__(self, f_name):
#         self.f_name = f_name
#         self.object.append(self)
    
    
    
#     def __iter__(self, *args):
#         return self
    

#     def __next__(self, *args):
#         try:
#             object = self.object[self.counter]

#             self.counter += 1
#             return object.f_name
#         except IndexError:
#             counter=0
#             raise StopIteration()
    
# Malumot('salom')
# Malumot('axliddin')
# Malumot('shokirov')
# Malumot('qaleiszzzzsss')
# a=list(filter(lambda x:x , Malumot('')))
# print(a)



# # 4-misol
class Malumot:
    objects = []
    mal_id = 1  
    
    def __init__(self, f_name):
        self.f_name = f_name
        self.id = Malumot.mal_id 
        Malumot.mal_id += 1
        self.__class__.objects.append(self)
    
    def __iter__(self):
        self.counter = 0
        return self
    
    def __next__(self):
        if self.counter < len(self.__class__.objects):
            obj = self.__class__.objects[self.counter]
            self.counter += 1
            return obj
        else:
            raise StopIteration()
    
    @classmethod
    def id_mal(cls):
        return [obj.id for obj in cls.objects]

Malumot('salom')
Malumot('axliddin')
Malumot('shokirov')
Malumot('qaleiszzzzsss')


id_list = Malumot.id_mal()
print("Barcha IDlar:", id_list)


    





