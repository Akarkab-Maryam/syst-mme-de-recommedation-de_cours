import csv
import json
import random

def generate_fake_data(num_rows=2000):
    data = []
    interests_options = ["Python", "IA", "Data Analysis", "Machine Learning", "Web Development", "SQL", "JavaScript", "CSS", "HTML", "Cloud Computing", "Big Data", "Computer Vision", "NLP", "React", "Angular", "Node.js"]
    competences_options = ["Excel", "Python", "SQL", "JavaScript", "HTML", "CSS", "R", "Tableau", "Power BI", "Git", "Docker", "AWS", "Azure", "Google Cloud", "Communication", "Gestion de projet", "Analyse de données", "Résolution de problèmes"]
    niveau_options = ["Débutant", "Intermédiaire", "Avancé"]
    domaine_options = ["Informatique", "Data Science", "Développement Web", "Gestion de Projet", "Marketing Digital"]

    for i in range(num_rows):
        nom = f"Personne {i+1}"
        num_interests = random.randint(1, 3)
        interests = random.sample(interests_options, num_interests)
        niveau = random.choice(niveau_options)
        num_competences = random.randint(2, 5)
        competences = random.sample(competences_options, num_competences)
        domaine = random.choice(domaine_options)

        data.append({
            "nom": nom,
            "intérêts": json.dumps(interests),
            "niveau": niveau,
            "competences": json.dumps(competences),
            "domaine": domaine
        })
    return data

def write_to_csv(data, filename="data.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["nom", "intérêts", "niveau", "competences", "domaine"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    fake_data = generate_fake_data()
    write_to_csv(fake_data)
    print("Le fichier CSV 'data.csv' a été généré avec 2000 lignes.")