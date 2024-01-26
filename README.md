# Top 2 Similar Phrases with FastAPI
  ## Overview
  This FastAPI application provides an API for comparing phrases in a list and identifying the top 2 closest phrases. The comparison is based on the cosine distance between the encodings of the phrases, calculated using a pre-trained bge embedding model. The application exposes a single endpoint, named top2, which accepts a list of phrases and returns the pair with the smallest cosine distance.
 ## Requirements
 Make sure you have the required libraries installed. You can install them using the provided `requirements.txt` file.
 
 ``` 
 pip3 install -r requirements.txt
```
 ## Usage
 1. Run the FastAPI server using the following command:
 ```
python3 -m uvicorn api:app --reload
 ```

2. Run a separate terminal, execute the demo script (demo.py) to send requests to the running API and display the results. The script provides various test cases for showcasing the functionality of the API.
 ```
python3 demo.py
 ```
   
3. Enter the corresponding test case number as input when prompted by the script. You will see the following promt:
   >  Enter test case number (1-8):
4. You will see the top 2 similar phrases in the input list.
   > Top 2 closest phrases: ['Deep learning is a subset of machine learning', 'Machine learning is a subset of artificial intelligence']
5. If there is an error in the input, you will see the error message corresponding to your input.
   > Status Code: 400
   > Error: At least two phrases required for comparison.
   
## Functionality
### 1. API Endpoint: /top2
The API provides a single endpoint, /top2, which is designed for comparing phrases and identifying the top 2 closest phrases within a given list. The process involves the following steps:

### 2. Input Phrases:
  The user submits a list of phrases to the /top2 endpoint.
  The list should contain at least two phrases for meaningful comparison.
  It should only contain non-empty strings.
  Moreover, the size of phrases should be less than 1000.
  
### 3. Embeddings Calculation:
The application utilizes a pre-trained bge embedding model to calculate numerical embeddings for each phrase in the list.
Sentence embeddings capture the semantic meaning of the phrases.
### 4. Cosine Distance Calculation:
The cosine distance is calculated between the embeddings of all pairs of phrases in the list.
Cosine distance is a metric that measures the cosine of the angle between two vectors, providing a measure of similarity.
### 5. Identification of Top 2 Closest Phrases:
The pair of phrases with the smallest cosine distance is identified as the top closest pair.
### 6. Response:
The API responds with a tuple containing the top 2 closest phrases identified during the comparison.
    
