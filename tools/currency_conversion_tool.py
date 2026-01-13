import os
from utils.currency_converter import CurrencyConverter
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv
from logger import logger

class CurrencyConverterTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("EXCHANGE_RATE_API_KEY")
        self.currency_service = CurrencyConverter(self.api_key)
        self.currency_converter_tool_list = self._setup_tools()
        logger.info("CurrencyConverterTool initialized")

    def _setup_tools(self) -> List:
        """Setup all tools for the currency converter tool"""
        @tool
        def convert_currency(amount:float, from_currency:str, to_currency:str):
            """Convert amount from one currency to another"""
            logger.info(f"Converting {amount} from {from_currency} to {to_currency}")
            result = self.currency_service.convert(amount, from_currency, to_currency)
            logger.info(f"Converted amount: {result}")
            return result
        
        return [convert_currency]