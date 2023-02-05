#cp ../transcribe-service/whisper.cpp/main .
#cp /home/jordi/sc/transcribe/transcribe-service/whisper.cpp/sc-models/* models
ffmpeg -i 15GdH9-curt.mp3 -ar 16000 -ac 1 -c:a pcm_s16le 15GdH9-curt.wav -y
./main  --threads 14  -m models/ggml-medium.bin -f 15GdH9-curt.wav -l ca -otxt  -osrt

