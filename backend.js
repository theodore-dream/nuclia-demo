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
    knowledgeBox: '6fd0e260-56f2-4269-ae4a-f944bc8df706'
});

app.get('/search', async (req, res) => {
    const { query, model } = req.query;
    console.log('Search request received:', { query, model }); // Log request details
    try {
        const results = await searchInNuclia(query, model);
        res.json({ results });
    } catch (error) {
        console.error('Search error:', error);
        res.status(500).send('Error performing search');
    }
});

async function searchInNuclia(query, model) {
    console.log('Sending search to Nuclia:', { query, model }); // Log what is being sent to the API
    try {
        const response = await nuclia.knowledgeBox.search(query, [model]);
        console.log('Received response from Nuclia:', response); // Log full response
        return response.results; // Assuming 'results' is part of the response object
    } catch (error) {
        console.error('Error searching in Nuclia:', error);
        throw error;
    }
}

const port = 3000;
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
