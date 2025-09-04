import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))
import argparse
from src.llm.brochure_generator import BrochureGenerator  #from llm.brochure_generator import BrochureGenerator

def main():
    parser = argparse.ArgumentParser(description='Generate company brochures using LLM')
    parser.add_argument('company_name', help='Name of the company')
    parser.add_argument('url', help='URL of the company website')
    parser.add_argument('--tone', choices=['professional', 'humorous'], 
                       default='professional', help='Tone of the brochure')
    parser.add_argument('--output', help='Output file path (optional)')
    
    args = parser.parse_args()
    
    # Generate brochure
    generator = BrochureGenerator(tone=args.tone)
    brochure = generator.generate_brochure(args.company_name, args.url)
    
    # Output results
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(brochure)
        print(f"Brochure saved to {args.output}")
    else:
        print(brochure)

if __name__ == "__main__":
    main()