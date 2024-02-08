class my_name:
    name = ""
    lastname = ""
    age = 0

    def a_name(self):
        print("Hello, ",self.name,self.lastname,self.age)

the_name = my_name()
the_name.name = 'pattapon'
the_name.lastname ='suwanwong'
the_name.age ='21'

the_name_2 = my_name()
the_name_2.name = 'Julius'
the_name_2.lastname ='Lol'
the_name_2.age ='1,000'

the_name_3 = my_name()
the_name_3.name = 'Nabil'
the_name_3.lastname ='Rum'
the_name_3.age ='210'

the_name_4 = my_name()
the_name_4.name = 'Bung'
the_name_4.lastname ='Bung'
the_name_4.age ='121'

the_name.a_name()
the_name_2.a_name()
the_name_3.a_name()
the_name_4.a_name()