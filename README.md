# Android to PC File Copy Script

This script copies files from an Android device connected via USB to a specified folder on your PC.

## Prerequisites

1. Python 3.x
2. ADB (Android Debug Bridge)

## Setup

### Step 1: Install ADB

1. **Download ADB**:
   - Download the platform tools from the [Android developer website](https://developer.android.com/studio/releases/platform-tools).
   - Extract the downloaded zip file to a location of your choice (e.g., `C:\adb`).

2. **Add ADB to your system PATH**:
   - Open the Start Search, type in "env", and select "Edit the system environment variables".
   - In the System Properties window, click on the "Environment Variables" button.
   - In the Environment Variables window, under "System variables", find the `Path` variable, select it, and click "Edit".
   - Click "New" and add the path to the `platform-tools` directory (e.g., `C:\adb`).
   - Click "OK" to close all dialog boxes.

### Step 2: Enable USB Debugging on Your Android Device

1. Go to `Settings` > `About phone`.
2. Tap `Build number` seven times to unlock developer options.
3. Go to `Settings` > `System` > `Developer options`.
4. Enable `USB debugging`.

### Step 3: Verify ADB Connection

1. Connect your Android device to your computer using a USB cable.
2. Open a command prompt and run:
   ```sh
   adb devices