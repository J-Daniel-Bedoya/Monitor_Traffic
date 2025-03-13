document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('uploadForm');
    const fileInput = document.getElementById('fileInput');
    const fileList = document.getElementById('fileList');

    // Cargar la lista de archivos al iniciar
    loadFileList();

    uploadForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = new FormData();
        formData.append('file', fileInput.files[0]);

        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                alert('Archivo subido exitosamente');
                fileInput.value = '';
                loadFileList(); // Recargar la lista
            } else {
                alert('Error al subir el archivo');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error al subir el archivo');
        }
    });

    async function loadFileList() {
        try {
            const response = await fetch('/list_files');
            const files = await response.json();
            
            fileList.innerHTML = '';
            files.forEach(file => {
                const item = document.createElement('a');
                item.className = 'list-group-item list-group-item-action d-flex justify-content-between align-items-center';
                item.href = `/download/${file.name}`;
                
                const nameSpan = document.createElement('span');
                nameSpan.textContent = file.name;
                item.appendChild(nameSpan);

                const deleteBtn = document.createElement('button');
                deleteBtn.className = 'btn btn-danger btn-sm';
                deleteBtn.textContent = 'Eliminar';
                deleteBtn.onclick = async (e) => {
                    e.preventDefault();
                    if (confirm('¿Estás seguro de eliminar este archivo?')) {
                        await deleteFile(file.name);
                    }
                };
                item.appendChild(deleteBtn);
                
                fileList.appendChild(item);
            });
        } catch (error) {
            console.error('Error:', error);
            fileList.innerHTML = '<div class="alert alert-danger">Error al cargar la lista de archivos</div>';
        }
    }

    async function deleteFile(filename) {
        try {
            const response = await fetch(`/delete/${filename}`, {
                method: 'DELETE'
            });

            if (response.ok) {
                loadFileList();
            } else {
                alert('Error al eliminar el archivo');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error al eliminar el archivo');
        }
    }
});
