from openai import OpenAI
from src.scraper.website import Website #from ..scraper.website import Website
from .link_analyzer import LinkAnalyzer
from ..utils.config import MODEL, openai

class BrochureGenerator:
    """Generates company brochures using LLM"""
    
    def __init__(self, tone: str = "professional"):
        self.link_analyzer = LinkAnalyzer()
        self.tone = tone
        self._set_system_prompt()
    
    def _set_system_prompt(self):
        """Set the system prompt based on desired tone"""
        if self.tone == "humorous":
            self.system_prompt = """You are an assistant that analyzes the contents of several relevant pages from a company website 
            and creates a short humorous, entertaining brochure about the company for prospective customers, investors and recruits. Respond in markdown.
            Include details of company culture, customers and careers/jobs if you have the information."""
        else:
            self.system_prompt = """You are an assistant that analyzes the contents of several relevant pages from a company website 
            and creates a short brochure about the company for prospective customers, investors and recruits. Respond in markdown.
            Include details of company culture, customers and careers/jobs if you have the information."""
    
    def get_all_details(self, url: str) -> str:
        """Get all details from landing page and relevant links"""
        result = "Landing page:\n"
        result += Website(url).get_contents()
        links = self.link_analyzer.get_relevant_links(url)
        print("Found links:", links)
        
        for link in links["links"]:
            result += f"\n\n{link['type']}\n"
            result += Website(link["url"]).get_contents()
        
        return result
    
    def get_user_prompt(self, company_name: str, url: str) -> str:
        """Generate user prompt for brochure generation"""
        user_prompt = f"You are looking at a company called: {company_name}\n"
        user_prompt += f"Here are the contents of its landing page and other relevant pages; use this information to build a short brochure of the company in markdown.\n"
        user_prompt += self.get_all_details(url)
        user_prompt = user_prompt[:5000]  # Truncate if more than 5,000 characters
        return user_prompt
    
    def generate_brochure(self, company_name: str, url: str) -> str:
        """Generate a brochure for the company"""
        user_prompt = self.get_user_prompt(company_name, url)
        
        response = openai.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        
        return response.choices[0].message.content