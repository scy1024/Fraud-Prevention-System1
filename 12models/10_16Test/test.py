class Person:
#{
  state = "NSW"
  def __init__(self, first_name, last_name, age, phone, email):
  #{
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.phone = phone
    self.email = email
  #}
  def __str__(self):
    return "{} {}: {} years old\nContact: {}, {}".format(self.first_name, self.last_name, self.age, self.phone, self.email)
  def __repr__(self):
    return "Person('{}', '{}', {}, '{}', '{}')".format(self.first_name, self.last_name, self.age, self.phone, self.email)
  @staticmethod
  def get_uni_website():
    return "www.uow.edu.au"
  @classmethod
  def get_state(cls):
    return  "State: " + cls.state
#}

# create objects:
personObj1 = Person("John", "Lee", 19, "0400000000", "jl123@gmail.com")
personObj2 = Person("Mary", "Zheng", 25, "0242239999", "maryz@gmail.com")
personObj3 = Person("Cindy", "Wilson", 53, "0430982200", "cw456@hotmail.com")

# display the string of each person object
print(str(personObj1))
print(str(personObj2))
print(str(personObj3))

# display the code of building each person object
print(repr(personObj1))
print(repr(personObj2))
print(repr(personObj3))

# display the university's website using the static method
print(Person.get_uni_website())

# display the state using the class method
print(Person.get_state())