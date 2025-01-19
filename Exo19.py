def main():
    # Initialiser un ensemble vide pour les mots uniques
    unique_words = set()
    total_words = 0

    # Demander à l'utilisateur de saisir des mots
    print("Entrez des mots (un mot à la fois). Si un mot est dupliqué, le programme s'arrêtera et affichera le nombre de mots uniques.")
    
    while True:
        # Demander à l'utilisateur d'entrer un mot
        word = input("Entrez un mot: ").strip()  # Enlever les espaces au début et à la fin

        # Convertir le mot en minuscule pour rendre l'entrée insensible à la casse
        word_lower = word.lower()

        # Compter tous les mots, y compris les doublons
        total_words += 1

        # Vérifier si le mot est déjà présent dans l'ensemble des mots uniques
        if word_lower in unique_words:
            print(f"Le mot '{word}' est dupliqué.")
            print(f"Nombre total de mots : {total_words}")
            print(f"Nombre de mots uniques : {len(unique_words)}")
            print("Mots uniques (triés par ordre alphabétique) :")
            print(sorted(unique_words))  # Afficher les mots uniques triés par ordre alphabétique
            break
        else:
            # Ajouter le mot à l'ensemble des mots uniques
            unique_words.add(word_lower)

    # Demander si l'utilisateur souhaite enregistrer les mots uniques dans un fichier
    save_to_file = input("Souhaitez-vous enregistrer les mots uniques dans un fichier ? (oui/non): ").strip().lower()
    if save_to_file == 'oui':
        with open("unique_words.txt", "w") as file:
            for word in sorted(unique_words):
                file.write(word + '\n')
        print("Les mots uniques ont été enregistrés dans 'unique_words.txt'.")

if __name__ == "__main__":
    main()
