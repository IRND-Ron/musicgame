import person

john = person.Person("John")
paul = person.Person("Paul")

print ("\nwhere did they start:")
john.where()
paul.where()

john.walk(10, 2)
paul.walk(10, 9)

john.run(100, 5)
paul.run(100, 4)

print ("\nwhere are they now:")
john.where()
paul.where()


print("\nfinished")
