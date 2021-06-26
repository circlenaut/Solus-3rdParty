#!/bin/bash

RELEASE_DIR="./releases"
if ! [ -d "$RELEASE_DIR" ]; then
    echo "Creating directory '${RELEASE_DIR}' ..."
    mkdir $RELEASE_DIR
fi

## Microsoft Visual Studio Code:
sudo eopkg bi --ignore-safety ./productivity/visual-studio-code/pspec.xml \
&& cp vscode-microsoft*.eopkg ./releases/vscode-microsoft-latest.eopkg \
&& mv -f vscode-microsoft*.eopkg ./releases/

## Microsoft Edge Dev:
sudo rm /usr/share/pixmaps/microsoft-edge-dev.png
sudo eopkg bi --ignore-safety ./browser/microsoft-edge-dev/pspec.xml \
&& cp microsoft-edge-dev*.eopkg ./releases/microsoft-edge-dev-latest.eopkg \
&& mv -f microsoft-edge-dev*.eopkg ./releases/

## Figma Linux:
sudo eopkg bi --ignore-safety ./graphics/figma-linux/pspec.xml \
&& cp figma-linux*.eopkg ./releases/figma-linux-latest.eopkg \
&& mv -f figma-linux*.eopkg ./releases/

## 1Password:
sudo eopkg bi --ignore-safety ./security/1password/pspec.xml \
&& cp 1password*.eopkg ./releases/1password-latest.eopkg \
&& mv -f 1password*.eopkg ./releases/

## Everdo:
sudo eopkg bi --ignore-safety ./productivity/everdo/pspec.xml \
&& cp everdo*.eopkg ./releases/everdo-latest.eopkg \
&& mv -f everdo*.eopkg ./releases/

## Morgen:
sudo eopkg bi --ignore-safety ./productivity/morgen/pspec.xml \
&& cp morgen*.eopkg ./releases/morgen-latest.eopkg \
&& mv -f morgen*.eopkg ./releases/

## Microsoft Teams:
sudo eopkg bi --ignore-safety ./productivity/microsoft-teams/pspec.xml \
&& cp microsoft-teams*.eopkg ./releases/microsoft-teams-latest.eopkg \
&& mv -f microsoft-teams*.eopkg ./releases/

## p3xOnenote:
sudo eopkg bi --ignore-safety ./productivity/p3x-onenote/pspec.xml \
&& cp p3x-onenote*.eopkg ./releases/p3x-onenote-latest.eopkg \
&& mv -f p3x-onenote*.eopkg ./releases/

## Download Helper:
sudo eopkg bi --ignore-safety ./browser/downloadhelper/pspec.xml \
&& cp video-download-helper-companion*.eopkg ./releases/video-download-helper-companion-latest.eopkg \
&& mv -f video-download-helper-companion*.eopkg ./releases/

## Lightworks:
sudo eopkg bi --ignore-safety ./graphics/lightworks/pspec.xml \
&& cp lightworks*.eopkg ./releases/lightworks-latest.eopkg \
&& mv -f lightworks*.eopkg ./releases/

## Update file ownership
sudo chown $USER: ./releases/*