from fastapi import FastAPI, HTTPException
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine

# Initialize the FastAPI app
app = FastAPI()

# Initialize the sentence embedding model
model = SentenceTransformer('BAAI/bge-large-zh-v1.5')

def check_phrases(phrases: list[str]) -> HTTPException:
    """
    Check if the input phrases are valid.

    Args:
        phrases (list[str]): List of input phrases.

    Returns:
        HTTPException: Exception if the input phrases are invalid.
    """
    if not isinstance(phrases, list):
        raise HTTPException(status_code=400, detail="Error: Not a list.")
    
    if len(phrases) == 0:
        raise HTTPException(status_code=400, detail="Error: No phrases provided.")
    
    if len(phrases) < 2:
        raise HTTPException(status_code=400, detail="Error: At least two phrases required for comparison.")
    
    for phrase in phrases:
        if not isinstance(phrase, str):
            raise HTTPException(status_code=400, detail="Error: Phrase is not a string.")
        if len(phrase) == 0:
            raise HTTPException(status_code=400, detail="Error: Phrase is empty.")
        if len(phrase) > 1000:
            raise HTTPException(status_code=400, detail="Error: Phrase is longer than 1000 characters.")
        

def calculate_embeddings(phrases: list[str]) -> list[list[float]]:
    """
    Calculate the embeddings for a list of phrases using the pre-trained sentence embedding model.

    Args:
        phrases (list[str]): List of input phrases.

    Returns:
        list[list[float]]: List of embeddings for the input phrases.
    """
    embeddings_list = [model.encode(phrase) for phrase in phrases]
    return embeddings_list

def calculate_cosine_distance(embedding1: list[float], embedding2: list[float])-> float:
    """
    Calculate the cosine distance between two embeddings.

    Args:
        embedding1 (list[float]): Embedding of the first phrase.
        embedding2 (list[float]): Embedding of the second phrase.

    Returns:
        float: Cosine distance between the two embeddings.
    """
    return cosine(embedding1, embedding2)

def find_top2_closest(phrases: list[str]) -> tuple[str, str]:
    """
    Find the top 2 closest phrases from a list of phrases.

    Args:
        phrases (list[str]): List of input phrases.

    Returns:
        Tuple(str, str): Tuple of the top 2 closest phrases.
    """
    embeddings = calculate_embeddings(phrases)
    num_phrases = len(phrases)
    
    if num_phrases == 2:
        return (phrases)

    min_distance = float('inf')
    closest_pair = ()

    for i in range(num_phrases):
        for j in range(i + 1, num_phrases):
            distance = calculate_cosine_distance(embeddings[i], embeddings[j])

            if distance < min_distance:
                min_distance = distance
                closest_pair = (phrases[i], phrases[j])

    return closest_pair


# Define the API post method for the top2 endpoint
@app.post("/top2")
async def top2(phrases: list[str])-> tuple[str, str]:
    """
    Check if the input phrases are valid.
    Find the top 2 closest phrases from a list of phrases.
    
    Args:
        phrases (list[str]): List of input phrases.

    Returns:
        tuple[str, str]: The top 2 closest phrases.
    """
    try:
        check_phrases(phrases)
    except HTTPException as e:
        raise e
    else:    
        return find_top2_closest(phrases)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)