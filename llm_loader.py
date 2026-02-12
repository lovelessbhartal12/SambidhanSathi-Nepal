from langchain_ollama import OllamaLLM
from prompt import create_constitution_prompt  


llm = OllamaLLM(
    model="deepseek-v3.1:671b-cloud",
    temperature=0.0,
    max_length=2048,
)

def ask_constitution_question(context: str, question: str) -> str:
    """
    Use the prompt template + DeepSeek LLM to answer questions
    based on provided context
    """
   
    constitution_prompt = create_constitution_prompt()

    
    prompt_text = constitution_prompt.format(context=context, question=question)

    
    response = llm.generate([prompt_text])  

    
    return response.generations[0][0].text

# if __name__ == "__main__":
#     retrieved_context = """
# Page 7: नागरिकको मौलिक अधिकारहरू: 
# - जीवन र स्वतन्त्रताको अधिकार
# - अभिव्यक्ति र विचारको स्वतन्त्रता
# - धर्म, संस्कृति, र भाषा पालनको अधिकार
# - शिक्षा र स्वास्थ्य सेवा प्राप्त गर्ने अधिकार
# - समानता र गैर-भेदभावको अधिकार
# """

#     user_question = "नेपालको नागरिकको मौलिक अधिकारहरू के-के छन्?"
#     answer = ask_constitution_question(retrieved_context, user_question)
#     print("Answer:\n", answer)
