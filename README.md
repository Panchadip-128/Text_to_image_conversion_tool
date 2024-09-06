🖼️ Text-to-Image Generation with Stable Diffusion:
----------------------------------------------------
This project demonstrates how to generate images from text prompts using the Stable Diffusion model in a web interface built with Streamlit. The model takes user inputs in the form of text descriptions (prompts) and generates corresponding images using a pre-trained deep learning model.

📝 Features:
--------------------
Text-to-Image Generation: Converts a user-provided text prompt into an image.
Stable Diffusion: Utilizes the StableDiffusionPipeline from Hugging Face's diffusers library.
CUDA/CPU Support: Automatically detects if CUDA (GPU) is available and uses it for faster inference; otherwise, it defaults to CPU.
User-friendly Interface: Built with Streamlit to allow users to input prompts and download generated images directly from the web interface.

🛠️ Requirements:
------------------
Before running the project, ensure that you have the following installed:

Python 3.8+
pip (Python package installer)

📦 Installation:
-----------------
Clone the repository:

git clone https://github.com/your-username/text-to-image-generation.git
cd text-to-image-generation

Install dependencies:
-----------------------

You can install the required dependencies using the provided requirements.txt file:

pip install -r requirements.txt
The dependencies include:

torch: PyTorch for deep learning.
diffusers: Provides access to Stable Diffusion models.
transformers: Hugging Face’s transformer models.
accelerate: Optimizes model training and inference performance.
streamlit: For the web app interface.
Pillow: Image processing library for saving generated images.

🚀 Running the App:
---------------------------
After installing the dependencies, you can start the Streamlit app by running the following command:

streamlit run app.py
This will launch a web interface where you can enter text prompts and generate images based on the provided text.

Example Prompts:
"A futuristic city skyline at sunset"
"A beautiful landscape from mountains during sunrise"
"An astronaut floating in space, looking at Earth"

📁 Project Structure:
----------------------

.
├── app.py               # Main Python file for running the Streamlit app
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── generated_image.png   # Example output image

🔧 How It Works:
-------------------
Loading the Model: The app uses StableDiffusionPipeline from the Hugging Face diffusers library. The model is loaded from the CompVis/stable-diffusion-v1-4 model repository.

Text Input: Users enter a text prompt via the Streamlit interface.

Image Generation: The text prompt is passed to the Stable Diffusion model, which generates an image corresponding to the description.

Output: The generated image is displayed in the Streamlit app, and the user can save the image locally.

🖥️ Example:
-------------
Below are the examples of the interface and a generated image:

Prompt: "A futuristic city skyline at sunset"
Output:![Example2](https://github.com/user-attachments/assets/026a3aa0-05f8-46fa-be43-52514df7b9d7)

Prompt: "Formula one cars in racing tracks"
Output:![Example1](https://github.com/user-attachments/assets/82d4854f-1042-4bc6-8f0b-92b844d883dc)



🧪 Technologies Used:
------------------------
PyTorch: As the underlying framework for model inference.
Hugging Face Diffusers: Provides pre-trained models for diffusion-based image generation.
Streamlit: Used to create the interactive web interface for the app.
Pillow: For saving and processing images.
🐞 Troubleshooting
CUDA Error: Ensure that you have a compatible GPU and the necessary CUDA libraries installed if you want to run the model on GPU. Otherwise, the model will run on the CPU by default.
Model Download Issues: If you encounter problems downloading the model, ensure that you have an active internet connection. You may also need to authenticate with Hugging Face if required.
💡 Future Enhancements
Model Selection: Add options to select between different versions of the Stable Diffusion model.
Image Customization: Allow users to specify image size, style, and other customization options.
Batch Processing: Generate multiple images at once based on different prompts.
