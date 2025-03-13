from flask import Flask, request, send_from_directory, render_template, jsonify
import os

app = Flask(__name__)

# Carpeta donde se guardarán los backups
BACKUP_FOLDER = "Archivos/"
if not os.path.exists(BACKUP_FOLDER):
    os.makedirs(BACKUP_FOLDER)

# Extensiones permitidas
ALLOWED_EXTENSIONS = {'backup', 'rsc'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No se envió ningún archivo", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No se seleccionó ningún archivo", 400

    if not allowed_file(file.filename):
        return "Tipo de archivo no permitido. Solo se aceptan archivos .backup y .rsc de Mikrotik", 400

    filepath = os.path.join(BACKUP_FOLDER, file.filename)
    file.save(filepath)
    return jsonify({'message': f'Backup recibido: {file.filename}'})

@app.route('/list_files')
def list_files():
    files = []
    for filename in os.listdir(BACKUP_FOLDER):
        if allowed_file(filename):  # Solo listar archivos permitidos
            file_path = os.path.join(BACKUP_FOLDER, filename)
            if os.path.isfile(file_path):
                files.append({
                    'name': filename,
                    'size': os.path.getsize(file_path)
                })
    return jsonify(files)

@app.route('/download/<filename>')
def download_file(filename):
    if not allowed_file(filename):
        return "Archivo no permitido", 400
    return send_from_directory(BACKUP_FOLDER, filename, as_attachment=True)

@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    if not allowed_file(filename):
        return "Archivo no permitido", 400
    try:
        file_path = os.path.join(BACKUP_FOLDER, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            return jsonify({'message': 'Archivo eliminado exitosamente'})
        return "Archivo no encontrado", 404
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5080, debug=True)
