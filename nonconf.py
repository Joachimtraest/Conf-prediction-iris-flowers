class Conf_Predict:
    
    @staticmethod
    def get_nonconf_scores(A, train_flowers,  new_flower, species, epsilon=0.05): #A = nonconformity measure
            #this function creates the list of nonconformity scores
            new_flower.set_species(species)
            all_flowers = train_flowers[:]
            all_flowers.append(new_flower)
            alpha_list = []
            for i in range(len(all_flowers)):
                other_flowers = all_flowers[:i] + all_flowers[i+1:]
                alpha_list.append(A(all_flowers[i], other_flowers))
            return alpha_list

    @staticmethod
    def get_py(A, train_flowers, new_flower, species, epsilon = 0.05): 
        #this value py is the fraction of the flowers that are at least as different from the others as the new flowers is
        #p.386 in shafer and vovk: tutorial on conformal prediction
        alpha_list = Conf_Predict.get_nonconf_scores(A, train_flowers, new_flower, species, epsilon)
        count = 0
        for i in alpha_list[:]:
            if i >= alpha_list[-1]:
                count += 1
        print(count)
        return count/(len(train_flowers) + 1)

    @staticmethod
    def NN(flower, other_flowers): #nearest neigbour nonconformity measure p. 389 shafer and vovk: tutorial on conformal prediction
        dist1 = []
        dist2 = []
        for j in other_flowers:
            if j.species == flower.species:
                dist1.append(abs(flower.sepal_length - j.sepal_length))
            else:
                dist2.append(abs(flower.sepal_length - j.sepal_length))
        min1 = min(dist1)
        min2 = min(dist2)
        if min1 == 0.0 and min2 == 0.0:
            alpha =  0
        elif min1 != 0.0 and min2 == 0.0:
            alpha = 9999999999999
        else:
            alpha = min1/min2
        return alpha
    