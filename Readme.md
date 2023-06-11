

# Human Data Attribute Extraction App

This application is designed to extract specific data attributes related to humans from one or multiple DOCX documents. It utilizes the power of ChatGPT, an AI language model, to analyze the documents and identify relevant information. The app also ensures privacy by replacing the actual user information with masked text or Ethereum wallet IDs.

## Requirments
  1. **Python 3.10 or Latest** are required
  2. Please insitall **requirment_1.txt** 
  ```
  pip install requirments_1.txt
  ```
  3. An Healthy Brain :) 

## Instructions

Before running the application, please make the following changes:

    1. Open the utils/const.py file in a text editor.
    2. Locate the line INPUT_PATH = 'test/' and modify the value to the path where your DOCX files are located. This path will be the input directory from which the application will read the documents.
    3. Find the line API_KEY = 'XXXXXXX' in the same file (utils/const.py) and replace 'XXXXXXX' with your actual ChatGPT API key. This key is required to connect to the ChatGPT service and perform language processing tasks.

It is essential to upload the DOCX files from the specified INPUT_PATH directory because the application uses Streamlit, a web application framework. Streamlit requires the files to be available in the same path specified during configuration.

## Running the Application

To run the application and start the human data attribute extraction process, execute the following command in your terminal:

```
streamlit run main.py

```

This command will launch the application, and you can interact with it through your web browser.

## Demo
Please watch the demo.webm 

## Credits

This application was developed by Mohammad Ali Abbas at waspak.co for Holland (A Fiverr Client).