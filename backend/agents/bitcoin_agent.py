from crewai import Agent
import requests

class BitcoinAgent:
    def __init__(self):
        self.agent = Agent(
            role='Bitcoin Price Analyst',
            goal='Fetch and analyze current Bitcoin price data',
            backstory='An expert in cryptocurrency market analysis with real-time price monitoring capabilities',
            verbose=True
        )

    def process_query(self, query: str):
        try:
            # Always attempt to fetch the price for Bitcoin-related queries
            response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json', timeout=10)
            if response.status_code != 200:
                raise Exception(f"CoinDesk API returned status code {response.status_code}")
                
            data = response.json()
            price = data['bpi']['USD']['rate_float']
            timestamp = data['time']['updated']
            
            # Format response based on query type
            if "price" in query.lower() or "worth" in query.lower() or "value" in query.lower() or "cost" in query.lower():
                return {
                    'response': f"The current Bitcoin price is ${price:,.2f} USD (as of {timestamp})"
                }
            else:
                return {
                    'response': f"Bitcoin is currently trading at ${price:,.2f} USD (as of {timestamp})"
                }
        except requests.Timeout:
            return {'error': "The Bitcoin price service is taking too long to respond. Please try again."}
        except requests.RequestException as e:
            return {'error': f"Failed to connect to the Bitcoin price service: {str(e)}"}
        except Exception as e:
            return {'error': f"Error processing Bitcoin query: {str(e)}"}