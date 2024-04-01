const express = require('express');
const path = require('path');
const FormData = require('form-data');
const fileUpload = require('express-fileupload');
const { Nuclia } = require('@nuclia/core');

require('localstorage-polyfill');
require('isomorphic-unfetch');

import('node-fetch').then(module => {
    global.fetch = module.default;
});

const app = express();

app.use(express.static(__dirname)); // Serve static files

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

const nuclia = new Nuclia({
    backend: 'https://nuclia.cloud/api',
    zone: 'aws-us-east-2-1',
    knowledgeBox: '6fd0e260-56f2-4269-ae4a-f944bc8df706',
});

app.get('/search', async (req, res) => {
    const { query, generativeModel } = req.query;
    console.log('Search request received:', { query, generativeModel }); // Log the query and model

    try {
        const results = await searchInNuclia(query, generativeModel);
        res.json({ results });
    } catch (error) {
        console.error('Search error:', error);
        res.status(500).send('Error performing search');
    }
});


async function searchInNuclia(query, generativeModel) {
    const apiUrl = `https://aws-us-east-2-1.nuclia.cloud/api/v1/kb/6fd0e260-56f2-4269-ae4a-f944bc8df706/search`;
    const params = new URLSearchParams({
        query: query,
        min_score_bm25: 5.0,
        generative_model: generativeModel, // Pass generativeModel to the API call
        features: 'paragraph',
        page_number: 0,
        page_size: 20,
        debug: true
    });

    console.log('Sending search to Nuclia:', query);
    try {
        const response = await fetch(`${apiUrl}?${params.toString()}`, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'x-ndb-client': 'api'
            }
        });

        if (!response.ok) {
            const errorBody = await response.json();
            console.error('Nuclia API responded with an error:', errorBody);
            throw new Error(`HTTP error! status: ${response.status}, detail: ${JSON.stringify(errorBody)}`);
        }

        const data = await response.json();
        console.log('Received response from Nuclia:', data);

        // Extract paragraph results
        const paragraphResults = data.paragraphs && data.paragraphs.results ? data.paragraphs.results : [];
        console.log('Extracted paragraph results:', paragraphResults);

        return paragraphResults; // Send these paragraph results to the frontend
    } catch (error) {
        console.error('Error searching in Nuclia:', error);
        throw error;
    }
}



const port = 3000;
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
