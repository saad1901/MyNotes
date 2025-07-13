# Docker Installation

## Prerequisites
- 64-bit operating system
- Virtualization enabled in BIOS
- Administrative privileges

## Installation on Windows
1. Download Docker Desktop from the [official website](https://www.docker.com/products/docker-desktop/).
2. Run the installer and follow the prompts.
3. After installation, launch Docker Desktop.
4. Verify installation by running `docker --version` in PowerShell.

## Installation on macOS
1. Download Docker Desktop for Mac from the [official website](https://www.docker.com/products/docker-desktop/).
2. Open the downloaded `.dmg` file and drag Docker to Applications.
3. Launch Docker Desktop.
4. Verify installation by running `docker --version` in Terminal.

## Installation on Linux (Ubuntu Example)
1. Update existing packages: `sudo apt update`
2. Install prerequisites: `sudo apt install apt-transport-https ca-certificates curl software-properties-common`
3. Add Docker’s GPG key: `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
4. Add Docker repository:
   ```
   sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
   ```
5. Install Docker Engine: `sudo apt update && sudo apt install docker-ce`
6. Verify installation: `docker --version`

## Post-Installation Steps
- Add your user to the `docker` group to run Docker without `sudo`:
  `sudo usermod -aG docker $USER`
- Restart your system or log out and back in. 