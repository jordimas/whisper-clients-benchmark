filename=15GdH9-curt.mp3
python3 hf-transcribe.py $filename --model_id openai/whisper-medium --language ca
mv $filename.txt hf/medium/
