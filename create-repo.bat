@echo off

set project=%1
cd %~dp0

If "%1"=="" (
    echo error:  create-repo FoldersName
) else (
    python create.py %project%
)