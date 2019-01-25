#!/bin/bash

# Verify if Postgres is installed
if ! type "psql" > /dev/null; then
    echo "Postgres is not installed."
    printf "To install:\t sudo apt-get install postgresql\n"
    echo "Then excute this script again"
fi

echo "Introduce your password..."
sudo echo "Password introduced."

echo "Configuring local data base..."

printf "\nCreating data base user\n"
sudo -u postgres createuser taquilla
echo "User created: taquilla"

printf "\nCreating data base\n"
sudo -u postgres createdb taquilladb
echo "Created data base: taquilladb" 

printf "\nAssigning privileges in the data base\n"
sudo -u postgres psql << EOF
alter user taquilla with encrypted password 'taquilla'; 
grant all privileges on database taquilladb to taquilla;
\q
EOF
echo "Assigned privileges"
echo "¡Created data base!"
