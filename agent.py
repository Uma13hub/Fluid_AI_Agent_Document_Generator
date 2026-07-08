from document_generator import create_docx


def create_plan(user_request):

    return [
        "Analyze the user request and identify the business objective",
        "Determine the required document type and structure",
        "Identify key sections required for stakeholder communication",
        "Generate professional business content",
        "Review content for completeness and clarity",
        "Create the final Microsoft Word document"
    ]


def generate_document_content(user_request, plan):

    document_content = {

        "1. Request Analysis": 
        f"""
User Request:

{user_request}

The AI agent analyzed the request and identified the requirement
as a business proposal document.
""",


        "2. Agent Understanding":
        """
The autonomous AI agent determined that the required output is a
professional project proposal for implementing an AI-powered customer
support chatbot solution.
""",


        "3. Generated Execution Plan": [
            plan[0],
            plan[1],
            plan[2],
            plan[3],
            plan[4],
            plan[5]
        ],


        "4. Executive Summary":
        """
The organization aims to improve customer support efficiency by
implementing an AI-powered chatbot solution.

The proposed system will automate customer queries, reduce response
time, and improve customer satisfaction.
""",


        "5. Business Objectives": [
            "Automate repetitive customer interactions",
            "Reduce customer response time",
            "Improve support team productivity",
            "Provide 24/7 customer assistance"
        ],


        "6. Current Challenges": [
            "High volume of manual customer queries",
            "Long response times during peak hours",
            "Increased operational cost",
            "Limited availability of support agents"
        ],


        "7. Proposed Solution":
        """
Implement an AI-powered chatbot using Large Language Models (LLMs)
with integration into existing customer support platforms.

The solution includes:
""",


        "Solution Features": [
            "Natural language understanding",
            "Automated query resolution",
            "Knowledge base integration",
            "Human escalation workflow"
        ],


        "8. Technical Approach": [
            "Phase 1: Requirement analysis and data collection",
            "Phase 2: AI model integration and chatbot development",
            "Phase 3: Testing and user validation",
            "Phase 4: Production deployment"
        ],


        "9. Implementation Timeline": [
            "Month 1: Requirement gathering and architecture design",
            "Month 2-3: Development and integration",
            "Month 4: Testing and deployment"
        ],


        "10. Required Resources": [
            "AI Engineer",
            "Backend Developer",
            "QA Engineer",
            "Cloud Infrastructure",
            "AI Model Platform",
            "Database"
        ],


        "11. Risks and Mitigation": [
            "Incorrect AI responses - Implement validation and human review workflow",
            "Data privacy concerns - Apply security controls and access restrictions",
            "Integration issues - Perform phased deployment"
        ],


        "12. Expected Benefits": [
            "Faster customer response",
            "Reduced operational effort",
            "Improved customer experience",
            "Better support analytics"
        ],


        "13. Conclusion":
        """
The AI-powered customer support chatbot will improve business efficiency
by automating customer interactions while allowing support teams to focus
on complex issues.

The autonomous AI agent successfully analyzed the request, created an
execution plan, generated the required business document, and produced
the final Word output.
"""
    }

    return document_content



def run_agent(user_request):

    # Step 1: Autonomous planning
    plan = create_plan(user_request)


    # Step 2: Execute document generation
    document_content = generate_document_content(
        user_request,
        plan
    )


    # Step 3: Create DOCX
    file_path = create_docx(
        document_content,
        title="AI Customer Support Chatbot Proposal"
    )


    return {
        "plan": plan,
        "document": file_path,
        "content": document_content
    }