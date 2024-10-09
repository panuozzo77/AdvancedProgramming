import os
import re

# Funzione per estrarre i titoli da un file markdown
def extract_headings(file_content):
    headings = []
    for line in file_content.splitlines():
        # Trova le righe che iniziano con # (livelli di headings)
        match = re.match(r'^(#{1,6})\s+(.*)', line)
        if match:
            level = len(match.group(1))  # Determina il livello dell'heading
            title = match.group(2).strip()  # Ottiene il titolo
            headings.append((level, title))
    return headings

# Funzione per generare un link cliccabile
def generate_link(filename, title):
    anchor = title.lower().replace(' ', '-').replace('.', '').replace('\'', '')  # Crea l'ancora
    filename = filename.replace(' ', '%20')  # Sostituisce gli spazi con %20 nel nome del file
    return f"- [{title}]({filename}#{anchor})"

# Funzione principale per creare l'indice
def create_index(root_folder):
    index_content = "# Index\n\n"
    # Cammina attraverso tutti i file e sottocartelle
    for subdir, _, files in os.walk(root_folder):
        for file in sorted(files):  # Ordina i file in ordine lessicografico
            if file.endswith(".md") and file != 'index.md':  # Evita di includere index.md
                filepath = os.path.join(subdir, file)
                # Aggiungi 'classNotes' al percorso relativo
                relative_path = os.path.relpath(filepath, os.path.dirname(root_folder))
                relative_path = os.path.join('classNotes', os.path.relpath(filepath, root_folder))

                # Leggi il contenuto del file markdown
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Estrai i titoli
                headings = extract_headings(content)

                # Aggiungi i titoli all'indice
                if headings:
                    index_content += f"## {relative_path}\n\n"
                    for level, title in headings:
                        link = generate_link(relative_path, title)
                        indent = '  ' * (level - 1)  # Gestisce i livelli di indentazione
                        index_content += f"{indent}{link}\n"
                    index_content += "\n"

    # Scrivi l'indice nel file index.md nella root del progetto
    with open(os.path.join(os.path.dirname(root_folder), 'index.md'), 'w', encoding='utf-8') as index_file:
        index_file.write(index_content)

# Imposta automaticamente la root folder e specifica la cartella 'classNotes'
project_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'classNotes')

# Crea l'indice
create_index(project_folder)
