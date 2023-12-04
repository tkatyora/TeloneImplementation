cd Documents
mkdi Projects
cd Projects
mkdir coorperateweb
cd coorperateweb
python -m venv venv
mkdir implement 
cd implements
git init 
git remote add origin  https://github.com/tkatyora/TeloneImplementation.git
git add .
git commit -m 'first commit'
git checkout -b child
git pull origin master 
git push origin child
cd ..
call venv/scripts/activate
pip install django
pillow