cd ~/aageno/view/
rm dp.zip
zip -r dp.zip aagenoui/*
cd /var/www/html
mr -rf *
mv ~/aageno/view/dp.zip .
unzip dp.zip
