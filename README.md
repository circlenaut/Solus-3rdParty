# 3rdParty Packages for Solus

# Archived
I am no longer willing to maintain the packages to the latest version as I no longer use them.  
You can use this as the template of your repo and maintain if you want.

## Disclaimer
These packages are **not official**, they are neither supported nor endorsed by the official Solus devs. Do not ask for help in Solus's help forum, instead create an issue [here](https://github.com/prateekmedia/Solus-3rdParty/issues).

## Direct .eopkg files(NEW)
Now you can directly download the compiled .eopkg files from [here](https://github.com/prateekmedia/Solus-3rdParty/releases/latest)

To install any program directly from eopkg file, First download the file and then `cd` into that folder like `$ cd ~/Downloads`, After that run  
```
$ sudo eopkg it ./your-program-name.eopkg
```
**NOTE** : Please read the release notes first to know if their are any extra dependencies or not

### Building from Source

**For Microsoft Edge Dev:**  
```
$ sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/prateekmedia/Solus-3rdParty/main/browser/microsoft-edge-dev/pspec.xml && sudo eopkg it microsoft-edge-dev*.eopkg && sudo rm microsoft-edge-dev*.eopkg
```
**For Figma Linux:**  
```
$ sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/prateekmedia/Solus-3rdParty/main/graphics/figma-linux/pspec.xml && sudo eopkg it figma-linux*.eopkg && sudo rm figma-linux*.eopkg
```
**For Magnus:**  
```
$ sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/prateekmedia/Solus-3rdParty/main/graphics/magnus/pspec.xml && sudo eopkg it magnus*.eopkg && sudo rm magnus*.eopkg
```
**For 1Password:**  
```
$ sudo eopkg bi --ignore-safety ./security/1password/pspec.xml && sudo eopkg it 1password*.eopkg && sudo rm 1password*.eopkg
```
releases: https://downloads.1password.com/linux/debian/pool/main/1/1password/1password-8.0.30.deb
**For Everdo:**  
```
$ sudo eopkg bi --ignore-safety ./productivity/everdo/pspec.xml && sudo eopkg it everdo*.eopkg && sudo rm everdo*.eopkg
```
**For MineTime:**  
```
$ sudo eopkg bi --ignore-safety ./productivity/minetime/pspec.xml && sudo eopkg it minetime*.eopkg && sudo rm minetime*.eopkg
```
releases: https://github.com/marcoancona/MineTime/releases
**For Microsoft Teams:**  
```
$ sudo eopkg bi --ignore-safety ./productivity/microsoft-teams/pspec.xml && sudo eopkg it microsoft-teams*.eopkg && sudo rm microsoft-teams*.eopkg
```
releases: https://aur.archlinux.org/packages/teams/
**For p3xOnenote:**  
```
$ sudo eopkg bi --ignore-safety ./productivity/p3x-onenote/pspec.xml && sudo eopkg it p3x-onenote*.eopkg && sudo rm p3x-onenote*.eopkg
releases: https://github.com/patrikx3/onenote/releases
