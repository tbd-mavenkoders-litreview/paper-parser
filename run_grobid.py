import os
import subprocess
from pathlib import Path

# --- Configuration ---
# ⚠️ ACTION REQUIRED: Verify this is the correct path to your 'data' directory
INPUT_ROOT = Path("/workspace/home/aiclub1/B220032CS_Jaefar/fyp/research-scraper/data")

# ⚠️ ACTION REQUIRED: Verify this is where you want to save the processed files
OUTPUT_ROOT = Path("/workspace/home/aiclub1/B220032CS_Jaefar/fyp/research-scraper/processed_data")

# Path to your config file (should be in the same directory as this script)
CONFIG_PATH = "./config.json"

# Number of concurrent processes, as requested
CONCURRENCY = 24
# --- End Configuration ---

def main():
    """
    Finds all 'papers' directories and processes their contents using the grobid_client.
    """
    print(f"🚀 Starting GROBID processing with {CONCURRENCY} concurrent workers...")
    print(f"Input root: {INPUT_ROOT}")
    print(f"Output root: {OUTPUT_ROOT}\n")

    # This line specifically finds all directories named 'papers'
    paper_dirs = list(INPUT_ROOT.rglob('papers'))

    if not paper_dirs:
        print("Error: No 'papers' directories found. Please check your INPUT_ROOT path.")
        return

    for i, input_dir in enumerate(paper_dirs, 1):
        # Create a corresponding output path that mirrors the input structure
        relative_path = input_dir.relative_to(INPUT_ROOT)
        output_dir = OUTPUT_ROOT / relative_path.parent / "processed"

        # Ensure the output directory exists
        output_dir.mkdir(parents=True, exist_ok=True)

        print(f"--- ({i}/{len(paper_dirs)}) ---")
        print(f"-> Processing: {input_dir}")
        print(f"   Output to:  {output_dir}")

        # Construct the command to run
        command = [
            "grobid_client",
            "--input", str(input_dir),
            "--output", str(output_dir),
            "--config", CONFIG_PATH,
            "--n", str(CONCURRENCY),
            "--force",
            "processFulltextDocument"
        ]

        # Execute the command
        try:
            subprocess.run(command, check=True, text=True)
            print(f"✅ Success: Completed processing for {relative_path.parent.name}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error processing {input_dir}:")
            print(f"   Stderr: {e.stderr.strip()}")
        except FileNotFoundError:
            print("\nError: 'grobid_client' command not found.")
            print("Please ensure 'grobid-client-python' is installed and in your system's PATH.")
            return

    print("\n🎉 All directories processed successfully!")

if __name__ == "__main__":
    main()
