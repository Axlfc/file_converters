# File Converters

This repository includes an audio file converter application implemented in Python, utilizing the Tkinter library for the graphical user interface and FFmpeg for audio conversion.

## Features

- **Graphical User Interface (GUI):**
  - Simple and interactive GUI for easy navigation.
  - Supports both single-file and batch conversion modes.

- **Audio Conversion:**
  - Converts WAV files to MP3 format using FFmpeg.
  - Choose the desired file extension and output format.

- **Cross-Platform Compatibility:**
  - Instructions for installing FFmpeg on GNU/Linux, Windows, and macOS included in this README.

## Installation

### Installing FFmpeg

#### GNU/Linux

On most GNU/Linux distributions, FFmpeg can be installed using the package manager.

- **Ubuntu/Debian:**
  ```bash
  sudo apt-get update
  sudo apt-get install ffmpeg
  ```
- **Fedora:**
  ```bash
  sudo dnf install ffmpeg
  ```
- **CentOS:**
  ```bash
  sudo yum install ffmpeg
  ```

#### Windows

##### Using winget
```powershell
winget install FFmpeg.FFmpeg
```

##### Using Chocolatey
```powershell
choco install ffmpeg
```

##### Using Binaries
- Visit the [FFmpeg Download page](https://ffmpeg.org/download.html) and download the suitable static build for Windows.
- Extract the downloaded archive, rename the folder to "ffmpeg," and move it to a convenient location like C:\.

##### Setting up PATH Variable
- Add the path to the "bin" folder within the "ffmpeg" directory to the PATH environment variable.
- Open a new PowerShell window to use the ffmpeg command.

#### macOS

Use Homebrew for macOS installation.

1. Install Homebrew:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install FFmpeg:
   ```bash
   brew install ffmpeg
   ```

## Usage

1. **Select File Extension:**
   - Choose the desired file extension for conversion (e.g., WAV).

2. **Select Conversion Mode:**
   - Choose between single-file and batch conversion modes.

3. **Input WAV File:**
   - Specify the input WAV file or folder containing WAV files.

4. **Convert to MP3:**
   - Choose the desired output format for conversion (e.g., MP3).

5. **Output MP3 File/Folder:**
   - Specify the output path for the converted files.

6. **Convert:**
   - Click the "Convert" button to initiate the conversion process.

7. **Progress Bar:**
   - Monitor the progress of the conversion with the progress bar.

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Conclusion

Following the steps outlined in this guide, you should now have FFmpeg successfully installed on your preferred operating system, whether it's GNU/Linux, Windows, or macOS. You can use FFmpeg's powerful features to manipulate audio and video files as needed.

