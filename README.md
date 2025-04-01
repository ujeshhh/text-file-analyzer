### **AI-Powered Text & File Analyzer 🚀**

This project leverages the power of **Google Gemini AI** and **spaCy** to provide an intelligent and interactive text analysis tool. With the help of **Gradio**, it features a user-friendly web interface for seamless input and output.

#### **Features:**
- **Smart Text Analysis**: Summarization, sentiment analysis, keyword extraction, and named entity recognition (NER).
- **Word Count**: Get the total word count for your input text.
- **File Support**: Upload `.txt` files or enter text manually for immediate analysis.
- **Interactive Web UI**: Built with **Gradio** for a simple and interactive experience.
- **Fast & Scalable**: Handle large text files with ease and provide insights quickly.
- **AI-Generated Reports**: Get detailed AI-driven reports with text analysis, summarization, sentiment, keywords, entities, and word count.
  
#### **Technologies Used:**
- **Google Gemini AI**: For text generation and summarization.
- **spaCy**: For named entity recognition and NLP tasks.
- **YAKE**: For keyword extraction.
- **Gradio**: For creating the web-based user interface.
  
#### **How It Works:**
- Users can input plain text or upload `.txt` files.
- The tool generates a detailed report, including a summary of the text, sentiment analysis, extracted keywords, named entities, and a word count.
- Built using **Python** and deployed on **Hugging Face** for easy access.

#### **Run the Project:**
1. Clone the repository:
   ```bash
   git clone https://github.com/ujeshhh/text-file-analyzer.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your **Google Gemini API Key** as an environment variable:
   ```bash
   export GEMINI_API_KEY="your_api_key"
   ```
4. Run the application:
   ```bash
   python app.py
