def verify_answer(context, answer):
    """
    Simple verification that checks if answer contains context keywords
    """
    context_words = set(context.lower().split())
    answer_words = set(answer.lower().split())
    
    # Find overlapping words
    common_words = context_words.intersection(answer_words)
    
    # Calculate similarity score
    if len(context_words) == 0:
        similarity = 0
    else:
        similarity = len(common_words) / len(context_words)
    
    # Return verification result
    return {
        "similarity_score": round(similarity, 2),
        "overlapping_words": list(common_words)[:10],
        "verification": "PASSED" if similarity > 0.2 else "LOW_MATCH"
    }