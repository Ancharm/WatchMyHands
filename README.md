# <ins>Watch</ins> My Hands - Empowering the community

Welcome to the documentation for our computer vision-based watch that can convert American Sign Language (ASL) to English and vice versa. This watch uses machine learning algorithms and computer vision techniques to interpret and translate sign language in real-time.

Table of Contents:

    - Overview
    - Requirements
    - Installation
    - Usage
    - Contributing
    - License

## Overview

Our watch is a wearable device that has a desktop camera and LCD screen to display the translated text. The machine learning model used in this watch has been trained on a large dataset of ASL alphabet and corresponding English translations.

## Requirements

To use our watch, you will need the following requirements:

    A Raspberry Pi 3B+ with a webcam (we are using the Raspberry Pi Camera v2.1)
    A miniature LCD display HAT (we are using the waveshare 1.3" LCD HAT with buttons)
    A power supply module (we are using the RPi UPS PowerPack with a 3.7V Li-polymer Battery)

## Installation

To install the watch software, follow the steps below:

    Clone the repository from Github: git clone https://github.com/Ancharm/WatchMyHands.git
    Navigate to the 1.3inch_LCD_HAT_code/1.3inch_LCD_HAT_code/python path
    Run the main program: sudo python main.py [An additional button test program can be run with sudo python key_demo.py]

## Usage

Using our watch is simple and easy. To use it, follow the steps below:

    Wear the watch on your wrist and power the pi
    Point the camera towards the person signing
    The watch will automatically recognize the signs and display the corresponding text on the screen
    To translate from English to ASL, toggle to recognition mode to convert voice to text and display it on the screen
  
