if ! [python]
echo "python jest zainstalowany"
else
    cd %USERPROFILE%\downloads
    curl -O https://www.python.org/ftp/python/3.8.7/python-3.8.7-amd64.exe
    echo "python został pobrany w wersji 3.8.7-amd64"
    python-3.8.7-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    echo "python został zainstalowany"  