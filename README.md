# Yt-dlp frontend (Project name pending)

## Overview
Before you start flaming me for this awful readme, im not good at writing these, you can contribute if you'd like.

**yt-dlp frontend** is a frontend (if that wasn't obvious enough) for **yt-dlp**, developed entirely in Python using **Flet**. It is designed to be easy to use and runs completely locally on your system (so you don't have to worry about your favorite downloading site going under all of a sudden).

## Installation:
🚧 There aren't any ready to use installers for Windows/Mac/Linux, so you're required to build this on your own for now

## Getting started (Contribute/Compilation):

### Setup a virtual environment
Setting a virtual environment up on python is pretty easy, just run the following command to create it

`python3 -m venv .venv`

To activate the virtual environment just run the following command (platform dependent)

Windows:
`.venv\Scripts\activate.bat`

Unix:
`source venv/bin/activate`

### Download the Required Dependencies
- [Python](https://python.org)
- [Ffmpeg](https://www.ffmpeg.org/)
- Flet: `pip install flet[all]`
- YT-DLP `pip install yt-dlp`

### Build the project:
Flet thankfully simplified the process so you just have to run 

`flet build (windows/macos/linux)`

# Contributing
You may make pull requests and whatnot, however for any major changes please open up an issue first to discuss said changes.

Be sure to test any changes before pushing!

# To-Do
- [ ] Implement the ability to pick where the file is saved
- [ ] Implement a proper settings page
- [ ] Allow the user to graphically change the file type / video quality / audio quality, etc.

# Authors
- Lead developer: [@nexusvoyager](https://github.com/nexusvoyager)
