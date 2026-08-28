from flask import Flask, render_template_string, request, redirect
import views


app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')
    detalhes = request.form.get('detalhes')
    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/delete/<id>')
def delete_note_route(id):
    views.delete(id)
    return redirect('/')

@app.route('/update/<id>')
def update_note_route(id):
    return render_template_string(views.edit(id))

@app.route('/update', methods=['POST'])
def update_form():
    id = request.form.get('id')
    titulo = request.form.get('titulo')
    detalhes = request.form.get('detalhes')
    views.update(id, titulo, detalhes)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)