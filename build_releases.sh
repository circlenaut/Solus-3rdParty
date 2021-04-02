#!/bin/bash

## Microsoft Edge Dev:
sudo rm /usr/share/pixmaps/microsoft-edge-dev.png
sudo eopkg bi --ignore-safety ./browser/microsoft-edge-dev/pspec.xml && mv microsoft-edge-dev*.eopkg ./releases/

## Figma Linux:
sudo eopkg bi --ignore-safety ./graphics/figma-linux/pspec.xml && mv figma-linux*.eopkg ./releases/

## 1Password:
sudo eopkg bi --ignore-safety ./security/1password/pspec.xml && mv 1password*.eopkg ./releases/

## Everdo:
sudo eopkg bi --ignore-safety ./productivity/everdo/pspec.xml && mv everdo*.eopkg ./releases/

## MineTime:
sudo eopkg bi --ignore-safety ./productivity/minetime/pspec.xml && mv minetime*.eopkg ./releases/

## Microsoft Teams:
sudo eopkg bi --ignore-safety ./productivity/microsoft-teams/pspec.xml && mv microsoft-teams*.eopkg ./releases/

## p3xOnenote:
sudo eopkg bi --ignore-safety ./productivity/p3x-onenote/pspec.xml && mv p3x-onenote*.eopkg ./releases/

## p3xOnenote:
sudo eopkg bi --ignore-safety ./productivity/p3x-onenote/pspec.xml && mv p3x-onenote*.eopkg ./releases/
sudo eopkg bi --ignore-safety ./browser/downloadhelper/pspec.xml && mv video-download-helper-companion*.eopkg ./releases/ 

## Update file ownership
sudo chown $USER: ./releases/*