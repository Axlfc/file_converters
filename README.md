# file_converters


# Installing FFmpeg on Different Platforms

FFmpeg is a versatile multimedia framework that allows you to process, convert, and manipulate audio and video files. This guide will walk you through the installation process for FFmpeg on various platforms, including GNU/Linux, Windows, and macOS. It will also cover setting up the PATH variable to ensure easy access to FFmpeg from the command line.

## Table of Contents
1. [GNU/Linux](#gnu-linux)
2. [Windows](#windows)
   - [Using winget](#using-winget)
   - [Using Chocolatey](#using-chocolatey)
   - [Using Binaries](#using-binaries)
   - [Setting up PATH Variable](#setting-up-path-variable)
3. [macOS](#macos)

## GNU/Linux <a name="gnu-linux"></a>
On most GNU/Linux distributions, FFmpeg can be installed using the package manager.

### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```
### Fedora
```bash
sudo dnf install ffmpeg
```

### CentOS
```bash
sudo yum install ffmpeg
```

## Windows <a name="windows"></a>
### Using winget <a name="using-winget"></a>

winget is a built-in package manager for Windows.

```powershell
winget install FFmpeg.FFmpeg
```
### Using Chocolatey <a name="using-chocolatey"></a>

Chocolatey is a popular third-party package manager for Windows.

```powershell
choco install ffmpeg
```
### Using Binaries <a name="using-binaries"></a>

- Visit the FFmpeg Download page and download the suitable static build for Windows.
- Extract the downloaded archive.
- Rename the extracted folder to "ffmpeg" for simplicity.
- Move the "ffmpeg" folder to a location like C:\ for easy access.

### Setting up PATH Variable <a name="setting-up-path-variable"></a>

To make FFmpeg accessible from PowerShell, you need to add its location to the PATH environment variable.

- Open the Start Menu, search for "Environment Variables," and select "Edit the system environment variables."
- Click the "Environment Variables" button.
- In the "System Variables" section, select the "Path" variable and click "Edit."
- Click "New" and add the path to the "bin" folder within the "ffmpeg" directory (e.g., C:\ffmpeg\bin).
- Click "OK" to close the windows.
- Open a new PowerShell window, and you should be able to use the ffmpeg command.

## macOS <a name="macos"></a>

The easiest way to install FFmpeg on macOS is by using the Homebrew package manager.

### Install Homebrew if you haven't already:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
````
### Install FFmpeg using Homebrew:

```bash
brew install ffmpeg
```

## Conclusion

Following the steps outlined in this guide, you should now have FFmpeg successfully installed on your preferred operating system, whether it's GNU/Linux, Windows, or macOS. You can use FFmpeg's powerful features to manipulate audio and video files as needed.
