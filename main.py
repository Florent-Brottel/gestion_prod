def generate_combinations(): #fonction qui calcule toutes les possibilités de production pour chaque année en respactant les contraintes : la première case ne peut pas être inférieur à 11. la somme des 5 cases doit être de 83. on veut case 1 + case 2 supérieur ou égal à 22, case 1 + case 2 + case 3 supérieur ou égal à 42, case 1 + case 2 + case 3 + case 4 supérieur ou égal à 62
    combinations = []
    for case1 in range(11, 73):  # La première case ne peut pas être inférieure à 11, car il y a 83 - 11 * 4 = 39 restant pour les autres cases
        for case2 in range(11, 73):  # De même pour la deuxième case
            for case3 in range(11, 73):  # De même pour la troisième case
                for case4 in range(11, 73):  # De même pour la quatrième case
                    case5 = 83 - (case1 + case2 + case3 + case4)  # Calcul de la cinquième case pour que la somme soit égale à 83
                    if case5 >= 11:  # Vérification que la cinquième case est supérieure ou égale à 11
                        if case1 + case2 >= 22 and case1 + case2 + case3 >= 42 and case1 + case2 + case3 + case4 >= 62:
                            combinations.append([case1, case2, case3, case4, case5])
    return combinations

def main():
    stock_min = [11, 11, 20, 20, 21]  # stock minimum pour chaque année
    combinations = generate_combinations()

    # Tri des combinaisons par stock total
    combinations.sort(key=lambda x: sum(max(x[i] - stock_min[i], 0) for i in range(5)))

    print("Combinaisons avec le stock le plus faible:")
    for i in range(5):
        combination = combinations[i]
        stock = sum(max(combination[i] - stock_min[i], 0) for i in range(5))
        print("Combinaison de prod :", combination)
        print("Stock total sur l'ensemble des années :", stock)
        print("Écart entre chaque case :", [combination[i] - combination[i - 1] for i in range(1, len(combination))])
        print()

    # Tri des combinaisons par écart minimum entre chaque case
    combinations.sort(key=lambda x: max(x) - min(x))

    print("Combinaisons avec le moins d'écart entre chaque case:")
    for i in range(5):
        combination = combinations[i]
        stock = sum(max(combination[i] - stock_min[i], 0) for i in range(5))
        print("Combinaison de prod :", combination)
        print("Stock total sur l'ensemble des années :", stock)
        print("Écart entre chaque case :", [combination[i] - combination[i - 1] for i in range(1, len(combination))])
        print()


if __name__ == "__main__":
    main()
