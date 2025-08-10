# Job Recommendation System using LangChain & LLM

This project is a **Job Recommendation System** that provides job listings from multiple fields, such as Software Engineering, AI, Healthcare, Marketing, and more. It allows users to filter jobs based on keywords, location, experience, and skills.

## Features
- Fetch job data from a CSV dataset
- Search and filter jobs by **title**, **skills**, **location**, and **experience**
- Includes jobs from multiple fields like IT, AI, Healthcare, Marketing, etc.
- User-friendly output format

## Tech Stack
- **Python** (Data handling & filtering)
- **Pandas** (For dataset management)
- **CSV dataset** (Job listings)

## Dataset
The dataset contains job details in the following format:
- **Title**: Job title (e.g., Software Engineer, Data Scientist)
- **Company**: Employer name
- **Location**: Job location
- **Experience**: Required experience in years
- **Skills**: Key skills required
- **Description**: Short job description

## Example Data
| Title                     | Company             | Location  | Experience | Skills                           | Description |
|---------------------------|---------------------|-----------|------------|-----------------------------------|-------------|
| Software Engineer         | Tech Solutions Inc  | Mumbai    | 2-4 years  | Python;JavaScript;SQL            | Develop and maintain software applications for client projects. |
| Doctor (General Physician)| City Hospital       | Delhi     | 5+ years   | Medical Diagnosis;Patient Care   | Provide healthcare services to patients in general medicine. |

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/Lazy-Creature/job-recommendation-system-llm-chatbot.git
   cd job-recommendation-system
````

2. Install dependencies:

   ```bash
   pip install pandas
   ```
3. Run the script:

   ```bash
   python main.py
   ```

## Environment Variables

Create a `.env` file in the project root to store sensitive keys (if needed):

```
API_KEY=your_api_key_here
```

Make sure `.env` is added to `.gitignore` so it is not uploaded to GitHub.

## Contributing

Pull requests are welcome. For significant changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
I used all opensource tools.....
```
