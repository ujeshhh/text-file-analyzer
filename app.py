import os
import gradio as gr
import google.generativeai as genai
import spacy
import yake
import subprocess

# Ensure spaCy model is downloaded dynamically
MODEL_NAME = "en_core_web_sm"
try:
    nlp = spacy.load(MODEL_NAME)
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", MODEL_NAME])
    nlp = spacy.load(MODEL_NAME)

# Configure Google Gemini AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Use environment variable for security

def analyze_text(text):
    """Perform AI-driven text analysis."""
    if not text:
        return "Please enter some text."

    # Word Count
    word_count = len(text.split())

    # Summarization using Google Gemini AI
    try:
        prompt = f"Summarize this text:\n{text}"
        model = genai.GenerativeModel(model_name="gemini-2.0-flash")
        response = model.generate_content([prompt])  # Ensure the prompt is passed as a list

        summary = response.text.strip() if response and hasattr(response, "text") else "Error in summarization."
    except Exception as e:
        summary = f"Summarization failed: {str(e)}"

    # Basic Sentiment Analysis
    sentiment = "Positive" if "good" in text.lower() else "Negative"

    # Keyword Extraction
    kw_extractor = yake.KeywordExtractor()
    keywords = [kw[0] for kw in kw_extractor.extract_keywords(text)[:5]]

    # Named Entity Recognition (NER)
    doc = nlp(text)
    entities = {ent.text: ent.label_ for ent in doc.ents}

    # AI-Generated Report
    report = f"""
    \n**Summary:** {summary}  
    \n**Sentiment:** {sentiment}  
    \n**Keywords:** {', '.join(keywords)}  
    \n**Entities:** {entities if entities else 'None'}
    \n**Word Count:** {word_count}
    """

    return report

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# AI-Powered Text & File Analyzer 🚀")
    
    input_text = gr.Textbox(label="Enter Text")
    file_input = gr.File(label="Upload .txt File", file_types=[".txt"])
    analyze_button = gr.Button("Analyze")
    output = gr.Markdown()

    def process_input(text, file):
        """Process text from input or file."""
        if file:
            with open(file.name, "r", encoding="utf-8") as f:
                text = f.read()
        return analyze_text(text)

    analyze_button.click(process_input, inputs=[input_text, file_input], outputs=output)

demo.launch()