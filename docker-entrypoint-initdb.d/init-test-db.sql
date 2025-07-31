CREATE USER testuser WITH PASSWORD 'password';
CREATE DATABASE testdatabase OWNER testuser;
GRANT ALL PRIVILEGES ON DATABASE testdatabase TO testuser;