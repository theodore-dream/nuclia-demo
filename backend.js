const express = require('express');
const path = require('path');
const FormData = require('form-data');
const fileUpload = require('express-fileupload');

let fetch;
import('node-fetch').then(module => {
    fetch = module.default;
});

const app = express();

// Serve static files (like frontend.js) from the current directory
app.use(express.static(__dirname));

app.use(fileUpload());

// Serve your frontend.html on the root URL
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'frontend.html'));
});


app.post('/upload', async (req, res) => {
    if (!req.files || Object.keys(req.files).length === 0) {
        return res.status(400).send('No files were uploaded.');
    }

    const files = req.files.files; // 'files' corresponds to the name attribute in FormData
    const results = [];

    for (const file of files) {
        const formData = new FormData();
        formData.append('file', file.data, file.name);

        try {
            const response = await fetch('https://aws-us-east-2-1.nuclia.cloud/api/v1/kb/6fd0e260-56f2-4269-ae4a-f944bc8df706/upload', {
                method: 'POST',
                headers: {
                    'X-NUCLIA-SERVICEACCOUNT': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Im51YSJ9.eyJpc3MiOiJodHRwczovL2F3cy11cy1lYXN0LTItMS5udWNsaWEuY2xvdWQvIiwiaWF0IjoxNzEwODk2NDQ0LCJzdWIiOiJiZWE2NWIyZC04NzA2LTQ2MzItYmVmYi03NDc2MDAwMjI1MWEiLCJqdGkiOiI3M2I5ZmJhOC0yMTQwLTRlMTAtODUxOS1iZjliODdhNDk5MTQiLCJleHAiOjI1MzM3MDc2NDgwMCwia2V5IjoiMTVkZWM2ZTgtMjlkNC00OTdhLWE1MDItMGJmOWFjNjc4MjFjIiwiYWxsb3dfa2JfbWFuYWdlbWVudCI6ZmFsc2V9.cPKOpyblK1zVdt5Ati19tJYU93HevVnzqXTI2vK_yaw4GxacbBmIGRmNZd88OJLWFbHpfL1NKwG5AyT2ugZkHRKuSOpge5nopoqre8yyAZtJnPVGEg4BvViOTX-PpLsXeaHhbfs_WcjNpIQEAXWiAzwo_PzcK4Rh9J5UZTmRFxQlzGfHXcH6XEYrmZy-ic69rbmVmqmh-dmGW2jvNdD6wy5GA81-XL96vtgH1AYzgW05iwaFE_FYWuzCJlOIgycxZBe80KJLEdE-CXlpW6d4TQmsAfayj9G-6t9B_vzNIC8TBVstwq6UHB5PSXYo1xxSuEVouUn399MSuMADTkwWhdEujn6x8mC484cqCDFnxgfEEoe9aeEYIUL-bBIilQz2mpQgQVHgx0hPpTbspc0mlKfWOzxj1JSKs8n649NWwccmym8vwriDvZTfONNjJq3MFG9G26clY6utTkPQSugUj_HJ_AoqAUzd6tEOvf0lBt7OoHQRqG13BrZT-TqxdaJem35pFrMC1x8-B11ZpkrquN8ZH07qPScn0nKcrc138f--abIS6XeqlqDw5R-B14SCDPiy76s8ZMHHGL4A99WMYAdzlSQsHqe-sRI0rZUsTWRDySaqc1r_wXj6CWPTHm7OAgZli60m--8dBNIjLHN3G843bNljpRy_dcTq5tNdLd0'
                },
                body: formData
            });
            const result = await response.json();
            results.push(result);
        } catch (error) {
            console.error('Upload error:', error);
            return res.status(500).send('Error uploading file to Nuclia.');
        }
    }

    res.json({ message: 'Files uploaded successfully', results });
});

const port = 3000;
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
