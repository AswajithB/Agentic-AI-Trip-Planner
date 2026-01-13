from utils.expense_calculator import Calculator
from typing import List
from langchain.tools import tool
from logger import logger

class CalculatorTool:
    def __init__(self):
        self.calculator = Calculator()
        self.calculator_tool_list = self._setup_tools()
        logger.info("CalculatorTool initialized")

    def _setup_tools(self) -> List:
        """Setup all tools for the calculator tool"""
        @tool
        def estimate_total_hotel_cost(price_per_night:int, total_days:int) -> int:
            """Calculate total hotel cost"""
            logger.info(f"Calculating total hotel cost for {total_days} nights at {price_per_night} per night")
            result = self.calculator.multiply(price_per_night, total_days)
            logger.info(f"Estimated total hotel cost: {result}")
            return result
        
        @tool
        def calculate_total_expense(*costs: float) -> float:
            """Calculate total expense of the trip"""
            logger.info(f"Calculating total expense for costs: {costs}")
            result = self.calculator.calculate_total(*costs)
            logger.info(f"Total expense: {result}")
            return result
        
        @tool
        def calculate_daily_expense_budget(total_cost: float, days: int) -> float:
            """Calculate daily expense"""
            logger.info(f"Calculating daily budget for total cost {total_cost} over {days} days")
            result = self.calculator.calculate_daily_budget(total_cost, days)
            logger.info(f"Daily budget: {result}")
            return result
        
        return [estimate_total_hotel_cost, calculate_total_expense, calculate_daily_expense_budget]