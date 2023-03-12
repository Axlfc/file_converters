def all_wav_to_mp3():
    pass
    '''bash
        find . -type f -name "*.wav" -exec bash -c 'ffmpeg -i "$0" -codec:a libmp3lame -qscale:a 2 "${0%.wav}.mp3" && rm "$0"' {} \;
    '''
    '''Windows
        Get-ChildItem -Recurse -Filter *.wav | ForEach-Object {
        $newPath = $_.FullName.Replace(".wav", ".mp3")
        ffmpeg -i $_.FullName -codec:a libmp3lame -qscale:a 2 $newPath
        Remove-Item $_.FullName
    }
    '''


def all_mp3_to_wav():
    pass
    '''bash
        find . -type f -name "*.mp3" -exec bash -c 'ffmpeg -i "$0" "${0%.mp3}.wav" && rm "$0"' {} \;
    '''
    '''Windows
        Get-ChildItem -Recurse -Filter *.mp3 | ForEach-Object {
        $newPath = $_.FullName.Replace(".mp3", ".wav")
        ffmpeg -i $_.FullName $newPath
        Remove-Item $_.FullName
    }
    '''


audio_extensions = {
    "WAV": ".wav",
    "MP3": ".mp3",
    "AIFF": ".aiff",
    "FLAC": ".flac",
    "AAC": ".aac",
    "WMA": ".wma",
    "OGG": ".ogg",
    "MIDI": ".midi",
    "AMR": ".amr",
    "CAF": ".caf",
    "AU": ".au",
    "ALAC": ".alac",
    "AC3": ".ac3",
    "DTS": ".dts",
    "RA": ".ra",
    "MP2": ".mp2",
    "AIFC": ".aifc",
    "GSM": ".gsm",
    "WV": ".wv",
    "OPUS": ".opus",
    "M4A": ".m4a",
    "M4R": ".m4r",
    "MMF": ".mmf"
}
