wav_to_mp3() {
	inputPath="$1"
	if [ ! -f "${inputPath}" ]; then
		echo "Error: Input WAV file not found."
    	return
	fi

    inputFileName="$(basename "$inputPath")"
    outputFileName="${inputFileName%.*}.mp3"
    outputPath="${2:-$(dirname "$inputPath")/$outputFileName}"

    if [ $# -eq 0 ]; then
        echo "ERROR: No arguments provided."
		return
	elif [ $# -eq 1 ]; then
		:
    elif [ $# -eq 2 ]; then
        echo "Two arguments provided: $1 and $2"
		if [[ "$2" == *.mp3 ]]; then
			outputPath="$(dirname "$2")"
			outputFileName="$(basename "$2")"
			echo "OURTOUTPUTPU noseje: ${outputPath}"
        	mkdir -p "$outputPath"
			outputPath="${outputPath}/${outputFileName}"
		elif [ -d "$2" ]; then
			echo "Second argument is a directory"
			if [[ "$2" == */ ]]; then
				outputPath="${outputPath}${outputFileName}"
			else
				outputPath="${outputPath}/${outputFileName}"
			fi
		elif [[ "$2" != *.* ]]; then
            echo "Second argument is a string without extension."
			if [[ "$2" == */ ]]; then
				mkdir -p "./${2%/}"
				outputPath="${outputPath}${outputFileName}"
			else
				mkdir -p "./$2"
				outputPath="${outputPath}/${outputFileName}"
			fi
		fi
    else
        echo "More than two arguments provided."
		return
    fi

	# Convert WAV to MP3 using FFmpeg
    ffmpeg -i "$inputPath" "$outputPath"

    echo "Conversion completed: $inputPath -> $outputPath"
}

batch_wav_to_mp3() {
    local source_dir=""
    local output_dir=""

    if [ $# -eq 0 ]; then
        source_dir="."
        output_dir="./converted_mp3"
    elif [ $# -eq 1 ]; then
        if [ -d "$1" ]; then
            source_dir="$1"
            output_dir="${source_dir}/converted_mp3"
        else
            echo "Invalid argument. Usage: batch_wav_to_mp3 [source_dir] [output_dir]"
            return
        fi
    elif [ $# -eq 2 ]; then
        if [ -d "$1" ]; then
            source_dir="$1"
            output_dir="$2"
        else
            echo "Invalid argument. Usage: batch_wav_to_mp3 [source_dir] [output_dir]"
            return
        fi
    else
        echo "Too many arguments. Usage: batch_wav_to_mp3 [source_dir] [output_dir]"
        return
    fi

    mkdir -p "$output_dir"

    for wav_file in "$source_dir"/*.wav; do
        if [ -f "$wav_file" ]; then
            wav_to_mp3 "$wav_file" "$output_dir"
        fi
    done
}