function uploadFiles() {
    const files = document.getElementById('pdfFile').files;
    const formData = new FormData();
    for (const file of files) {
        formData.append('files', file);
    }
    fetch('/upload', { method: 'POST', body: formData })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
}
