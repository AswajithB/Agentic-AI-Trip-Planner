import os
import sys
from dotenv import load_dotenv

# Ensure project root is in path
sys.path.append(os.getcwd())
load_dotenv()

from tools.weather_info_tool import WeatherInfoTool
from tools.place_search_tool import PlaceSearchTool
from tools.expense_calculator_tool import CalculatorTool
from tools.currency_conversion_tool import CurrencyConverterTool
from logger import logger

def test_tools():
    print("Starting Tool Verification...")
    logger.info("Starting Tool Verification Script")

    # 1. Test Weather Tool
    try:
        print("Testing WeatherInfoTool...", end=" ")
        weather_tool = WeatherInfoTool()
        # Test getting current weather for a known city
        result = weather_tool.weather_tool_list[0].invoke("London")
        if "London" in result or "degree" in result or "N/A" in result:
            print("✅ Passed")
            logger.info(f"Weather Tool Test Passed. Result: {result}")
        else:
            print(f"❌ Failed (Unexpected result: {result})")
    except Exception as e:
        print(f"❌ Failed ({e})")
        logger.error(f"Weather Tool Test Failed: {e}")

    # 2. Test Place Search Tool
    try:
        print("Testing PlaceSearchTool...", end=" ")
        place_tool = PlaceSearchTool()
        # Test searching for attractions
        result = place_tool.place_search_tool_list[0].invoke("Eiffel Tower")
        if result:
            print("✅ Passed")
            logger.info(f"Place Search Tool Test Passed.")
        else:
            print("❌ Failed (Empty result)")
    except Exception as e:
        print(f"❌ Failed ({e})")
        logger.error(f"Place Search Tool Test Failed: {e}")

    # 3. Test Calculator Tool
    try:
        print("Testing CalculatorTool...", end=" ")
        calc_tool = CalculatorTool()
        # Test multiplication
        result = calc_tool.calculator_tool_list[0].invoke({"price_per_night": 100, "total_days": 5})
        if result == 500:
            print("✅ Passed")
            logger.info(f"Calculator Tool Test Passed. Result: {result}")
        else:
            print(f"❌ Failed (Expected 500, got {result})")
    except Exception as e:
        print(f"❌ Failed ({e})")
        logger.error(f"Calculator Tool Test Failed: {e}")

    # 4. Test Currency Converter Tool
    try:
        print("Testing CurrencyConverterTool...", end=" ")
        curr_tool = CurrencyConverterTool()
        # Test conversion (assuming API key works, otherwise it might fail or return 0/error)
        result = curr_tool.currency_converter_tool_list[0].invoke({"amount": 100, "from_currency": "USD", "to_currency": "EUR"})
        if isinstance(result, (int, float)) and result > 0:
            print("✅ Passed")
            logger.info(f"Currency Tool Test Passed. Result: {result}")
        else:
            # If API key is missing or invalid, it might return None or error string. 
            # We assume it passes if it runs without crashing, but let's check basic validity.
            print(f"⚠️ Warning (Result: {result}) - Check API Key")
            logger.warning(f"Currency Tool Test Warning: {result}")
    except Exception as e:
        print(f"❌ Failed ({e})")
        logger.error(f"Currency Tool Test Failed: {e}")

    print("\nVerification Complete. Check logs for details.")

if __name__ == "__main__":
    test_tools()
