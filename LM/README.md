# Real-Time Speech-to-Text Transcription System with Language Model Enhancement

This project demonstrates a **Real-Time Speech-to-Text (SRT)** transcription system that leverages the power of **OpenAI's Whisper model** for transcription and integrates **Hugging Face's T5 language model** for grammar correction and enhanced transcription accuracy. The system is designed to accurately transcribe speech in **noisy environments** and correct common language issues to improve overall quality.

## Overview

The **Speech-to-Text Transcription System** utilizes:
- **Whisper** for automatic speech recognition (ASR), which transcribes spoken language into text.
- **T5 (Text-to-Text Transfer Transformer)** to improve the quality of the transcribed text by correcting grammar and enhancing clarity.

By integrating these technologies, the system helps achieve better transcription results, especially in challenging audio conditions (e.g., noisy background, varied accents). This makes it suitable for real-time applications like virtual assistants, transcription services, and customer support automation.

## Technologies Used

- **Whisper**: OpenAI's speech-to-text model, which accurately transcribes audio input into text, even in noisy environments or with varied accents.
- **T5 (Text-to-Text Transfer Transformer)**: Hugging Face’s pre-trained language model used to enhance transcriptions by correcting grammatical errors and improving clarity.
- **Python 3.7+**: The programming language used to implement the system.
- **Hugging Face Transformers**: A library to load and interact with pre-trained models like T5.
- **Torch**: A deep learning framework required for model inference with the Whisper and T5 models.

## Prerequisites

- **Python 3.7 or higher**
- **Pip** (Python package installer)

### Libraries:
- `whisper` – OpenAI’s Whisper model for speech-to-text transcription.
- `transformers` – Hugging Face's library to load and use language models like T5.
- `torch` – PyTorch for model execution.

## Installation

To get started, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/speech-to-text-transcription.git
   cd speech-to-text-transcription
## Usage

1. **Prepare your audio file**:  
   Ensure the audio file you want to transcribe is available in `.wav` format.

2. **Run the script**:  
   Execute the following command in the terminal:

   ```bash
   python Main.py
