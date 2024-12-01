from crewai import Agent

class LanguageAgent:
    def __init__(self):
        self.agent = Agent(
            role='Multilingual Assistant',
            goal='Process and respond to queries in multiple languages',
            backstory='A language expert capable of understanding and processing multilingual inputs',
            verbose=True
        )

    def process_query(self, query, language='en'):
        try:
            # For non-Bitcoin queries, provide a helpful response
            return {
                'response': "I'm currently configured to help with Bitcoin-related queries. Try asking something like 'What's the current Bitcoin price?'",
                'language': language
            }
        except Exception as e:
            return {'error': str(e)}