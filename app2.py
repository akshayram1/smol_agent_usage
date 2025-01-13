import streamlit as st
from smolagents.agents import ToolCallingAgent
from smolagents import tool, LiteLLMModel
from typing import Optional
import cv2
import pytesseract
from PIL import Image
import io

# Define the LiteLLMModel
model = LiteLLMModel(model_id="gpt-4o")

@tool
def extract_components(image_data: bytes) -> str:
    """
    Extract components from a web design image.

    Args:
        image_data: The image data in bytes.

    Returns:
        A string describing the components found in the image.
    """
    image = Image.open(io.BytesIO(image_data))
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    components = pytesseract.image_to_string(gray)
    return components

@tool
def generate_code(components: str) -> str:
    """
    Generate code for the given components. 

    Args:
        components: A string describing the components.

    Returns:
        The generated code for the components.
    """
    # This is a placeholder implementation. You can replace it with actual code generation logic.
    return f"Generated code for components: {components}"

# Define the ToolCallingAgent
agent = ToolCallingAgent(tools=[extract_components, generate_code], model=model)

# Streamlit app title
st.title("Web Design Component Extractor")

# File uploader for the web design image
uploaded_file = st.file_uploader("Upload a web design image", type=["png", "jpg", "jpeg"])

# Button to run the agent
if st.button("Extract and Generate Code"):
    if uploaded_file is not None:
        image_data = uploaded_file.read()
        components = agent.run("extract_components", image_data=image_data)
        code = agent.run("generate_code", components=components)
        st.write("Extracted Components:", components)
        st.write("Generated Code:", code)
    else:
        st.write("Please upload an image.")