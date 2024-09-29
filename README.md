# 📚 Gemma-2 Study Bot: StudyWithU

## Introduction

This is a conversational web application where users can interact with an AI model based on the **Gemma-2b-it** language model. The AI provides informative and accurate responses to user queries based on PDF documents uploaded by the user. The application is built with **Streamlit** on the frontend, utilizing the **Hugging Face Transformers** library to power the backend model.

## Features

- **Real-time Chat**: Users can upload PDF documents and chat with the AI to get answers regarding the content.
- **PDF Content Analysis**: Extracts content from the uploaded PDFs and allows users to ask questions about them.
- **Quiz Generation**: Generates quizzes based on the content of the uploaded PDF for enhanced learning.
- **Session Memory**: The application maintains a conversation history to provide a continuous and seamless user experience.

## Model Information

The application utilizes the **Gemma-2b-it** model, which is designed for informative and conversational use cases, providing accurate answers and support for questions based on uploaded documents.

- **Model Name**: Gemma-2b-it
- **Model Description**: The model is fine-tuned for answering questions and providing explanations based on the context extracted from PDF documents.
- **Hugging Face Repository**: [JaeJiMin/daily_hug](https://huggingface.co/JaeJiMin/daily_hug)

The model is served locally without the need for external API calls to Hugging Face, ensuring faster response times for a real-time chat experience.

## Technologies Used

### Frontend
- **Streamlit**: Used for building the interactive user interface.
- **CSS**: For custom styling and layout adjustments within the Streamlit app.

### Backend
- **Python (Hugging Face Transformers)**: Utilizes the **Gemma-2b-it** AI model for generating responses.
- **Torch**: For loading and using the Gemma-2b-it model.
- **pdfplumber**: For extracting text from PDF files.
- **Dotenv**: To manage environment variables for secure API keys and configurations.

### Model
- **Gemma-2b-it**: A fine-tuned conversational model used to provide responses based on the content of uploaded documents.

## Setup and Installation

### Prerequisites
- **Python 3.8+** (for backend)
- **Git** (to clone the repository)
- **Streamlit** (for frontend)

### Backend Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the necessary Python dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit application**:

   ```bash
   streamlit run app.py
   ```

The Streamlit server should now be running on `http://localhost:8501`.

## Usage Instructions

1. **Upload PDF Files**: Use the "Upload PDF files" button to upload one or more PDF documents.
2. **Ask Questions**: Navigate to the "Ask Questions" tab, type in your question about the content of the uploaded PDF, and receive a response from the AI model.
3. **Generate Quizzes**: Go to the "Generate Quizzes" tab and click on "Generate Quiz" to create multiple-choice questions based on the content of the uploaded document.


## Example Usage

- **Upload PDF Documents**: Upload a PDF document that contains content you'd like to explore.
- **Ask Questions**: In the "Ask Questions" tab, enter a question like "What is the main topic of the document?" to receive an answer.
- **Generate Quizzes**: In the "Generate Quizzes" tab, click the "Generate Quiz" button to generate multiple-choice questions based on the uploaded document.

## Dependencies

- **pdfplumber**: For extracting text from PDF files.
- **torch**: For loading and using the language model.
- **transformers**: For using the **Gemma-2** model and tokenizer.
- **streamlit**: For building the user interface.
- **dotenv**: For managing environment variables.


## Acknowledgements

This project uses the **Gemma-2** language model from Google, along with the **Hugging Face Transformers** library for natural language processing.

