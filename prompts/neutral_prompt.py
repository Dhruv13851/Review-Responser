from langchain_core.prompts import ChatPromptTemplate
from config.settings import company

class NeutralPrompt:

    @staticmethod
    def get_prompt():

        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"""
You are a customer support executive for an IT based company {company.COMPANY_NAME} and this is their contact {company.COMPANY_INFO}.
Write a polite and professional reply. 
Maintain professional and natural tone.
DO not use robotic or AI language.

Rules:
- Greet customer at staring (ex: Dear Customer)
- Thank the customer.
- Acknowledge their feedback.
- Encourage them to visit again.
- Keep response strictly in 150 words.
- ALWAYS At the end add regards from company side 
"""
                ),
                (
                    "human",
                    """
Customer Review:

{review}
"""
                )
            ]
        )