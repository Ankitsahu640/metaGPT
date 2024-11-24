import os
from agents.understanding_agent import extract_text_from_pdf
from agents.planning_agent import generate_project_plan_groq

def main():

    print("Extracting content from the PDF...")
    project_description = extract_text_from_pdf("data/document.pdf")
    print("PDF content extracted successfully.")

    print("Generating SDLC documentation using ChatGroq...")
    sdlc_documentation = generate_project_plan_groq(project_description)
    print("SDLC documentation generated successfully.")

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "README.md")
    print(f"Saving output to: {os.path.abspath(output_file)}")
    
    try:
        with open(output_file, 'w') as file:
            file.write(sdlc_documentation)
        print(f"File successfully written to {output_file}")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":

    os.environ["GROQ_API_KEY"] = "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"
    
    main()
