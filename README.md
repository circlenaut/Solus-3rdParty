# 3rdParty Packages for Solus
The offical Solus 3rd-party repo is [here](https://getsol.us/articles/software/third-party/en/). Otherwise feel free to use the packages below.

## Disclaimer
These packages are **not official**, they are neither supported nor endorsed by the official Solus devs. Do not ask for help in Solus's help forum, instead create an issue [here](https://github.com/circlenaut/Solus-3rdParty/issues).

## Direct .eopkg files(NEW)
You can directly download the compiled .eopkg files from [here](https://github.com/circlenaut/Solus-3rdParty/releases/latest)

To install any program directly from eopkg file, First download the file and then `cd` into that folder like `$ cd ~/Downloads`, After that run  
```
$ sudo eopkg it ./your-program-name.eopkg
```
**NOTE** : Please read the release notes first to know if their are any extra dependencies or not

### Building from Source
Clone this repo and execute the following

**For Microsoft Visual Studio Code:**
```
$ sudo eopkg bi --ignore-safety ./productivity/visual-studio-code/pspec.xml && sudo eopkg it vscode-microsoft*.eopkg && sudo rm vscode-microsoft*.eopkg
```
**For Microsoft Edge Dev:**  
```
$ sudo eopkg bi --ignore-safety ./browser/microsoft-edge-dev/pspec.xml && sudo eopkg it microsoft-edge-dev*.eopkg && sudo rm microsoft-edge-dev*.eopkg
```
**For Figma Linux:**  
```
$ sudo eopkg bi --ignore-safety ./graphics/figma-linux/pspec.xml && sudo eopkg it figma-linux*.eopkg && sudo rm figma-linux*.eopkg
```
**For 1Password:**  
```
$ sudo eopkg bi --ignore-safety ./security/1password/pspec.xml && sudo eopkg it 1password*.eopkg && sudo rm 1password*.eopkg
```
**For Everdo:**  
```
$ sudo eopkg bi --ignore-safety ./productivity/everdo/pspec.xml && sudo eopkg it everdo*.eopkg && sudo rm everdo*.eopkg
```
**For Morgen:**  
```
$ sudo eopkg bi --ignore-safety ./productivity/morgen/pspec.xml && sudo eopkg it morgen*.eopkg && sudo rm morgen*.eopkg
```
**For Microsoft Teams:**  
```
$ sudo eopkg bi --ignore-safety ./productivity/microsoft-teams/pspec.xml && sudo eopkg it microsoft-teams*.eopkg && sudo rm microsoft-teams*.eopkg
```
**For p3xOnenote:**  
```
$ sudo eopkg bi --ignore-safety ./productivity/p3x-onenote/pspec.xml && sudo eopkg it p3x-onenote*.eopkg && sudo rm p3x-onenote*.eopkg
```
**For Video DownloadHelper Companion App:**  
```
$ sudo eopkg bi --ignore-safety ./browser/downloadhelper/pspec.xml && sudo eopkg it video-download-helper-companion*.eopkg && sudo rm video-download-helper-companion*.eopkg
```
**For Lightworks:**  
```
$ sudo eopkg bi --ignore-safety ./graphics/lightworks/pspec.xml && sudo && sudo eopkg it lightworks*.eopkg && sudo rm lightworks*.eopkg
```
## Obsolescence
Note that the eopkg package system is being phased out and replaced by Solbuild:
- https://www.reddit.com/r/SolusProject/comments/7trxu9/can_i_use_local_pspecxml_to_build_package/
- https://www.reddit.com/r/SolusProject/comments/epu81o/building_an_eopkg/

**New Build references:**  
```
- https://getsol.us/articles/packaging/
- https://getsol.us/articles/packaging/building-a-package/en/
- https://getsol.us/articles/packaging/local-repository/en/
- https://getsol.us/articles/packaging/building-a-package/en/
- https://www.ordinatechnic.com/distribution-specific-guides/Solus/building-a-package-on-solus-for-installation-by-eopkg-from-a-custom-local-repository
