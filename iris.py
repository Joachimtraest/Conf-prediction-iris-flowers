
class Iris:

    def __init__(self, species=None, sepal_length=None, sepal_width=None, petal_length=None, petal_width=None, flower_index = None):
        self.species = species
        self.sepal_length = sepal_length
        self.petal_width = petal_width
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.flower_index = flower_index
        pass

    def get_species(self):
        return self.species

    def get_sepal_length(self):
        return self.sepal_length
    
    def get_sepal_width(self):
        return self.sepal_length

    def get_petal_width(self):
        return self.petal_width
    
    def get_petal_length(self):
        return self.petal_length

    def set_species(self, new_species):
        self.species = new_species
        return

    def set_sepal_length(self, new_sepal_length):
        self.sepal_length = new_sepal_length
        return

    def set_sepal_width(self, new_sepal_width):
        self.sepal_width = new_sepal_width
        return

    def set_petal_width(self, new_petal_width):
        self.petal_width = new_petal_width
        return
    
    def set_petal_length(self, new_petal_length):
        self.petal_length = new_petal_length
        return
class Iris_Dataset:
    def __init__(self):
        self.species_data=[]
        self.sepal_length_data=[]
        self.sepal_width_data=[]
        self.petal_length_data=[]
        self.petal_width_data=[]
        self.flowerlist = []
        self.lenght = 0        
        pass

    def add_iris(self, iris):
        self.species_data.append(iris.species)
        self.sepal_length_data.append(iris.sepal_length)
        self.sepal_width_data.append(iris.sepal_width)
        self.petal_length_data.append(iris.petal_length)
        self.petal_width_data.append(iris.petal_width)
        self.flowerlist.append(iris)
        self.lenght += 1

    def get_unique_species(self):
        return list(set(self.species_data))

