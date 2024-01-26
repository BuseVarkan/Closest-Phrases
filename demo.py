import requests

api_endpoint = "http://localhost:8000/top2"

test_phrases = []

# Test case 1: Empty list
phrases = []
test_phrases.append(phrases)

# Test case 2: List with 1 element
phrases = ["Buse"]
test_phrases.append(phrases)

# Test case 3: List with 2 elements
phrases = ["Buse", "Varkan"]
test_phrases.append(phrases)

# Test case 4: Phrase is empty
phrases = ["computer", ""]
test_phrases.append(phrases)

# Test case 5: Phrase with more than 1000 characters
phrases = ["a" * 1001, "b"]
test_phrases.append(phrases)

# Test case 6: Valid list
phrases = ["1111", "2222", "abcdef", "23456"]
test_phrases.append(phrases)

# Test case 7: Valid list
phrases = ["Buse", "Varkan", "apple", "orange", "I love playing video games","Deep learning is a subset of machine learning","Machine learning is a subset of artificial intelligence"]
test_phrases.append(phrases)

# Test case 8: Valid list
phrases = ["xyzxyz", "xyzxyz", "xyzxyz"]
test_phrases.append(phrases)

# Get test case number from user
test_case_number = int(input("Enter test case number (1-8): "))

# Send request to API
response = requests.post(api_endpoint, json=test_phrases[test_case_number - 1])

if response.status_code == 200:
    print("Top 2 closest phrases:", response.json())

else:
    print("Status Code:",response.status_code)
    print(response.json().get("detail"))
