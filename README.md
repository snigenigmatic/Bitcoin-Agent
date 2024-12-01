# Bitcoin Agent 🤖💰

## Overview

Bitcoin Agent is a sophisticated tool designed to help traders and investors make informed decisions in the cryptocurrency market, specifically focused on Bitcoin. 

## Features

- **Real-time Price display**: Show the current price of Bitcoin in a user-friendly format.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection for real-time data
- API keys for cryptocurrency exchanges 

## Installation

1. Clone the repository:
```bash
git clone https://github.com/snigengmatic/Bitcoin-Agent.git
cd Bitcoin-Agent
```

2. Create a virtual environment (recommended):
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Run the backend:
```bash
python main.py
```

5. Access the web interface:
- install frontend dependencies:
```bash
// from root directory
npm install
```
- run `npm run dev` in the frontend directory:
```bash
npm run dev
```

## Configuration

Create a `.env` file in the project backend directory with the following variables:
```
OPENAI_API_KEY=your_openai_api_key
```

## Usage

1. Start the agent:
```bash
python main.py
```

2. Access the web interface:
- Open your browser
- Navigate to `http://localhost:3000`

3. Configure your trading parameters:
- Set your risk tolerance
- Define trading strategies
- Configure alerts

## Project Structure

```
Bitcoin-Agent/
├── app     
│   ├── componenets           # main react components
│   ├── api                   # API routes to the agent
├── backend             # Backend files
    ├── requirements.txt    # List of dependencies
    ├── main.py             # Main entry point
    ├── README.md           # Project description
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Security

- Never share your API keys
- Use environment variables for sensitive information
- Regularly update dependencies
- Monitor trading activity for unusual patterns


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by the C Kaustubh
