# Top 2 Similar Phrases with FastAPI
  ## Overview
  This FastAPI application provides an API for comparing phrases in a list and identifying the top 2 closest phrases. The comparison is based on the cosine distance between the encodings of the phrases, calculated using a pre-trained sentence bge embedding model. The application exposes a single endpoint, named top2, which accepts a list of phrases and returns the pair with the smallest cosine distance.
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
   
