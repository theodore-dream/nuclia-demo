async function performSearch() {
    const query = document.getElementById('searchQuery').value;
    const response = await fetch('http://127.0.0.1:5000/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: query })
    });

    const data = await response.json();
    document.getElementById('results').innerText = JSON.stringify(data, null, 2);
}
