````markdown
##  How to Run & Use This Project

Follow these steps to set up and run the Hybrid Job Search Chatbot project:

### 1. Clone the Repository
```bash
git clone https://github.com/Lazy-Creature/job-recommendation-system.git
cd job-recommendation-system
````

### 2. Set Up the Virtual Environment (Recommended)

Set up a Python virtual environment to keep dependencies contained:

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Environment Configuration

Since you cannot upload a `.env` file to GitHub, take the following steps:

* Create a `.env` file in the project’s root directory.
* Add your API key configuration:

  ```
  GROQ_API_KEY=your_groq_api_key_here
  ```

> **Note:** Ensure `.env` is included in `.gitignore` to avoid accidentally committing it.

### 5. Prepare the Built-in Dataset

Make sure `jobs.csv` (your job listings dataset) exists in the `data/` folder at the project root. The file should have lowercase headers such as:

```
title,company,location,experience,skills,description
```

Example row:

```
"Software Engineer","Tech Solutions Inc","Mumbai","2-4 years","python;javascript;sql","Develop and maintain software applications for client projects."
```

### 6. Launch the App

```bash
streamlit run app.py
```

This command runs the UI, so you can:

* **Upload a resume PDF to match relevant jobs**
* Or **ask for AI-related jobs even without uploading a resume**

### 7. Clear Your Chat History

Use the “🗑️ Clear Chat” button within the UI to reset your conversation.

---

## Project Structure Overview

```
.
├── .gitignore        # Excludes sensitive files like .env
├── app.py            # Main Streamlit application
├── requirements.txt  # Project dependencies
├── README.md         # Documentation (you’re here!)
├── data/
│   └── jobs.csv      # Built-in job dataset
└── Hidden_layer/
    ├── __init__.py
    ├── llm_loader.py
    ├── chain_builder.py
    ├── prompt_builder.py
    ├── chat_handler.py
    ├── pdf_handler.py
    └── dataset_handler.py
```

---

## Key Functionalities

* **Hybrid Chatbot**: Uses Groq’s LLaMA-3 model and optional RAG from PDF resumes.
* **Built-in Job Dataset**: Automatically matches jobs without manual uploads.
* **Modular Code**: Clean separation of concerns across helper modules.




