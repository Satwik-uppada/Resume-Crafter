# Revamp360 🚀

Welcome to the **Revamp 360**, an AI-driven application that helps you optimize resumes based on specific job descriptions. This tool leverages advanced language models to tailor resumes to align with job postings, giving users a competitive edge in their job applications.

![GitHub repo size](https://img.shields.io/github/repo-size/Satwik-uppada/Resume-Crafter)
![GitHub last commit](https://img.shields.io/github/last-commit/Satwik-uppada/Resume-Crafter)
![License](https://img.shields.io/badge/license-MIT-blue)

---

## Table of Contents
1. [Demo](#demo)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technologies](#technologies)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)

---

## Demo

Check out the **AI Resume Crafter** in action! Featuring a **3D rotating cube** and **neon-themed** UI, the demo showcases how users can upload resumes, enter job descriptions, and receive optimized versions quickly.

![image](https://github.com/user-attachments/assets/dcfac7b8-4d53-4a91-819b-5a816af0eda4)



---

## Features

- **3D Animated Cube**: Adds a unique, futuristic aesthetic while the resume is generated.
- **Neon-Themed UI**: Custom CSS styling gives a sleek, tech-forward design.
- **File Upload and Text Input**: Allows users to upload resumes and job descriptions as text files or manually paste content.
- **AI-Powered Optimization**: Uses the Groq API with advanced language models for precise resume tailoring.
- **Downloadable Resume**: Once optimized, users can download the resume in a text format for easy editing.

---

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Satwik-uppada/Resume-Crafter.git
    cd Resume-Crafter
    ```

2. **Set Up Environment**:
    - Make sure you have Python installed (3.8+ recommended).
    - Install necessary packages:
        ```bash
        pip install streamlit python-dotenv groq
        ```

3. **Environment Variables**:
    - Create a `.env` file in the project directory.
    - Add your Groq API key:
        ```plaintext
        GROQ_API_KEY=your_groq_api_key_here
        ```

4. **Run the App**:
    ```bash
    streamlit run app.py
    ```

---

## Usage

1. **Launch the App**:
    - Run the app with `streamlit run app.py` and open the local server link.

2. **Input Your Resume**:
    - Upload your resume file (`.txt` format) or paste the text manually.

3. **Input Job Description**:
    - Upload the job description file or paste it manually in the provided text area.

4. **Optimize**:
    - Click the "Optimize Resume" button to generate an AI-tailored version of your resume for the job description provided.
    - The app will display a rotating 3D cube animation as it processes the resume.

5. **Download**:
    - Once the optimized resume is generated, you can download it directly in a text file format.

---

## Technologies

- **Frontend**: [Streamlit](https://streamlit.io/) for the interactive user interface.
- **Backend**: [Groq API](https://groq.com/) for language model integration.
- **Styling**: Custom CSS for a futuristic design with animated 3D cube effects.
- **Environment Management**: [python-dotenv](https://pypi.org/project/python-dotenv/) for secure API key handling.

---

## Contributing

Contributions are welcome! Here’s how you can get started:

1. **Fork the Project**.
2. **Create a Branch**: `git checkout -b feature/AmazingFeature`
3. **Commit Your Changes**: `git commit -m 'Add some AmazingFeature'`
4. **Push to the Branch**: `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

**Satwik Uppada**  
- LinkedIn: [Satwik Uppada](https://www.linkedin.com/in/satwik-uppada/)
- GitHub: [Satwik Uppada](https://github.com/Satwik-uppada/)

---

Enjoy using the **AI Resume Crafter**! Feel free to reach out for questions or suggestions.
