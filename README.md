
# BenBot

BenBot is an AI-driven Splunk chatbot that helps streamline interactions with Splunk data by leveraging OpenAI's API for natural language understanding and response generation. This project is designed to integrate seamlessly with Splunk, enhancing data queries, insights, and user interaction.

## Features

- **AI-Powered Responses**: Uses OpenAI's language models to interpret and respond to queries.
- **Splunk Integration**: Directly connects to Splunk for querying logs and data.
- **User-Friendly Configuration**: Includes a configurable setup to customize API keys and Splunk settings.

## Requirements

- **Python 3.7+**
- **Docker**: For containerized deployment.
- **OpenAI API Key**: Required for AI-driven responses.
- **Splunk**: An active Splunk instance for log and data access.

## Installation

### Clone the Repository

Clone the repository to your local machine:

```bash
git clone git@github.com:johdcyber/benbot.git
cd benbot
```

## Docker Deployment

### Step 1: Build the Docker Image

To deploy BenBot using Docker, build the Docker image by running:

```bash
docker build -t benbot .
```

### Step 2: Configure Environment Variables

Create an `.env` file in the project root to store your environment variables, like your OpenAI API key and Splunk credentials:

```env
OPENAI_API_KEY=your_openai_api_key
SPLUNK_HOST=your_splunk_host
SPLUNK_PORT=your_splunk_port
SPLUNK_USERNAME=your_splunk_username
SPLUNK_PASSWORD=your_splunk_password
```

### Step 3: Run the Docker Container

After building the image and configuring the environment, you can run the container:

```bash
docker run --env-file .env -p 8080:8080 benbot
```

This will start BenBot, which will be accessible on `http://localhost:8080`.

## Usage

1. **Access the BenBot Interface**: Go to `http://localhost:8080` to start interacting with the chatbot.
2. **Query Splunk Data**: Enter queries in natural language to retrieve and analyze data from Splunk.

## Security Note

To prevent accidental exposure, ensure sensitive information, such as API keys, are kept out of version control. It’s recommended to add `config.txt` or `.env` to `.gitignore`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

### Contributions

We welcome contributions that add new features or enhance functionality. Feel free to fork the project and submit pull requests.

