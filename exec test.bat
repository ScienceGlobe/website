@echo off
:header
color 2
echo  #####     ####    ####    #######  ##   ##    ####   #######             ####   ####      #####   ######   #######
echo ##   ##   ##  ##    ##      ##   #  ###  ##   ##  ##   ##   #            ##  ##   ##      ##   ##   ##  ##   ##   #
echo #        ##         ##      ## #    #### ##  ##        ## #             ##        ##      ##   ##   ##  ##   ## #
echo  #####   ##         ##      ####    ## ####  ##        ####             ##        ##      ##   ##   #####    ####
echo      ##  ##         ##      ## #    ##  ###  ##        ## #             ##  ###   ##   #  ##   ##   ##  ##   ## #
echo ##   ##   ##  ##    ##      ##   #  ##   ##   ##  ##   ##   #            ##  ##   ##  ##  ##   ##   ##  ##   ##   #
echo  #####    @echo off
 ####    ####    #######  ##   ##    ####   #######             #####  #######   #####   ######   #######
echo Science Globe: Instalando Python e bibliotecas necessárias...
echo Science Globe: Fazendo a validação dos arquivos...

py scienceglobe/manage.py makemigrations
py scienceglobe/manage.py migrate

echo Science Globe: Validação realizada com sucesso!


echo Science Globe: Iniciando o servidor Django...
py scienceglobe/manage.py runserver
pause