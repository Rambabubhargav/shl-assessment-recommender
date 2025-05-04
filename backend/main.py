from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

with open("product_catalog.json", "r") as f:
    catalog = json.load(f)

@app.get("/recommend")
def recommend(role: str = Query(...)):
    role = role.lower()
    results = []
    for item in catalog:
        score = sum(1 for tag in item["roles"] if role in tag)
        if score > 0:
            item["score"] = score
            results.append(item)
    return sorted(results, key=lambda x: x["score"], reverse=True)
