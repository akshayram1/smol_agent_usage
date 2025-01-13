import streamlit as st
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

# Define the agent
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

# Streamlit app title
st.title("SmolAgents Usage Streamlit App")

# Input text box for user query
user_query = st.text_input("Enter your query:")

# Button to run the agent
if st.button("Run Agent"):
    if user_query:
        result = agent.run(user_query)
        st.write("Result:", result)
    else:
        st.write("Please enter a query.")