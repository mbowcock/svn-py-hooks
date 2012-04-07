echo off
set REPOS=%1
set REV=%2
set PATH=c:\python31;
python.exe d:\repositories\reponame\hooks\processCommit.py %REPOS% %REV%
