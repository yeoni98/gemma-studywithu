
import pdfplumber
import numpy as np
import os
import streamlit as st
import re
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

load_dotenv()


def extract_text_from_pdfs(pdf_files):
    text = ""
    for pdf_file in pdf_files:
        pdf_file.seek(0)
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        pdf_file.seek(0)
    return text


def generate_answer(model, tokenizer, question, context, device, max_context_length=1024, max_new_tokens=150):
    if len(context) > max_context_length:
        context = context[:max_context_length]

    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=max_new_tokens, pad_token_id=tokenizer.eos_token_id)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer.split("Answer:")[-1].strip()


def main():
    st.set_page_config(page_title="📚 Gemma-2 Study Bot", page_icon="📚", layout="wide")
    st.header("📚 Welcome to the Gemma-2 Study Bot!")
    st.write("Upload one or more PDFs and ask questions or generate quizzes based on the content.")

    device = "cuda" if torch.cuda.is_available() else "cpu"

    @st.cache_resource
    def load_model():
        model_name = "google/gemma-2-2b-it"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name).to(device)
        return tokenizer, model

    tokenizer, model = load_model()

    uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

    if uploaded_files:
        extracted_text = extract_text_from_pdfs(uploaded_files)

        question_tab, quiz_tab = st.tabs(["Ask Questions", "Generate Quizzes"])

        with question_tab:
            question = st.text_input("Enter your question about the PDF content:")

            if question:
                max_context_length = 1024  # Set a limit for the context length
                answer = generate_answer(model, tokenizer, question, extracted_text, device,
                                         max_context_length=max_context_length, max_new_tokens=150)
                st.write(f"**Answer:** {answer}")

        with quiz_tab:
            if st.button("Generate Quiz"):
                prompt = f"""Based on the following context, create 5 multiple-choice questions, their correct answers, and explanations. 

                ### Context:
                {extracted_text[:4000]}

                Please format the output as follows:

                1. Question
                A) Option A
                B) Option B
                C) Option C
                D) Option D
                - Correct answer: (e.g., A)
                - Explanation: Explanation text

                ...

                Generate the quiz questions:"""

                inputs = tokenizer(prompt, return_tensors="pt").to(device)

                with torch.no_grad():
                    outputs = model.generate(**inputs, max_new_tokens=300, pad_token_id=tokenizer.eos_token_id)
                quiz = tokenizer.decode(outputs[0], skip_special_tokens=True)

                # Display the generated quiz
                st.write("### Generated Quiz:")
                st.write(quiz)


if __name__ == '__main__':
    main()




