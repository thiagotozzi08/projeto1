from utils import load_template, get_notes, add_note

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=nota['title'], details=nota['content'])
        for nota in get_notes()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    add_note(titulo, detalhes)