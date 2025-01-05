from crewai_tools import SerperDevTool
import os

# Directly assign the API key
serper_api_key = ""

# Assign the SERPER_API_KEY to the environment
os.environ["SERPER_API_KEY"] = serper_api_key

# Tool for searching on Google
tool = SerperDevTool()
