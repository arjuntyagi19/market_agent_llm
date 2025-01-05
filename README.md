# Market-Research-Agent

## Description

The objective of this application is to assist users in performing comprehensive financial and market analyses of any company using publicly available information from the internet. The application employs multiple AI agents, each specialized in different aspects of financial and market research, to gather, analyze, and compile data into a cohesive and informative report. This tool enhances the user's ability to make informed decisions based on detailed and factual analysis. Key technologies used in this project include CrewAi,Langchain, Streamlit, Python and Google Gemini Flash 1.5 LLM 
The project involves developing a Multi-Agent architecture system to generate relevant AI and Generative AI use cases for a company or industry. The system consists of four main agents: a Research Agent that gathers industry and company data, a Use Case Generation Agent that analyzes this data to propose AI/ML solutions, a Resource Collection Agent that searches for relevant datasets, and a Final Proposal Agent that consolidates the use cases and resources into a comprehensive report. The solution aims to enhance operations, customer experiences, and innovation within the targeted industry by leveraging AI technologies like LLMs and GenAI.


High level design-

![image](https://github.com/user-attachments/assets/3ed2e59f-80de-4b6e-9796-073c7b9ddc0f)

The HLD provides an overview of the architecture and key components involved in the system. Below is a proposed design for your Market Research Agent project:

Key Components:
User Interface (UI)

Purpose: Interface for users to interact with the system (enter queries, view results).
Technologies: React.js for building a responsive and interactive UI.
Flow: Users enter market-related queries (e.g., stock analysis, trend prediction) and receive responses in a conversational format.
Backend API (Server)

Purpose: Handle the logic, API requests, and interactions between the UI, LLM, and database.
Technologies: Node.js (Express) or Flask for creating a RESTful API.
Flow: The server receives requests from the frontend, processes them by passing them to the LLM model, and returns the result.
Large Language Model (LLM) Integration

Purpose: Use LLMs (such as GPT-3, GPT-4, or your own custom model) to generate responses based on user input. The LLM processes queries related to market trends, stock prices, and other market research.
Technologies: Hugging Face API (or custom-trained models).
Flow: The backend communicates with the LLM, sending the user query and receiving a processed response (e.g., predictions, analysis).
Database

Purpose: Store user queries, responses, historical data, and models for analytics and performance tracking.
Technologies: MongoDB (for flexible document storage), PostgreSQL (for structured data if required).
Flow: The backend interacts with the database to store and retrieve data for analysis.
External APIs/Services (Optional)

Purpose: Integrate external APIs for real-time data such as stock prices, market trends, etc.
Technologies: APIs like Alpha Vantage, Yahoo Finance, or custom APIs for financial data.
Flow: The backend calls external APIs when required, fetching the latest market data to supplement LLM analysis.


Low-Level Design (LLD)
The LLD provides more detailed design specifications, including the structure of individual components and their functions. Below is a detailed breakdown for your Market Research Agent project:

Key Components:
Frontend (React.js)

Components:
MainComponent: Displays the user interface, sends and receives API calls, and manages the state.
InputForm: Accepts user queries related to market research and sends them to the backend.
ResponseDisplay: Renders the result from the LLM or external APIs.
State Management: Use React Context or Redux to manage the state for the application.
Backend (Node.js/Flask)

API Endpoints:
POST /query: Receives the user query and processes it (calls LLM and external APIs).
GET /history: Fetches user query history and responses from the database.
POST /trainModel: Optional endpoint for retraining models on new data (if applicable).
Business Logic:
LLM Handler: A service that communicates with the LLM API to send and receive query results.
Data Processor: Processes user input and formats it in a way that is compatible with the LLM.
Analytics/History Handler: Stores the query, response, and other metadata in the database.
LLM Integration (API)

Handler Class:
makeApiRequest(): Sends the user query to the LLM (e.g., GPT-3 or Hugging Face models) and handles the response.
parseResponse(): Processes the response from the LLM and formats it to present to the user.
Database (MongoDB/PostgreSQL)

Collections/Tables:
UserQueries: Stores user queries with timestamps.
LLMResponses: Optionally stores the LLM responses.
Analytics: Stores data for performance analysis (e.g., query trends, response times).
Schema:
UserQueries: _id, user_id, query, timestamp
LLMResponses: _id, user_id, query_id, response, timestamp


## Installation

To run this project, follow these steps:

1. Clone this repository to your local machine.
   ```bash
   git clone [https://github.com/psrane8/Market-Research-Agent.git]
   ```

2. Navigate to the project directory.
   ```bash
   cd Market-Research-Agent
   ```

3. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure you have installed all dependencies as instructed above.

2. Run the Streamlit app.
   ```bash
   streamlit run app.py
   ```

3. Access the app through your browser at http://localhost:8501

4. Create a .env file consisting of "GOOGLE_API_KEY" and "SERPER_API_KEY"
   
5. Type the name of the company and watch the report being created


## Credits

- [CrewAI](https://www.crewai.com/)
- [Langchain](https://www.langchain.com/)
- [Google Gemini Flash 1.5](https://deepmind.google/technologies/gemini/flash/)
- [Streamlit](https://streamlit.io/)
- [SerperAPI](https://serper.dev/)
- [Python](https://www.python.org/)

## License

This project is licensed under the [MIT License](LICENSE).
```
