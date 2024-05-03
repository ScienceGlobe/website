@echo off
cls
:header
color 2
echo
echo
echo  #####     ####    ####    #######  ##   ##    ####   #######             ####   ####      #####   ######   #######
echo ##   ##   ##  ##    ##      ##   #  ###  ##   ##  ##   ##   #            ##  ##   ##      ##   ##   ##  ##   ##   #
echo #        ##         ##      ## #    #### ##  ##        ## #             ##        ##      ##   ##   ##  ##   ## #
echo  #####   ##         ##      ####    ## ####  ##        ####             ##        ##      ##   ##   #####    ####
echo      ##  ##         ##      ## #    ##  ###  ##        ## #             ##  ###   ##   #  ##   ##   ##  ##   ## #
echo ##   ##   ##  ##    ##      ##   #  ##   ##   ##  ##   ##   #            ##  ##   ##  ##  ##   ##   ##  ##   ##   #
echo  #####     ####    ####    #######  ##   ##    ####   #######             #####  #######   #####   ######   #######
echo
echo
pause
echo Science Globe: Instalando Python e bibliotecas necessárias...

rem Verifica se o Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Science Globe: Python não encontrado. Instalando...
    rem Instala o Python usando o pip
    python -m pip install 
)

echo Science Globe: Instalando bibliotecas Python...
pip install asgiref==3.8.1
pip install bleach==6.1.0
pip install distlib==0.3.8
pip install Django==5.0.4
pip install django-axes==6.4.0
pip install django-crispy-forms==2.1
pip install django-debug-toolbar==4.3.0
pip install django-summernote==0.8.20.0
pip install filelock==3.13.4
pip install numpy==1.26.4
pip install pillow==10.3.0
pip install platformdirs==4.2.0
pip install python-dotenv==1.0.1
pip install six==1.16.0
pip install sqlparse==0.5.0
pip install tzdata==2024.1
pip install utils==1.0.2
pip install virtualenv==20.25.3
pip install virtualenvwrapper-win==1.2.7
pip install webencodings==0.5.1
echo Science Globe: Todas as bibliotecas foram instaladas com sucesso!

rem Inicia o servidor Django
echo.
echo Science Globe: Iniciando o servidor Django...
py manage.py runserver
pause

