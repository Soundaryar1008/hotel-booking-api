from fastapi import FastAPI
import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

app = FastAPI()

# Load dataset (Only Once)
file_path = "cleaned_hotel_bookings.csv"  
df = pd.read_csv(file_path)

# Prepare text data for embeddings
df['text_data'] = df.apply(lambda row: f"Booking from {row['country']}, revenue {row['adr']}, lead time {row['lead_time']} days", axis=1)

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Convert text data into embeddings
embeddings = model.encode(df['text_data'].tolist(), show_progress_bar=True)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

@app.get("/")
def read_root():
    return {"message": "Booking Analytics & Q&A API is running!"}

# 🔹 Q&A API with FAISS
@app.get("/ask")
def ask_question(query: str, top_k: int = 5):
    query_embedding = model.encode([query])
    
    # Ensure `top_k` is within bounds
    num_records = len(df)
    top_k = min(top_k, num_records)
    
    distances, indices = index.search(np.array(query_embedding), top_k)
    results = [df.iloc[idx]['text_data'] for idx in indices[0] if idx < num_records]
    
    return {"query": query, "results": results}

# 🔹 Revenue Trends API
@app.get("/revenue-trends")
def get_revenue_trends():
    revenue_data = df.groupby(["arrival_date_year", "arrival_date_month"])["adr"].sum().reset_index()
    revenue_data.columns = ["year", "month", "total_revenue"]
    return revenue_data.to_dict(orient="records")

# 🔹 Bookings by Country API
@app.get("/bookings-by-country")
def get_bookings_by_country():
    country_counts = df["country"].value_counts().reset_index()
    country_counts.columns = ["country", "num_bookings"]
    return country_counts.to_dict(orient="records")

# 🔹 Lead Time Stats API
@app.get("/lead-time-stats")
def get_lead_time_stats():
    return {
        "average_lead_time": float(df["lead_time"].mean()),
        "max_lead_time": int(df["lead_time"].max()),
        "min_lead_time": int(df["lead_time"].min())
    }

# 🔹 Cancellation Rate API
@app.get("/cancellation-rate")
def get_cancellation_rate():
    cancel_rate = df['is_canceled'].value_counts(normalize=True) * 100
    return {"cancellation_rate": cancel_rate.to_dict()}

# Run API using: uvicorn app:app --reload
