# AI Chatbot with LangChain and OllamaLLM

## Description
This project is an AI chatbot that can run locally on your machine using LangChain and Ollama LLM models to generate responses based on user input. The chatbot maintains a conversation history to provide context for its responses.

## Installation
1. Install Ollama here https://ollama.com/download
2. Install Llama-3 8B from the Ollama library.
    ```sh
   ollama pull llama3
    ```
   
4. Clone the repository

5. Install the required dependencies:
    ```sh
    pip install langchain langchain-ollama ollama
    ```

## Usage
To start the chatbot, run the `main.py` file:
```sh
python main.py
