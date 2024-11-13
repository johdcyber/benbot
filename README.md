
# BenBot

BenBot is an AI-driven Splunk chatbot that helps streamline interactions with Splunk data by leveraging OpenAI's API for natural language understanding and response generation. This project is designed to integrate seamlessly with Splunk, enhancing data queries, insights, and user interaction.

## Features

- **AI-Powered Responses**: Uses OpenAI's language models to interpret and respond to queries.
- **Splunk Integration**: Directly connects to Splunk for querying logs and data.
- **User-Friendly Configuration**: Includes a configurable setup to customize API keys and Splunk settings.

## Requirements

- **Python 3.7+**
- **Splunk**: An active Splunk instance for log and data access.
- **OpenAI API Key**: Required for AI-driven responses.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:johdcyber/benbot.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd benbot
   ```

3. **Install Required Packages**:
   Use `pip` to install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Keys**:
   Add your OpenAI API key and Splunk credentials in the `config.txt` file.

## Usage

1. **Run BenBot**:
   Launch the chatbot with:
   ```bash
   python benbot.py
   ```

2. **Interact with Splunk Data**:
   Enter queries in natural language to retrieve and interact with your Splunk data.

## Security Note

Ensure that sensitive information, such as API keys, is not committed to the repository. Add `config.txt` to `.gitignore` to avoid accidental exposure.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

### Contributions

Feel free to fork this project and submit pull requests! We welcome contributions that enhance functionality or add new features.

