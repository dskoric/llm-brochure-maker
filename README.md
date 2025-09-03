LLM Brochure Maker
A Python tool that automatically generates company brochures by scraping websites and using Large Language Models (LLMs) to summarize the content into a professional brochure.

Features
Scrapes company websites to extract relevant information
Identifies important pages (About, Careers, etc.)
Generates professional brochures using LLMs
Supports both OpenAI API and local Ollama models
Installation

1. Clone the repository:
git clone https://github.com/dskoric/llm-brochure-maker.git
cd llm-brochure-maker

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt


Setup
Option 1: Using OpenAI API
1. Copy the environment template:
cp .env.example .env

2. Edit .env file and add your OpenAI API key:
OPENAI_API_KEY=your_openai_api_key_here


Option 2: Using Ollama (Free Alternative)

1. Install Ollama by following the instructions at https://ollama.com/
2. Pull a suitable model (e.g., Llama 3):
ollama pull llama3
3. Copy the environment template:
cp .env.example .env
4. Edit .env file and set the following:
USE_OLLAMA=true
OLLAMA_MODEL=llama3

Usage
Command Line Interface
Generate a brochure using OpenAI:
python -m src.main "Company Name" "https://company-website.com"

Generate a brochure using Ollama:
python -m src.main "Company Name" "https://company-website.com" --use-ollama

Save the brochure to a file:
python -m src.main "Company Name" "https://company-website.com" --output brochure.md

Generate a humorous brochure:
python -m src.main "Company Name" "https://company-website.com" --tone humorous


Python API
from src.llm.brochure_generator import BrochureGenerator

# Using OpenAI
generator = BrochureGenerator()
brochure = generator.generate_brochure("Company Name", "https://company-website.com")
print(brochure)

# Using Ollama
generator = BrochureGenerator(use_ollama=True)
brochure = generator.generate_brochure("Company Name", "https://company-website.com")
print(brochure)

Project Structure:
llm-brochure-maker/
├── src/
│   ├── scraper/         # Web scraping functionality
│   ├── llm/            # LLM integration and prompts
│   ├── utils/          # Configuration and utilities
│   └── main.py         # CLI entry point
├── notebooks/          # Jupyter notebooks for experimentation
├── tests/              # Unit tests
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variables template
└── README.md          # This file

How It Works
The scraper extracts the main content from the company's website
The LLM analyzes the links to identify relevant pages (About, Careers, etc.)
The scraper extracts content from these relevant pages
The LLM generates a concise brochure summarizing the company information
Troubleshooting
If you encounter API key issues, verify your .env file is correctly configured
For Ollama issues, ensure the Ollama service is running and the model is downloaded
If website scraping fails, some sites may have anti-scraping measures
License
This project is open source and available under the MIT License.