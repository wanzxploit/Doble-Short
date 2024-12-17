# Doble Short

![Banner](https://raw.githubusercontent.com/wanzxploit/Doble-Short/refs/heads/main/banner.png)

![GitHub stars](https://img.shields.io/github/stars/wanzxploit/Doble-Short?style=social)
![Version](https://img.shields.io/badge/version-1.0-brightgreen)
![Python](https://img.shields.io/badge/python-3.7+-blue)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20termux-lightgrey)



## Description
Doble Short is a command-line tool to shorten links using various services such as Bitly, TinyURL, and Cutt.ly. It allows users to shorten single or multiple URLs with ease and track the status of each shortened link.

## Features
- **Single URL Shortener**: Shorten one link at a time.
- **Multiple URL Shortener**: Process a list of URLs from a file.
- **Supports multiple services**: Bitly, TinyURL, and Cutt.ly.
- **Progress indicators**: Shows progress while shortening links.
- **Output tables**: Neatly displays results with Rich library.
- **User-friendly interface**: Interactive prompts for easy navigation.

## Installation

### Prerequisites
Make sure you have the following installed on your system:
- Python 3.x
- `pip` for installing Python packages
- `make` for handling the installation process

### Steps to Install

1. Clone the repository or download the tool:
    ```bash
    git clone https://github.com/wanzxploit/Doble-Short.git
    cd Doble-Short
    ```

2. Run the installer script to install required dependencies:
    ```bash
    make install
    ```

3. Once the installation is complete, run the tool using the following command:
    ```bash
    make run
    ```

    Or, you can run it directly with Python:
    ```bash
    python3 main.py
    ```

## Usage

Once you run the tool, you will be presented with a menu to choose between:
- **Single Shortener**: Shorten a single URL.
- **Multi Shortener**: Process multiple URLs from a file.
- **Exit**: Close the tool.

### Example Usage:

1. Shorten a single URL:
    ```
    Enter URL: https://example.com
    ```

2. Shorten multiple URLs from a file:
    ```
    Enter file name: links.txt
    ```

## Updating & Upgrading

To keep Doble Short up to date, you can always pull the latest changes from the repository:

```bash
git pull origin master
```

To upgrade dependencies, run the following command:
```bash
make upgrade
```

## Troubleshooting

If you encounter any issues with the installation or usage, feel free to raise an issue on the [GitHub Issues page](https://github.com/wanzxploit/Doble-Short/issues).

## License
This tool is open-source and distributed under the MIT License.
