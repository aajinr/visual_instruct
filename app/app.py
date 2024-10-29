import streamlit as st
from PIL import Image
from llama_predict import predict  # Import the predict function

# Set up the title and description of the Streamlit app
st.title("Image Description Generator")
st.write("Upload an image in JPEG or PNG format, and the model will provide a detailed description of the content.")

# Upload an image file
uploaded_file = st.file_uploader("Choose an image...", type=["jpeg", "jpg", "png"])

# If an image is uploaded, process it
if uploaded_file is not None:
    # Open the uploaded image file
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Generate a description for the uploaded image
    with st.spinner("Generating description..."):
        description = predict(image)
    
    # Display the generated description
    st.subheader("Image Description")
    st.write(description)
