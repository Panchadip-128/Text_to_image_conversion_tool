import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

# Load the Stable Diffusion model
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id)

# Move the model to GPU if available, otherwise use CPU
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Streamlit app layout
st.title("Text-to-Image Generation using Stable Diffusion")

# Text input for prompt
prompt = st.text_input("Enter a prompt to generate an image:", value="A futuristic city skyline at sunset")

# Button to trigger image generation
if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        # Generate image based on prompt
        image = pipe(prompt).images[0]
        
        # Display the image
        st.image(image, caption="Generated Image", use_column_width=True)

        # Option to save the generated image
        output_path = "generated_image.png"
        image.save(output_path)
        st.success(f"Image saved as {output_path}")

