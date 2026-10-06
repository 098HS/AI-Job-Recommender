<<<<<<< HEAD
# AI Job Recommender

An intelligent job recommendation system that analyzes your resume and suggests job opportunities based on your skills and experience.

## Features

- 📄 **Resume Analysis**: Upload and analyze PDF resumes
- 🤖 **AI-Powered Insights**: Get personalized career guidance and skill recommendations
- 💼 **Job Recommendations**: Discover relevant job opportunities from LinkedIn and Naukri
- 📊 **Profile Summary**: Get an overview of your professional profile

## Tech Stack

- **Streamlit**: Web application framework
- **OpenAI**: AI-powered analysis and recommendations
- **PyMuPDF**: PDF text extraction
- **Apify**: Web scraping and job data fetching
- **Python 3.12+**: Core language

## Installation

### Prerequisites
- Python 3.12 or higher
- pip or uv package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/shivamsi1255-a11y/AI-_JOB_Analyist.git
cd AI-_JOB_Analyist
```

2. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
# or
source .venv/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Or with uv:
```bash
uv sync
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your API keys (OpenAI, Apify, etc.)
```

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

Then:
1. Open your browser to the provided local URL
2. Upload your resume (PDF)
3. View analysis and get job recommendations

## Project Structure

```
.
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── pyproject.toml         # Project configuration
├── README.md              # This file
├── src/
│   ├── __init__.py
│   ├── helper.py          # Utility functions for PDF extraction and AI
│   ├── job_api.py         # Job fetching from LinkedIn and Naukri
│   └── mcp_server.py      # MCP server implementation
└── .env                   # Environment variables (not committed)
```

## Environment Variables

Create a `.env` file in the root directory with:
```
OPENAI_API_KEY=your_openai_key
APIFY_API_TOKEN=your_apify_token
```

## License

MIT License - feel free to use this project for your own purposes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
=======
# AI-Job-Recommender
>>>>>>> caea55721f6bda780cdf8f50370101f2878bbe4c
