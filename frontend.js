function performSearch() {
    const query = document.getElementById('searchQuery').value;
    const generativeModel = document.querySelector('input[name="generativeModel"]:checked').value;

    console.log('Selected generative model:', generativeModel); // Log the selected model

    fetch(`/search?query=${encodeURIComponent(query)}&generativeModel=${encodeURIComponent(generativeModel)}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const resultsElement = document.getElementById('searchResults');
            resultsElement.innerHTML = ''; // Clear previous results

            data.results.forEach(result => {
                const div = document.createElement('div');
                div.textContent = result.text || 'No text available';
                resultsElement.appendChild(div);
            });
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error performing search');
        });
}
