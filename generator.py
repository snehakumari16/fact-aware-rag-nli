import ollama

def generate_answer(question, context):

    prompt = f"""
    Answer only from the context.

    Context:
    {context}

    Question:
    {question}
    """

    response = ollama.chat(
        model='llama3',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    return response['message']['content']