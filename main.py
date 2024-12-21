# Definition der Meldung, die angezeigt wird, wenn "H" gedrückt wird
message = """
Sehr geehrte Damen und Herren,

ich heiße Mario Sipicki und hiermit möchte ich mich gerne um eine Ausbildung zum Fachinformatiker für Anwendungsentwicklung bewerben.
Meine Projekte, die ich während der Quarantäne 2020 in Python (PyCharm) erstellt / programmiert habe, finden Sie hier auf GitHub.

Ich habe auch alle Projekte mit Windows Powershell mit den folgenden Schritten auf Github hochgeladen:
1. cd .. und / oder cd " " -> cd = change directory (zur Erklärung)
2. git init .
3. gh repo create
4. git add *; git commit -m "init"; git push --set-upstream origin master

Vielen Dank im Voraus!

Mit freundlichen Grüßen
Mario Sipicki
"""

# Benutzer auffordern, "H" zu drücken
print("Press 'H'  (für Hallo) and then Enter to display the message...")

# Benutzereingaben
user_input = input("Press 'H' (für Hallo) to show the message: ")

# Überprüfen Sie, ob die Eingabe "H" oder "h" ist.
if user_input.lower() == 'h':
    print(message)
else:
    print("You did not press 'H'.")
