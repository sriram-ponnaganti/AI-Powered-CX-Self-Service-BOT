import pandas as pd
from sentence_transformers import SentenceTransformer, util
import torch

# 1. Load your Consumer Electronics dataset
df = pd.read_csv('faqs.csv')

# 2. Load a pre-trained VXI-appropriate model 
# 'all-MiniLM-L6-v2' is fast and lightweight, perfect for real-time BPO support
model = SentenceTransformer('all-MiniLM-L6-v2')

# 3. Convert all FAQ questions into numerical embeddings
print("Encoding FAQs... please wait.")
faq_embeddings = model.encode(df['question'].tolist(), convert_to_tensor=True)

def get_best_match(user_query):
    # Convert user query into an embedding
    query_embedding = model.encode(user_query, convert_to_tensor=True)
    
    # Calculate similarity between query and all FAQs
    # Using cosine similarity to find the 'closest' meaning
    cosine_scores = util.cos_sim(query_embedding, faq_embeddings)
    
    # Find the index of the highest score
    best_match_idx = torch.argmax(cosine_scores).item()
    best_score = cosine_scores[0][best_match_idx].item()
    
    return best_match_idx, best_score

# Test the engine
query = "My mobile is acting up, how do I wipe it?"
idx, score = get_best_match(query)

print(f"\nUser Query: {query}")
print(f"Matched FAQ: {df.iloc[idx]['question']}")
print(f"Bot Answer: {df.iloc[idx]['answer']}")
print(f"Confidence Score: {score:.4f}")