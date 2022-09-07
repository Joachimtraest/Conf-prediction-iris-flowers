class CP_Iris:
    
    @staticmethod
    def get_nonconf_scores(A, new_flower, train_flowers, species, epsilon=0.05): #A = nonconformity measure
            #this function creates the list of nonconformity scores
            print(new_flower)
            new_flower.set_species(species)
            all_flowers = train_flowers[:]
            all_flowers.append(new_flower)
            alpha_list = []
            for i in range(len(all_flowers)):
                other_flowers = all_flowers[:i] + all_flowers[i+1:]
                alpha_list.append(A(all_flowers[i], other_flowers))
            return alpha_list

    @staticmethod
    def get_py(A,  new_flower,  train_flowers ,species, epsilon = 0.05): 
        #this value py is the fraction of the flowers that are at least as different from the others as the new flowers is
        #p.386 in shafer and vovk: tutorial on conformal prediction
        alpha_list = CP_Iris.get_nonconf_scores(A,  new_flower, train_flowers, species, epsilon)
        count = 0
        for i in alpha_list[:]:
            if i >= alpha_list[-1]:
                count += 1
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
    
    @staticmethod
    def Dist_to_avg(flower, other_flowers):
        #distance to the average of each species nonconformity measure (p. 392 in Shafer and Vovk)
        all_flowers = other_flowers[:]
        all_flowers.append(flower)
        species_list = []
        for i in all_flowers:
            species_list.append(i.species)
        
        sepal_lengths = []

        for j in all_flowers:
            if j.species == flower.species:
                sepal_lengths.append(j.sepal_length)
        avg = sum(sepal_lengths)/len(sepal_lengths)
        return abs(avg - flower.sepal_length)

    @staticmethod
    def classify_Iris(A, flower, other_flowers, possible_species):
        #gives the corresponding epsilon for each prediction region 
        p_list = []
        for i in possible_species:
            p = CP_Iris.get_py(A, flower, other_flowers, i)
            p_list.append((i,p))
        
        sorted_list = sorted(p_list)
        all_elements = ''
        for i in sorted_list:
            all_elements += i[0] + ','
        print('if epsilon is < ' +  str(sorted_list[0][1])  + ' the prediction region includes: ' + all_elements)
        for j in range(1, len(sorted_list)):
            elements = ''
            for k in sorted_list[j:]:
                elements += k[0] + ','
            print('if epsilon is > ' +  str(sorted_list[j-1][1]) + ' and < ' + str(sorted_list[j][1]) + ' the prediction region includes ' + elements  )
        print('if epsilon is > ' + str(sorted_list[-1][1]) + ' the prediction region is empty')
        return