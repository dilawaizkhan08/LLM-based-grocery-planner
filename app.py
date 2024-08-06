import streamlit as st
from main import create_chat_completion, prepare_prompt

def main():
    st.title("Grocery Planner Chat")

    # Initialize session state
    if 'history' not in st.session_state:
        st.session_state.history = []

    # Function to handle the submit button click
    def handle_submit(user_query):
        # Prepare the prompt with the conversation history
        prompt = prepare_prompt(st.session_state.history, user_query)

        # Get the response from the model
        response = create_chat_completion(prompt)

        # Update the conversation history
        st.session_state.history.append(("user", user_query))
        st.session_state.history.append(("assistant", response))

    # Input field for user query at the bottom
    user_input = st.chat_input("Ask your question:")

    if user_input:
        handle_submit(user_input)

    # Display the conversation history with auto-scrolling
    st.subheader("Conversation History")
    for speaker, message in st.session_state.history:
        if speaker == "user":
            st.markdown(f'<p style="text-align: right;"><span style="background-color: grey; padding: 10px; border-radius: 10px; margin: 5px;">{message}</span></p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p style="text-align: left;"><span style="background-color: none; padding: 10px; border-radius: 10px; margin: 5px;">{message}</span></p>', unsafe_allow_html=True)

    # JavaScript code to auto-scroll to the bottom
    st.markdown(
        """
        <script>
        const chatContainer = document.querySelector('.element-container');
        if (chatContainer) {
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
        </script>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
