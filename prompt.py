from langchain_core.prompts import PromptTemplate

# Define a prompt template for Nepali Constitution Q&A
def create_constitution_prompt():
    return PromptTemplate(
        input_variables=["context", "question"],
        template="""तपाईंलाई नेपालको संविधानको सम्बन्धित खण्डहरूको जानकारी दिइएको छ।

        तपाईंलाई नेपालको संविधानको सम्बन्धित खण्डहरूको जानकारी दिइएको छ। 
    तपाईंको काम:  

    1. प्रयोगकर्ताको प्रश्नको उत्तर दिनुहोस्।  
    2. उत्तर **नेपाली भाषामा स्पष्ट र संक्षिप्त** दिनुहोस्।  
    3. **स्रोत र पृष्ठ संख्या** उल्लेख गर्नुहोस्।  
    4. केवल दिइएको context मा आधारित भएर जवाफ दिनुहोस्, अन्यथा "स्रोतमा जानकारी उपलब्ध छैन" भन्नुहोस्।  
    तपाईंले यस प्रश्नको उत्तर **छोटो, स्पष्ट र संक्षिप्त** दिनुहोस्।  
  
 

    प्रयोगकर्ता प्रश्न:
    {question}

    सन्दर्भ खण्डहरू:
    {context}

    कृपया प्रश्नको उत्तर तयार गर्नुहोस्:
    """
    )

# Example usage:
# final_prompt = constitution_prompt.format(context="Page 20: ...", question="संवैधानिक इजलास के हो?")
# print(final_prompt)
