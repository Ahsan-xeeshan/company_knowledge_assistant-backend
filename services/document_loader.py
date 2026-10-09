from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

DOCUMENT_PATH = BASE_DIR/"backend"/"documents"


def chunk_text(text:str):
    paragraphs = [
        paragraph.strip()
        for paragraph in text.split("\n\n")
        if paragraph.strip()
    ]
    return paragraphs

   

def load_documents(): 
    
    all_chunks = []

    print(f"Reading documents from :{DOCUMENT_PATH}")

    for file_path in sorted(DOCUMENT_PATH.glob("*.txt")):
        print(f"Loading: {file_path.name}")

        text = file_path.read_text(
            encoding="utf-8"
        )

        chunks = chunk_text(text)

        for index, chunk in enumerate(chunks):
            all_chunks.append({
                "id":f"{file_path.stem}_{index}",
                "text": chunk,
                "source": file_path.name
            })
    return all_chunks
     