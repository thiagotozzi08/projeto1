from utils import load_template, get_notes, add_note, delete_note, get_note, update_note

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=nota['title'], details=nota['content'], id=nota['id'])
        for nota in get_notes()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    add_note(titulo, detalhes)

def delete(id):
    delete_note(id)

def edit(id):
    nota = get_note(id)
    return load_template('update.html').format(id=nota.id, title=nota.title, content=nota.content)

def submit(titulo, detalhes):
    add_note(titulo, detalhes)

def update(id, titulo, detalhes):
    update_note(id, titulo, detalhes)