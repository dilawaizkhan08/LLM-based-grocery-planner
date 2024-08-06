from main import *

def main():
    print("Welcome to the software engineering chat! Type 'exit' to end the chat.")
    history = []

    while True:
        # Get the user input
        user_query = input("Ask your question: ")

        # Check if the user wants to exit
        if user_query.lower() == 'exit':
            print("Goodbye!")
            break

        # Prepare the prompt with the conversation history
        prompt = prepare_prompt(history, user_query)

        # Get the response from the model
        response = create_chat_completion(prompt)

        # Print the response
        print(response)

        # Update the conversation history
        history.append(f"User: {user_query}")
        history.append(f"Assistant: {response}")

if __name__ == "__main__":
    main()
