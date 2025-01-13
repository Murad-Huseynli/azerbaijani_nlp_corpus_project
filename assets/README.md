# Azerbaijani News Text Processing and Analysis
## About The Project
This research project focuses on developing and implementing various NLP techniques for processing and analyzing Azerbaijani news text from Telegram channels. The project includes text tokenization, sentence segmentation, spelling correction, and statistical analysis using Heaps Law. The goal is to create a foundation for generating synthetic news content through AI.

### Key Findings
* Implemented Heaps Law analysis with coefficients k = 0.0009 and b = 1.8585
* Developed weighted Levenshtein distance algorithm for improved spelling correction
* Successfully handled special cases in tokenization like compound names (e.g., "Ilham Aliyev")
* Created confusion matrix for spelling error analysis

### Built With
* Python
* Regular expressions for basic tokenization
* Byte Pair Encoding (BPE) for compound word handling
* Custom implementation of Levenshtein distance algorithm

## Getting Started
### Prerequisites
* Python environment
* Telegram chat export functionality
* JSON processing capabilities

### Dataset Structure
The project uses text data from three main Azerbaijani news sources:
* SputnikAz
* APA
* DIM

## Usage
The project includes several key components:

1. `text_from_json_tg.py`: Extracts text from Telegram JSON exports
2. `simple_tokenizer.py`: Basic tokenization using regex
3. `sentence_tokenizer.py`: Sentence segmentation implementation
4. `bpe.py`: Byte Pair Encoding for compound word handling
5. `spelling_checker.py`: Basic Levenshtein distance implementation
6. `weight_spelling_checker.py`: Enhanced spelling correction with weighted distance
7. `heaps_law.py`: Statistical analysis of vocabulary growth

## Implementation Details
### Text Processing Pipeline:
1. Data collection from Telegram channels
2. Basic tokenization with URL removal
3. Compound word handling using BPE
4. Sentence segmentation
5. Spelling correction using weighted Levenshtein distance

## Roadmap
- [x] Basic tokenization implementation
- [x] Heaps Law analysis
- [x] BPE implementation
- [x] Basic spelling checker
- [x] Weighted spelling checker
- [ ] Improve sentence segmentation
- [ ] Implement more advanced tokenization methods
- [ ] Add support for more Azerbaijani language features

## License
Research project conducted at ADA University, School of Information Technologies and Engineering and distributed under the MIT License. See `LICENSE` for more information.


