import streamlit as st
import requests

# Set up the Streamlit interface
st.title('AI Model Interaction')
user_input = st.text_input("Enter your question or prompt:")

# Function to send requests to the AI model
def get_model_response(prompt):
    # Define the endpoint URL
    url = "http://localhost:1234/v1/chat/completions"
    
    # Define the data to be sent in the POST request
    data = {
        "model": "local-model",  # Update with your model name
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 150
    }
    
    # Send the POST request and get the response
    response = requests.post(url, json=data)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the JSON response if successful
    else:
        return {"error": "Could not retrieve response from the model"}  # Return an error message if not successful

# Display the response from the AI model
if user_input:
    response = get_model_response(user_input)
    if 'error' in response:
        st.error(response['error'])
    else:
        st.write("Model response:", response['choices'][0]['message']['content'])  # Adjust based on your model's response structure
