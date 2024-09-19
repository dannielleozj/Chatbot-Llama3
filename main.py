from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

#embed the context and question into the prompt
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)

#chain model and template together
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to the AI chatbot! Type 'exit' to quit.")

    #collect user input
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        result = chain.invoke({"context": context, "question": user_input})
        print("Bot:", result)

        #store and pass context back into Bot
        context += f"\nUser:{user_input}\nAI:{result}"

if __name__ == "__main__":
    handle_conversation()


