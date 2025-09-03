import json
from openai import OpenAI
from ..scraper.website import Website
from ..utils.config import MODEL, openai

class LinkAnalyzer:
    """Analyzes website links to determine which are relevant for brochure creation"""
    
    def __init__(self):
        self.system_prompt = """You are provided with a list of links found on a webpage. 
        You are able to decide which of the links would be most relevant to include in a brochure about the company, 
        such as links to an About page, or a Company page, or Careers/Jobs pages.
        You should respond in JSON as in this example:
        {
            "links": [
                {"type": "about page", "url": "https://full.url/goes/here/about"},
                {"type": "careers page", "url": "https://another.full.url/careers"}
            ]
        }"""
    
    def get_user_prompt(self, website: Website) -> str:
        """Generate user prompt for link analysis"""
        user_prompt = f"Here is the list of links on the website of {website.url} - "
        user_prompt += "please decide which of these are relevant web links for a brochure about the company, respond with the full https URL in JSON format. "
        user_prompt += "Do not include Terms of Service, Privacy, email links.\n"
        user_prompt += "Links (some might be relative links):\n"
        user_prompt += "\n".join(website.links)
        return user_prompt
    
    def get_relevant_links(self, url: str) -> dict:
        """Get relevant links from a website"""
        website = Website(url)
        response = openai.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": self.get_user_prompt(website)}
            ],
            response_format={"type": "json_object"}
        )
        result = response.choices[0].message.content
        return json.loads(result)