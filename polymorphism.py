class India:
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class Bangladesh:
    def capital(self):
        print("Dhaka is the capital of India.")

    def language(self):
        print("Bengali is the most widely spoken language of Bangladesh.")

    def type(self):
        print("Bangladesh is a developing country.")
obj_ind=India()
obj_Bangladesh=Bangladesh()

for country in(obj_ind,obj_Bangladesh):
    country.capital()
    country.language()
    country.type()
    