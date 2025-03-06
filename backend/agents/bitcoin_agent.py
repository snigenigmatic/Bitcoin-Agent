from crewai import Agent
import requests
import time
import socket
import logging
from typing import Dict, Optional, Tuple

class BitcoinAgent:
    def __init__(self):
        self.agent = Agent(
            role='Bitcoin Price Analyst',
            goal='Fetch and analyze current Bitcoin price data',
            backstory='An expert in cryptocurrency market analysis with real-time price monitoring capabilities',
            verbose=True
        )
        # Define multiple API endpoints for fallback
        self.api_endpoints = [
            ('https://api.coindesk.com/v1/bpi/currentprice.json', self._parse_coindesk),
            ('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd', self._parse_coingecko),
            ('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT', self._parse_binance)
        ]
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def _check_dns(self, url: str) -> bool:
        """Pre-check DNS resolution."""
        try:
            host = url.split('/')[2]
            socket.gethostbyname(host)
            return True
        except Exception as e:
            self.logger.warning(f"DNS resolution failed for {url}: {str(e)}")
            return False

    def _parse_coindesk(self, data: Dict) -> Tuple[float, str]:
        """Parse CoinDesk API response."""
        return data['bpi']['USD']['rate_float'], data['time']['updated']

    def _parse_coingecko(self, data: Dict) -> Tuple[float, str]:
        """Parse CoinGecko API response."""
        return float(data['bitcoin']['usd']), time.strftime('%Y-%m-%d %H:%M:%S UTC')

    def _parse_binance(self, data: Dict) -> Tuple[float, str]:
        """Parse Binance API response."""
        return float(data['price']), time.strftime('%Y-%m-%d %H:%M:%S UTC')

    def _fetch_with_retry(self, url: str, max_retries: int = 3) -> Optional[requests.Response]:
        """Fetch data with exponential backoff retry."""
        for attempt in range(max_retries):
            try:
                if not self._check_dns(url):
                    continue
                    
                wait_time = (2 ** attempt) * 1  # exponential backoff
                if attempt > 0:
                    time.sleep(wait_time)
                    
                self.logger.info(f"Attempting to fetch from {url} (attempt {attempt + 1}/{max_retries})")
                return requests.get(url, timeout=10)
            except (requests.RequestException, socket.gaierror) as e:
                self.logger.warning(f"Attempt {attempt + 1} failed for {url}: {str(e)}")
                if attempt == max_retries - 1:
                    raise

        return None

    def process_query(self, query: str):
        last_error = None
        
        for url, parser in self.api_endpoints:
            try:
                response = self._fetch_with_retry(url)
                if not response:
                    continue
                    
                if response.status_code != 200:
                    self.logger.warning(f"API {url} returned status code {response.status_code}")
                    continue

                data = response.json()
                price, timestamp = parser(data)
                
                # Format response based on query type
                if any(word in query.lower() for word in ["price", "worth", "value", "cost"]):
                    return {
                        'response': f"The current Bitcoin price is ${price:,.2f} USD (as of {timestamp})"
                    }
                else:
                    return {
                        'response': f"Bitcoin is currently trading at ${price:,.3f} USD (as of {timestamp})"
                    }
                    
            except Exception as e:
                last_error = str(e)
                self.logger.error(f"Error with {url}: {str(e)}")
                continue

        return {
            'error': f"Failed to fetch Bitcoin price from all available sources. Last error: {last_error}"
        }