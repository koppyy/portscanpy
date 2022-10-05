#!bin/bash
clear
cd 
rm -rf portscanpy
git clone https://github.com/koppyy/portscanpy
clear
echo 'Não há atualizações!'
sleep 10
cd portscanpy
python portscanpy.py
