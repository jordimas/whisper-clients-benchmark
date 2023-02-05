#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2023 Jordi Mas i Hernandez <jmas@softcatala.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import os
import datetime
from evaluate import load
import sys

def score(name, reference_file, prediction_file):

    with open(reference_file) as f:
        reference = f.read()

    with open(prediction_file) as f:
        prediction = f.read()
    
    # This is a very naive way to calculate WER, there is normalisation like
    # it's done in the orginal Whisper paper since the main goal here is
    # to check for regressions
    _wer = load("wer")
    wer_score = _wer.compute(predictions=[prediction], references=[reference])
    wer_score = wer_score * 100
    print(f"{name} - {prediction_file}. WER: {wer_score}")
    
def main():
    print("Benchmark whisper.cpp inference")
    score("OpenAI whisper", "15GdH9-curt.txt", "15GdH9-curt/15GdH9-curt.mp3.txt")
    score("Whisper.cpp", "15GdH9-curt.txt", "15GdH9-curt.wav.txt")
    
if __name__ == "__main__":
    main()
