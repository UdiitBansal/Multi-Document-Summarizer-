from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os

from pdf_utils import extract_text
from chunker import chunk_text
from embedding import (
    generate_embeddings,
    store_chunks,
    search_chunks
)
from summarizer import summarize_text
from analyzer import analyze_summary

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {"message": "Backend Running"}


@app.post("/analyze")
async def analyze_pdf(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text(file_path)

    chunks = chunk_text(text)

    embeddings = generate_embeddings(chunks)

    store_chunks(
        chunks,
        embeddings
    )

    summary = summarize_text(text)

    analysis = analyze_summary(summary)

    return {
    "summary": summary,
    "themes": analysis["themes"],
    "findings": analysis["findings"],
    "insights": analysis["insights"],
    "contradictions": analysis["contradictions"],
    "conclusion": analysis["conclusion"]
}