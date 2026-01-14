from utils.save_to_document import save_document
import os

def test_local_pdf():
    print("Testing save_document locally...")
    sample_text = """
    # Day 1: London
    
    ## Morning
    Visit the British Museum.
    
    ## Afternoon
    Walk around Covent Garden.
    """
    
    output_file = save_document(sample_text)
    
    if output_file and os.path.exists(output_file) and output_file.endswith(".pdf"):
        print(f"SUCCESS: PDF created at {output_file}")
    else:
        print(f"FAILURE: File not created properly: {output_file}")

if __name__ == "__main__":
    test_local_pdf()
