import os

def generate_invitations(template, attendees):
    # Vérification des erreurs spécifiques et des types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Error: Attendees must be a list.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for person in attendees:
        if not isinstance(person, dict):
            print("Error: Attendees must be a list of dictionaries.")
            return

    # Génération des invitations et création des fichiers
    for i, person in enumerate(attendees, start=1):
    # i : numéro de la personne dans la liste, commence à 1
    # person : dictionnaire contenant les infos de l'invité courant

        invitation_text = template
    # On crée une copie du template pour ne pas modifier l'original
    # invitation_text sera personnalisé pour cette personne

        keys = ["name", "event_title", "event_date", "event_location"]
    # Liste des clés que l'on doit remplacer dans le template

        for key in keys:
            value = person.get(key)
    # On récupère la valeur associée à la clé dans le dictionnaire
    # Si la clé n'existe pas, get() renverra None

            if not value:
                value = "N/A"
            invitation_text = invitation_text.replace("{" + key + "}", value)
# On remplace dans le texte le placeholder {clé} par la valeur correspondante

        filename = f"output_{i}.txt"
    # On crée le nom du fichier avec le numéro de l'invité

        if os.path.exists(filename):
            print(f"Warning: {filename} already exists and will be overwritten.")

        try:
            with open(filename, "w") as f:
                f.write(invitation_text)

        except Exception as e:
            print(f"Error writing to {filename}: {e}")
    # On ouvre le fichier en mode écriture (écrase s'il existe déjà),
    # on écrit le texte personnalisé dedans,
    # Le fichier se ferme automatiquement grâce au 'with'
