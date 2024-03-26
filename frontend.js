function performSearch() {
    const query = document.getElementById('searchQuery').value;
    const model = document.getElementById('generativeModel').value;

    fetch(`/search?query=${encodeURIComponent(query)}&model=${encodeURIComponent(model)}`)
        .then(response => response.json())
        .then(data => {
            const resultsElement = document.getElementById('searchResults');
            resultsElement.innerHTML = ''; // Clear previous results
            data.results.forEach(result => {
                const div = document.createElement('div');
                div.textContent = result.title; // Adjust according to how you want to display results
                resultsElement.appendChild(div);
            });
        })
        .catch(error => console.error('Error:', error));
}
