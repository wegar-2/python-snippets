

class SimpleClass:
    pass


class ComplexClass(SimpleClass):
    def __init__(self):
        pass


base_inst = SimpleClass()
derived_inst = ComplexClass()

print(base_inst.__class__)
print(base_inst.__class__.__bases__)
print(base_inst.__class__.__base__)
print(type(type(base_inst)))
