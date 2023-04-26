class_name = "Person"

Person = type(class_name, (), {
    "name": "",
    "age": 0,
    "get_info": lambda self: f"My name is {self.name} and I am {self.age} years old."
})

person = Person()
person.name = "Alice"
person.age = 30

print(person.get_info())
