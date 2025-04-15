# ViGCA v0.1.0 Release Notes

## Overview

ViGCA (Vision-Guided Cursor Automation) is an AI-powered application that watches your screen, learns visual targets, and automatically moves your mouse cursor to those targets when they appear. This initial release provides the core functionality and a clean, modern Windows 11 user interface.

## Features

- **Screen Monitoring**: Continuously monitors your screen for visual targets
- **Target Learning**: Easily create and manage visual targets by selecting regions on your screen
- **Smart Detection**: Uses computer vision algorithms to accurately identify targets even with slight variations
- **Automated Cursor Control**: Precisely moves the cursor to detected targets
- **Modern Windows UI**: Clean, modern interface optimized for Windows 11
- **Multiple Detection Methods**: Choose between template matching and feature-based matching
- **Configurability**: Customize detection rate, confidence thresholds, cursor movement, and more
- **Programmable API**: Use the core functionality in your own Python scripts

## Installation

### Windows 11 (64-bit)

1. **Download** the release ZIP file
2. **Extract** all files to a folder of your choice
3. **Right-click** on `install_vigca_windows.bat` and select "Run as administrator"
4. **Follow** the on-screen instructions to complete the installation

## System Requirements

- Windows 10/11 (64-bit)
- Python 3.8 or higher
- Screen resolution of 1280x720 or higher (recommended)

## Known Issues

- The application may experience performance issues on systems with limited resources when using feature-based matching.
- Some high-DPI displays may show scaling issues with the user interface.
- CPU usage can be high during continuous detection with high capture rates.

## Upcoming Features (Planned)

- Cloud synchronization for targets across devices
- Advanced pattern recognition with deep learning
- Scheduled automation routines
- Multi-monitor support
- Recording and playback of cursor sequences

## Acknowledgments

- OpenCV for computer vision capabilities
- PyAutoGUI for cursor control
- MSS for fast screen capture
- CustomTkinter for the modern UI elements

## Contact & Support

- GitHub Issues: [Report bugs or request features](https://github.com/your-username/vigca/issues)
- Email: your.email@example.com

---

Thank you for using ViGCA! We hope it helps automate repetitive tasks and makes your computer interaction more efficient.