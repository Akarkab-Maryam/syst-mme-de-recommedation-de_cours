import pandas as pd
import json
import ast

# Modifier selon ton fichier
chemin_csv = r'C:\Users\maryam\Contacts\Desktop\Retour terrain\data.csv'
nombre_etudiants = 60  # Ajuste ce nombre si tu as plus d'étudiants

# Charger le fichier CSV
try:
    df = pd.read_csv(chemin_csv)
except FileNotFoundError:
    print("Erreur: Le fichier data.csv n'a pas été trouvé.")
    exit()

# Lecture des étudiants
etudiants_df = df.iloc[:nombre_etudiants]

etudiants = []
for index, row in etudiants_df.iterrows():
    def charger_colonne(col):
        try:
            return json.loads(row[col])
        except:
            try:
                val = ast.literal_eval(row[col])
                return val if isinstance(val, list) else []
            except:
                return []

    interets = charger_colonne('intérêts')
    competences = charger_colonne('competences')

    etudiants.append({
        "id": index + 1,
        "nom": row['nom'],
        "interets": interets,
        "competences": competences,
        "niveau": row['niveau']
    })

# --- Liste de cours (à adapter avec tes vrais cours) ---
cours = [
    {
        "titre": "Introduction à Python",
        "sujets": ["Python", "Programmation", "Algorithmes"],
        "niveau": "Débutant"
    },
    {
        "titre": "Analyse de Données avec Pandas",
        "sujets": ["Pandas", "Analyse de Données", "Python"],
        "niveau": "Intermédiaire"
    },
    {
        "titre": "Machine Learning Fondamental",
        "sujets": ["Machine Learning", "IA", "Algorithmes", "Statistiques"],
        "niveau": "Avancé"
    },
    {
        "titre": "Cybersécurité : Bases",
        "sujets": ["Cybersécurité", "Réseaux", "Sécurité"],
        "niveau": "Intermédiaire"
    },
    {
        "titre": "Big Data avec Spark",
        "sujets": ["Big Data", "Spark", "Analyse Distribuée"],
        "niveau": "Avancé"
    },
    # Ajoute plus de cours ici...
]

# Dictionnaire rapide d'accès
etudiants_dict = {e['id']: e for e in etudiants}

# Fonction de recommandation améliorée
def recommander_cours(etudiant_id):
    etudiant = etudiants_dict.get(etudiant_id)
    if not etudiant:
        return {"message": "Étudiant non trouvé"}

    interets = set(etudiant.get("interets", []))
    competences = set(etudiant.get("competences", []))
    niveau = etudiant["niveau"]

    cours_potentiels = []

    for c in cours:
        if c.get("niveau") != niveau:
            continue  # On filtre strictement sur le niveau

        score = 0
        sujets = set(c.get("sujets", []))

        # Pondération des intérêts et compétences
        score += 3 * len(interets.intersection(sujets))
        score += 2 * len(competences.intersection(sujets))
        score += 5  # Bonus de niveau (optionnel ici car déjà filtré)

        if score > 0:
            cours_potentiels.append({
                "titre": c.get("titre", "Cours sans titre"),
                "score": score
            })

    cours_potentiels.sort(key=lambda x: x["score"], reverse=True)

    return {"recommandations": [c["titre"] for c in cours_potentiels]}

# Exemple : recommander pour tous les étudiants
if __name__ == "__main__":
    for etudiant in etudiants:
        resultats = recommander_cours(etudiant['id'])
        print(f"\nÉtudiant {etudiant['id']} - {etudiant['nom']}")
        print(json.dumps(resultats, indent=4, ensure_ascii=False))
