# 🔍 Epstein Files Investigative Research Assistant

An AI-powered research tool for exploring the 25,000+ Epstein document pages using Google's Gemini File Search API. Ask natural language questions and get cited answers with links back to original sources.

## 🌟 Features

- **Natural Language Search**: Ask questions in plain English
- **Source Citations**: Every answer includes references to original Google Drive documents
- **Fully Managed RAG**: Powered by Gemini File Search (no vector database setup needed)
- **25K+ Documents**: Handles the complete Epstein files dataset
- **Fast & Accurate**: Uses Gemini 2.5 Flash for quick responses or Pro for deep analysis
- **Interactive UI**: Built with Streamlit for easy exploration

## 📋 Prerequisites

- Python 3.11 or higher
- Google Gemini API key ([Get one here](https://ai.google.dev/))
- Epstein dataset CSV file (~100MB) from [HuggingFace](https://huggingface.co/datasets/tensonaut/EPSTEIN_FILES_20K)

## 🚀 Quick Start

### 1. Clone & Setup

```bash
cd epstein-research-assistant

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Copy example .env file
cp .env.example .env

# Edit .env and add your Gemini API key
# GEMINI_API_KEY=your_api_key_here
```

### 3. Download Dataset

Download the Epstein dataset CSV from HuggingFace and place it in the `data/` folder:

```bash
# Create data directory if it doesn't exist
mkdir -p data

# Place your downloaded CSV here:
# data/epstein_dataset.csv
```

### 4. Run the Application

```bash
streamlit run src/app.py
```

The app will open in your browser at `http://localhost:8501`

## 📖 How to Use

### Step 1: Load Dataset
1. The app will automatically detect your CSV file
2. Choose how many documents to process (start with 100 for testing)
3. Click "Process Documents"

### Step 2: Upload to Gemini
1. Click "Upload to Gemini" to create the search index
2. Wait for documents to upload (progress bar shows status)
3. First-time indexing costs ~$0.15 per 1M tokens

### Step 3: Ask Questions
1. Type your question in natural language
2. Click "Search"
3. View answer with source citations
4. Click on citations to see original document references

## 💡 Example Questions

- "Who are the main individuals mentioned in the documents?"
- "What locations appear most frequently?"
- "Find all communications mentioning [specific person]"
- "What types of documents are included (emails, legal, travel)?"
- "Summarize documents about [specific topic/event]"
- "Are there any documents from [specific date range]?"

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│   Streamlit UI (src/app.py)         │
│   - Query input                     │
│   - Citation display                │
│   - Document upload                 │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│   Application Layer                 │
│   - CSV Processor                   │
│   - File Search Manager             │
│   - Query Engine                    │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│   Gemini File Search API            │
│   - Automatic chunking              │
│   - Vector embeddings               │
│   - Semantic search                 │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│   Gemini 2.5 Pro/Flash              │
│   - Answer generation               │
│   - Citation extraction             │
└─────────────────────────────────────┘
```

## 📁 Project Structure

```
epstein-research-assistant/
├── .env                          # API keys (create from .env.example)
├── .env.example                  # Environment template
├── requirements.txt              # Python dependencies
├── README.md                     # This file
├── data/
│   ├── epstein_dataset.csv       # Your dataset (download separately)
│   └── processed/                # Temporary files (auto-generated)
├── src/
│   ├── __init__.py
│   ├── app.py                    # Streamlit application
│   ├── config.py                 # Configuration management
│   ├── csv_processor.py          # CSV parsing & processing
│   ├── file_search_manager.py    # Gemini File Search operations
│   ├── query_engine.py           # Query processing & formatting
│   └── utils.py                  # Helper functions
└── notebooks/
    └── data_exploration.ipynb    # Optional: Dataset analysis
```

## ⚙️ Configuration

Edit `.env` file to customize:

```bash
# Required
GEMINI_API_KEY=your_api_key_here

# Optional
MODEL_NAME=gemini-2.5-flash          # or gemini-2.5-pro
FILE_SEARCH_STORE_NAME=epstein_docs  # Custom store name
DATASET_PATH=data/epstein_dataset.csv
MAX_UPLOAD_BATCH=50                  # Upload batch size
```

## 💰 Cost Estimation

Gemini File Search pricing (as of 2025):
- **Indexing**: $0.15 per 1M tokens (one-time)
- **Storage**: FREE
- **Queries**: FREE

**Estimated costs for 25K documents:**
- Assuming ~1K tokens/document average
- 25,000 documents × 1,000 tokens = 25M tokens
- Cost: 25M × $0.15/1M = **~$3.75 one-time**

Subsequent queries are FREE!

## 🔧 Advanced Usage

### Using Different Models

**Gemini 2.5 Flash** (Default):
- Faster responses (1-2 seconds)
- Good for exploration & quick queries
- Lower latency

**Gemini 2.5 Pro**:
- Deeper analysis
- Better for complex multi-document synthesis
- More thorough citations

Change model in sidebar or `.env` file.

### Processing Full Dataset

Start with a small subset (100-1000 documents) for testing, then scale up:

```python
# In the UI, increase the document limit
# Or modify directly in code
processor.process_documents(limit=25000)  # Full dataset
```

### Custom System Instructions

Modify `query_engine.py` to customize how the AI responds:

```python
system_instruction = """
Your custom instructions here...
"""
```

## 🐛 Troubleshooting

### CSV Not Found
- Ensure CSV is in `data/epstein_dataset.csv`
- Check `DATASET_PATH` in `.env`

### API Key Error
- Verify `GEMINI_API_KEY` in `.env`
- Get API key from https://ai.google.dev/

### Upload Timeout
- Reduce `MAX_UPLOAD_BATCH` in `.env`
- Try smaller document subset first

### Memory Issues
- Process documents in smaller batches
- Use pagination in CSV processing

## 📚 Dataset Information

The Epstein Files dataset contains:
- ~25,000 document pages/emails
- OCR-processed text from JPG images
- Google Drive paths to original documents
- Released by House Oversight Committee

Download from: [HuggingFace - tensonaut/EPSTEIN_FILES_20K](https://huggingface.co/datasets/tensonaut/EPSTEIN_FILES_20K)

## 🤝 Contributing

This is a research tool built for educational and investigative purposes. Feel free to:
- Submit issues for bugs
- Suggest improvements
- Fork and customize for your needs

## ⚖️ Legal & Ethics

- This tool is for research and investigative journalism
- All data comes from publicly released documents
- Citations link back to official sources
- Use responsibly and verify information

## 📄 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

- Dataset by [@tensonaut](https://huggingface.co/tensonaut)
- Powered by Google Gemini API
- Built with Streamlit

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review [Gemini File Search docs](https://ai.google.dev/gemini-api/docs/file-search)
3. Open an issue on GitHub

---

**Built with ❤️ for transparency and investigative research**
