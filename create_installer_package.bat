@echo off
:: ViGCA Installer Package Creator for Windows 11
:: This script creates a self-contained installer package

setlocal enabledelayedexpansion

:: Set title and colors
title ViGCA Installer Package Creator
color 0A

echo **************************************************************
echo *                                                            *
echo *   ViGCA - Vision-Guided Cursor Automation                  *
echo *   Installer Package Creator                                *
echo *                                                            *
echo **************************************************************
echo.
echo This script will create a standalone installer package for ViGCA.
echo.

:: Check if 7-Zip is installed
where 7z >nul 2>&1
if %errorLevel% NEQ 0 (
    echo ERROR: 7-Zip not found.
    echo.
    echo This script requires 7-Zip to create the installer package.
    echo Please install 7-Zip from: https://7-zip.org/
    echo.
    echo Press any key to exit...
    pause >nul
    exit /b 1
)

echo Creating temporary directory...
if exist "temp_installer" rmdir /s /q "temp_installer"
mkdir "temp_installer"
mkdir "temp_installer\vigca"
mkdir "temp_installer\examples"
mkdir "temp_installer\resources"

echo Copying files...
xcopy /y "vigca\*.py" "temp_installer\vigca\" >nul
xcopy /y "examples\*.py" "temp_installer\examples\" >nul
if exist "resources\*.*" xcopy /y "resources\*.*" "temp_installer\resources\" >nul
copy /y "*.py" "temp_installer\" >nul
copy /y "*.md" "temp_installer\" >nul
copy /y "LICENSE" "temp_installer\" >nul
copy /y "*.txt" "temp_installer\" >nul
copy /y "install_vigca_windows.bat" "temp_installer\" >nul

echo Creating README.txt file with instructions...
echo ViGCA - Vision-Guided Cursor Automation > "temp_installer\README.txt"
echo Windows 11 64-bit Installation Instructions >> "temp_installer\README.txt"
echo. >> "temp_installer\README.txt"
echo 1. Extract all files to a folder of your choice >> "temp_installer\README.txt"
echo 2. Right-click on install_vigca_windows.bat and select "Run as administrator" >> "temp_installer\README.txt"
echo 3. Follow the on-screen instructions to complete installation >> "temp_installer\README.txt"
echo. >> "temp_installer\README.txt"
echo Requirements: >> "temp_installer\README.txt"
echo - Windows 10/11 (64-bit) >> "temp_installer\README.txt"
echo - Python 3.8 or higher >> "temp_installer\README.txt"
echo. >> "temp_installer\README.txt"
echo For more information, see the included README.md file. >> "temp_installer\README.txt"

echo Creating installer package...
7z a -tzip "ViGCA_Windows_Installer.zip" ".\temp_installer\*" -r >nul

echo Cleaning up...
rmdir /s /q "temp_installer"

echo.
echo **************************************************************
echo * Installation package created successfully!                 *
echo * File: ViGCA_Windows_Installer.zip                          *
echo **************************************************************
echo.
echo You can distribute this ZIP file to users. When they extract
echo and run the install_vigca_windows.bat file, ViGCA will be 
echo installed on their system.
echo.
echo Press any key to exit...
pause >nul
exit /b 0