@echo off
cls
:header
color 2
echo  #####     ####    ####    #######  ##   ##    ####   #######             ####   ####      #####   ######   #######
echo ##   ##   ##  ##    ##      ##   #  ###  ##   ##  ##   ##   #            ##  ##   ##      ##   ##   ##  ##   ##   #
echo #        ##         ##      ## #    #### ##  ##        ## #             ##        ##      ##   ##   ##  ##   ## #
echo  #####   ##         ##      ####    ## ####  ##        ####             ##        ##      ##   ##   #####    ####
echo      ##  ##         ##      ## #    ##  ###  ##        ## #             ##  ###   ##   #  ##   ##   ##  ##   ## #
echo ##   ##   ##  ##    ##      ##   #  ##   ##   ##  ##   ##   #            ##  ##   ##  ##  ##   ##   ##  ##   ##   #
echo  #####     ####    ####    #######  ##   ##    ####   #######             #####  #######   #####   ######   #######
pause
echo Science Globe: Instalando Python e bibliotecas necessárias...

echo Science Globe: Verifica se o Python está instalado
python --version 2>nul

IF %ERRORLEVEL% EQU 0 (
    echo Science Globe: Python está instalado:
    python --version
) ELSE (
    echo Science Globe: Python não está instalado. Baixando a versão mais recente...
    REM Baixa a versão mais recente do Python
    powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe', 'python-3.12.3-amd64.exe')"
    echo Instalando Python...
    REM Instala a versão baixada do Python
    python-3.12.3-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    echo Python instalado com sucesso:
    python --version
    REM Remove o instalador após a instalação
    del python-3.12.3-amd64.exe
)

echo Science Globe: Instalando bibliotecas Python...

rem Definindo o tamanho da barra de carregamento
set "barSize=20"

rem Inicializando a barra de carregamento
set "progress=0"
for /l %%a in (1,1,%barSize%) do set "bar=!bar!-"

rem Instalando cada biblioteca com uma barra de progresso
pip install asgiref==3.8.1 >nul
set /a "progress+=1"
call :UpdateProgressBar
pip install bleach==6.1.0 >nul
set /a "progress+=1"
call :UpdateProgressBar
pip install distlib==0.3.8 >nul
set /a "progress+=1"
call :UpdateProgressBar
pip install Django==5.0.4 >nul
set /a "progress+=1"
call :UpdateProgressBar
pip install django-axes==6.4.0 >nul
set /a "progress+=1"
call :UpdateProgressBar
pip install django-crispy-forms==2.1 >nul
set /a "progress+=1"
call :UpdateProgressBar
pip install django-debug-toolbar==4.3.0 >nul
set /a "progress+=1"
call :UpdateProgressBar
pip install django-summernote==0.8.20.0 >nul
set /a "progress+=1"
call :UpdateProgressBar
pip install filelock==3.13.4 >nul
set /a "progress+=1"
call :UpdateProgressBar
pip install numpy==1.26.4 >nul
set /a "progress+=1"
call :UpdateProgressBar
pip install pillow==10.3.0 >nul
set /a "progress+=1"
call :UpdateProgressBar
pip install platformdirs==4.2.0 >nul
set /a "progress+=1"
call :UpdateProgressBar
pip install python-dotenv==1.0.1 >nul
set /a "progress+=1"
call :UpdateProgressBar
pip install six==1.16.0 >nul
set /a "progress+=1"
call :UpdateProgressBar
pip install sqlparse==0.5.0 >nul
set /a "progress+=1"
call :UpdateProgressBar
pip install tzdata==2024.1 >nul
set /a "progress+=1"
call :UpdateProgressBar
pip install utils==1.0.2 >nul
set /a "progress+=1"
call :UpdateProgressBar
pip install virtualenv==20.25.3 >nul
set /a "progress+=1"
call :UpdateProgressBar
pip install virtualenvwrapper-win==1.2.7 >nul
set /a "progress+=1"
call :UpdateProgressBar
pip install webencodings==0.5.1 >nul
set /a "progress+=1"
call :UpdateProgressBar

echo Science Globe: Todas as bibliotecas foram instaladas com sucesso!
pause

echo Science Globe: Fazendo a validação dos arquivos...

py scienceglobe/manage.py makemigrations
py scienceglobe/manage.py migrate

echo Science Globe: Validação realizada com sucesso!


echo Science Globe: Iniciando o servidor Django...
py scienceglobe/manage.py runserver
pause

exit

:UpdateProgressBar
rem Atualizando a barra de carregamento
set "bar="
for /l %%a in (1,1,%progress%) do set "bar=!bar!#"
for /l %%a in (%progress%,1,%barSize%) do set "bar=!bar!-"

rem Redesenhando a barra de carregamento na mesma linha
echo Progresso:      %progress%/%barSize% concluído   
goto :eof
