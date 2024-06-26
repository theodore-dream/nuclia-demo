# Nuclia demo

### Nuclia reference architecture

<img width="740" alt="Screenshot 2024-04-04 at 12 42 50 AM" src="https://github.com/theodore-dream/nuclia-demo/assets/20304946/38be491a-7ec8-4fd6-8ad9-3ecc5611d72b">

### Overview

This is a demo of Nuclia capabilities. 

The python code allows for managemnent of data in Nuclia. 
 - This allows you to upload data to your Nuclia cloud knowledge box specifying a file path or by specifying a URL
 - You can also check on the processing status of your resources in your knowledge box as well as delete resources

The nodejs javascript backend and frontend code allows for a sample website demo of frontend and backend capabilities
 - The frontend presents a search bar that can be used to search for data that is stored in the Nuclia knowledge box.
 - You can also select the LLM generative model to perform the search

### File Structure

This is a set of files that are in 2 groupings
 - one of the set of files are python utility scripts
 - the other set of files compromise a node.js app with frontend and backend that you can deploy to see an example of the Nuclia search functionality. You can also change the generative model. 

 ### Setup Instructions

 Note that you will need to make some changes to make this work for you
  - For the python utility scripts:
    - You will need to change the cloud URL to point to your own cloud region and knowledge box and API key
    - You will need to alter the file path for the "upload_web" script to upload from your own directory 
  - For the nodejs web application:
    - You do not need to make any changes if you are OK with using my knowledge box, this primarily contains different wikipedia articles about AI at this time, ensure you do search queries about AI to properly test it

### Execution Instructions

 - Python scripts: Once you have setup your python scripts by properly setting the variables, you can run with python3 in terminal
 - Nodejs scripts: You need to run "node backend.js" to init the backend server, and then you can connect from http://localhost:3000/ to interact with frontend and perform searches on AI topics. 

 ### Python scripts:

  - knowledge_box_delete.py: utility script to iterate through all resources in knowledge box and delete them all 
  - knowledge_box_list_resources.py: utility script to list all resources in a knowledge box and show processing status 
  - knowledge_box_summarize.py: utility script to iterate through all resources in a knowledge box and summarize them
  - knowledge_box_upload_file.py: utility script to upload a file from a specified path, such as PDFs
  - knowledge_box_upload_web.py: utility script to point a URL to Nuclia cloud and then trigger Nuclia to ingest the data at that URL
  - test_connect.py: utility script for troubleshooting connectivity as a unit test 

### Nodejs scripts:
 - backend.js - backend of nodejs application 
 - frontend.js - scripts for middleware
 - index.html - frontend
