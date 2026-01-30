# Paper Parser - GROBID Processing

A Python utility for batch processing academic PDF documents using [GROBID](https://github.com/kermitt2/grobid) to extract structured content (TEI XML).

## Overview

This tool automates the extraction of structured data from research papers by:
- Recursively finding all `papers` directories in your input path
- Processing PDFs using GROBID's `processFulltextDocument` service
- Outputting structured TEI XML files

## Prerequisites

- Python 3.7+
- Running GROBID server (default: `http://localhost:8070`)
- `grobid-client-python` installed

```bash
pip install grobid-client-python
```

## Configuration

### config.json
```json
{
    "grobid_server": "http://localhost:8070",
    "batch_size": 1000,
    "sleep_time": 5,
    "timeout": 600,
    "coordinates": ["persName", "figure", "ref", "biblStruct", "formula", "s"]
}
```

### run_grobid.py
Edit the following paths in `run_grobid.py`:
- `INPUT_ROOT`: Path to your data directory containing `papers` folders
- `OUTPUT_ROOT`: Path where processed XML files will be saved
- `CONCURRENCY`: Number of parallel workers (default: 24)

## Usage

1. Start your GROBID server
2. Configure paths in `run_grobid.py`
3. Run:

```bash
python run_grobid.py
```

## Directory Structure

```
grobid0/
├── config.json          # GROBID client configuration
├── grobid.yaml          # Full GROBID server configuration
├── light/
│   └── grobid.yaml      # Lightweight GROBID configuration
└── run_grobid.py        # Main processing script
```

## Output

Processed files are saved as TEI XML in the corresponding `processed/` subdirectory mirroring your input structure.

## License

MIT
