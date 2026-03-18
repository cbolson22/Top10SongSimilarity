# Top 10 Song Similarity Analysis

[**View the Project Website**](https://cbolson22.github.io/Top10SongSimilarity/)

## Purpose
This project investigates the evolution of popular music by analyzing the similarity of Billboard Top Charts hits across seven decades (1950s–2010s). By extracting and comparing audio features such as tempo, energy, and structural complexity, we aim to uncover trends that define how "pop" music has changed over time.

---

## Repository Contents

- **`analysis_pipeline_example.ipynb`**: The primary workflow for extracting audio features (using `librosa` and `msaf`) and computing similarity metrics between songs.
- **`decade_comparison.ipynb`**: Detailed comparative analysis and visualization of trends across different decades.
- **`docs/`**: Contains the source for the project's [web dashboard](https://cbolson22.github.io/Top10SongSimilarity/), including interactive plots and findings.
- **`MSD_test_files/`**: Old files and logic for matching Billboard chart data with a Million Song Dataset (MSD) subset.
  - `merged.csv`: The resulting dataset of Billboard hits found within the MSD.
  - `build_billboard_table.py` & `build_subset_table.py`: Scripts for data cleaning and integration.
- **`decade_top_20/`**: Historical Billboard Hot 100 data (`charts.csv`) and processed rankings for analysis.

---

## Getting Started

### 1. Environment Setup
Ensure you have Python 3.10+ installed. It is recommended to use a virtual environment:

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Running the Analysis
The project relies on Jupyter notebooks for the analysis pipeline:

1. Open `analysis_pipeline_example.ipynb` to see how audio features are extracted from the `song_mp3/` directory (which you will need to populate with audio samples).
2. Use `decade_comparison.ipynb` to generate the trend visualizations found in the `docs/plots/` folder.
3. If you wish to rebuild the Million Song Dataset subset integration, navigate to `MSD_test_files/` and run the `build_*.py` scripts.

---

## Methodology Note
This analysis uses a combination of the Billboard Hot 100 historical dataset (via Kaggle) and local MP3 samples downloaded from YouTube.