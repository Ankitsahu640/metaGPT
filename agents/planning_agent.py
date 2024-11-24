from langchain_groq import ChatGroq

def generate_project_plan_groq(project_description):

    GROQ_LLM = ChatGroq(
        model="llama3-70b-8192",
    )
    
    prompt = f"""
    You are a professional SDLC documentation generator. Create a highly detailed and structured SDLC document
    based on the provided project description. Follow these instructions:
    
    1. Start with a **Project Overview** that summarizes the project's goals, objectives, and intended audience.
    2. Include **User Stories** with clear descriptions, acceptance criteria, and priorities.
    3. Add **Technical Stories** with technologies, tools, APIs, and backend/frontend specifications.
    4. Clearly list **Assumptions and Limitations** for the project.
    5. Provide **Scalability Considerations** for future improvements.
    6. Use a **Table of Contents** for navigation.
    7. Ensure that the output is structured in Markdown (`README.md`) format.

    Input Project Description:
    {project_description}
    """
    result = GROQ_LLM.invoke(prompt)

    return result.content
    
