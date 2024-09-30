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
- **Hugging Face Personal Token**: A personal access token from Hugging Face is required to access the **Gemma-2b-it** model. You can obtain it by [signing up](https://huggingface.co/join) on Hugging Face and navigating to your [tokens page](https://huggingface.co/settings/tokens).

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

4. **Configure Environment Variables**:

   - Create a `.env` file in the root directory of the project.
   - Add your Hugging Face personal token to the `.env` file:

     ```env
     HUGGINGFACE_TOKEN=your_hugging_face_token_here
     ```

     > **주의**: `.env` 파일은 절대 버전 관리 시스템(Git 등)에 포함되지 않도록 `.gitignore` 파일에 추가해야 합니다.

5. **Run the Streamlit application**:

   ```bash
   streamlit run app.py
   ```

   The Streamlit server should now be running on `http://localhost:8501`.

It sounds like you want to develop a system with two main functions: 


## Results
1. **Ask Questions**
- **Functionality**: Users can **upload a PDF** and **ask questions** about its content. 
- **Features**:
  - The system **generates answers** based on the contents of the uploaded PDF.
  - The system **remembers previous responses**, allowing users to **ask follow-up questions**, like "**Can you explain more?**" based on the **context of prior answers**.
  

2. **Generate Quizzes**
- **Functionality**: **Generates 5 random quizzes** each time.
- **Features**:
  - Provides **new random quizzes** each time they are generated.
  - When a user selects an **incorrect answer**, the system displays a message indicating it is incorrect.
  - When a user selects the **correct answer**, the system **confirms it** and provides an **explanation**.
  ### ![Screenshot 2024-10-01 at 8 32 51 AM](https://github.com/user-attachments/assets/de90a2cf-1d53-45f2-bfae-c6561f871007)
  ### ![Screenshot 2024-10-01 at 8 33 08 AM](https://github.com/user-attachments/assets/0ec6b4c6-44fb-426c-9426-4c57c690bcdf)
   ![Screenshot 2024-10-01 at 8 33 26 AM](https://github.com/user-attachments/assets/96a73d56-da09-48c9-bd09-e7f690f38677)

