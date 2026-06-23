from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(
    text,
    chunk_size=500,
    chunk_overlap=100
):
    """
    Split large text into overlapping chunks
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_text(text)

    return chunks