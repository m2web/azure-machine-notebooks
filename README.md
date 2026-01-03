# 🎸 Azure AI-102: The Spirit of Artificial Intelligence

## Study Labs & Notebooks (Rush Edition)

This repository contains my study materials, Jupyter Notebooks, and data assets for the **Microsoft Azure AI-102 (Azure AI Engineer Associate)** exam. To make the learning process more engaging, I have themed the datasets, prompts, and analysis around the discography, lyrics, and history of the band **Rush**.

> "All this machinery making modern music can still be open-hearted." — *The Spirit of Radio*

---

## 🚀 Overview

This project demonstrates the implementation of Azure AI Services using Python and Jupyter Notebooks. It covers the core pillars of the AI-102 exam while analyzing the "Working Man's" approach to Artificial Intelligence learning.

## 🛠️ Tech Stack

- **Platform:** Azure Machine Learning (Compute Instance)
- **Language:** Python
- **Services:** Azure AI Services (Vision, Speech, Language, Document Intelligence, Search)
- **Format:** `.ipynb`, `.jsonl` (for fine-tuning/training), and `.png` (for vision tasks)

---

## 🎼 Featured Labs (The Rush Portfolio)

### 1. 👁️ Computer Vision: "The Camera Eye"

- **Objective:** Image classification and object detection.
- **Rush Twist:** Using `.png` files to identify iconic album covers (*Moving Pictures*, *2112*, *Signals*) and detecting Neil Peart's drum kit components in concert photos.

### 2. ✍️ Natural Language Processing: "The Pass"

- **Objective:** Sentiment analysis, entity recognition, and summarization.
- **Rush Twist:** Analyzing the lyrical depth of Peart's songwriting to determine emotional sentiment across different decades (70s Sci-Fi vs. 80s Synth vs. 90s Alt-Rock).

### 3. 🤖 Language Modeling: "Cygnus X-1"

- **Objective:** Fine-tuning and prompt engineering using `.jsonl` files.
- **Rush Twist:** Training models on interview transcripts to generate responses in the "voice" of Geddy Lee or Alex Lifeson.

### 4. 🔍 Knowledge Mining: "Finding My Way"

- **Objective:** Implementing Azure AI Search.
- **Rush Twist:** Indexing a library of JSONL files containing setlists and tour dates to create a searchable "Rush Encyclopedia."

---

### 5. 🧠 Advanced Vision & Embeddings: "Signals and Echoes"

- **Objective:** Explore the unified Vision APIs and embeddings for image understanding and multimodal retrieval.
- **Rush Twist:** Create embeddings from album art and lyric snippets to enable cross-modal search between images and text using the unified API showcased in `AdvancedImageAnalysisUnifiedAPIAndEmbeddings.ipynb`.

### 6. 🔎 OCR & Document Analysis: "Words in Motion"

- **Objective:** Optical Character Recognition and document feature extraction.
- **Rush Twist:** Extract and index lyrical transcriptions and scanned setlists from tour PDFs and images to enrich the search index — experiments live in `OCRLab.ipynb`.

## 📂 File Structure

This repository currently uses a flat structure with all notebooks and data files at the root level:

- **Azure AI Search Labs:**
  - `azure-ai-search-setup.ipynb` - Initial Azure AI Search configuration
  - `azure-ai-search-integrated.ipynb` - Integrated search implementation
  - `azure-ai-search-test.ipynb` - Testing and validation
  - `6.1CreatingTheSkillset.ipynb` - Custom skillset creation
  - `6.2CreatingTheIndexer.ipynb` - Indexer configuration
  - `7.1TestQuery.ipynb` - Query testing
  - `7.2HybridSearch.ipynb` - Hybrid search implementation
  - `CreatingDataSourceConnection.ipynb` - Data source connectivity

- **Azure AI Language Services:**
  - `AzureAILanguageTextSummarization.ipynb` - Text summarization demos
  - `TextAnalyticsSentimentAnalysisPII.ipynb` - Sentiment analysis and PII detection
  - `translate.ipynb` - Translation services

- **Azure AI Vision & Generative AI:**
  - `AzureAIVisionImageCaptioningAndAnalysis.ipynb` - Image analysis and captioning
  - `AdvancedImageAnalysisUnifiedAPIAndEmbeddings.ipynb` - Advanced unified Vision + Embeddings examples
  - `Create-image-dalle-3.ipynb` - DALL-E 3 image generation

- **Model Testing & Deployment:**
  - `DeekSeekFavRushAlbum.ipynb` - Custom model testing (Rush-themed!)
  - `Phi-4-model-params.ipynb` - Model parameter exploration
  - `web-app-deploy.ipynb` - Web application deployment

- **Data Assets:**
  - `rush_lyrics_for_indexing.jsonl` - Rush lyrics dataset for search indexing
  - `rush_lyrics_for_indexing-old.jsonl` - Previous version of lyrics dataset
  - `rush_lyrics/XanaduHandwritten.png` - Handwritten lyric image for OCR experiments
  - `rush_lyrics/XanaduHandwritten_transcript.txt` - Saved OCR transcript from `OCRLab.ipynb`

- **Additional Labs:**
  - `OCRLab.ipynb` - Optical Character Recognition experiments and demos
    - Produces a transcript at `rush_lyrics/XanaduHandwritten_transcript.txt` when run

---

## ⚡ Setup Instructions

1. Clone this repo to your Azure ML Compute Instance.
2. Install the Azure AI SDK:

```bash
pip install azure-ai-textanalytics azure-cognitiveservices-vision-computervision
```

1. Create an `.env` file with your `AZURE_AI_ENDPOINT` and `AZURE_AI_KEY`.
2. Run the notebooks to explore the intersection of Prog-Rock and AI.
