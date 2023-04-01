# pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
whisper 15GdH9-curt.mp3 --model medium --language ca --output_dir 15GdH9-curt/
cp 15GdH9-curt/15GdH9-curt.txt 15GdH9-curt-openai_whisper-medium.txt
