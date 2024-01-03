# Llama-2 Knowledge Building Application

This Python application is designed to simplify knowledge building within your team by providing a question-answering system based on scientific publications related to "Llama-2" fetched from the ArXiv API. It utilizes OpenAI's GPT-3.5 for answering questions about Llama-2.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Rate Limiting](#rate-limiting)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The project is structured into multiple modules for clarity and modularity:

1. **`fetch_arxiv.py`**: Fetches scientific papers related to "Llama-2" from the ArXiv API and returns them as a list of strings.

2. **`data_preparation.py`**: Performs data cleaning and preparation on the fetched papers to remove inconsistencies and prepare them for embedding generation.

3. **`generate_embeddings.py`**: Uses OpenAI's embedding algorithms to convert the cleaned papers into embeddings.

4. **`main.py`**: The main application that allows users to ask questions about Llama-2. It uses GPT-3.5 and the generated embeddings to provide answers.

5. **`requirements.txt`**: Contains a list of required Python packages for this project.

## Installation

To set up and run the application, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/asadkarim7/llama-knowledge-builder.git
   cd llama-knowledge-builder
    ```
2. Install the required Python packages:
    ```bash
   pip install -r requirements.txt
   ```
   1. Create a `.env` file in the root directory of the project and add your OpenAI API key to it:

      ```bash
        OPENAI_API_KEY=your-api-key
        ```
   2. Run the application:
      ```bash
      python main.py
      ```
## Usage

The application is designed to be simple and easy to use. It provides a command-line interface that allows users to ask questions about Llama-2 and get answers from the scientific papers fetched from the ArXiv API.

To ask a question, simply run the application and type your question into the command-line interface. The application will then fetch the relevant papers from the ArXiv API, clean them, generate embeddings, and use GPT-3.5 to provide an answer to your question.

## Rate Limiting

The application includes rate limiting to comply with ArXiv's API terms. It waits for 3 seconds between each batch of API requests to ensure that the rate limit of one request every three seconds is not exceeded.
```bash 
python main.py --limit 100
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
    
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
