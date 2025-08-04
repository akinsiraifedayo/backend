# Setup DockerHub

## 1. Create an environment called `production` on your github repo

## 2. Create account on [dockerhub](https://hub.docker.com/)
- Create a repository
- Create your personal access token and store it as the `DOCKERHUB_TOKEN` secret in your `production` github environment created above so you can access it with `secrets.DOCKERHUB_TOKEN`
- Store your username as the `DOCKERHUB_USERNAME` variable. so you can access it with `vars.DOCKERHUB_USERNAME`


## 3. Create your free (AWS)[https://aws.amazon.com/] account and add MFA to it for security reasons
- create an Ubuntu EC2 instance and enable access on https port 443, http 80 and ssh 22
- save your aws server private key secure locally and also save it to `SERVER_SSH_KEY` secrets on github actions, so you can access it with `secrets.SERVER_SSH_KEY`
- save the IP address of the aws ec2 container to `SSH_SERVER_HOST` so you can access it with `secrets.SSH_SERVER_HOST`
- save `ubuntu` to `SSH_SERVER_USER` as thats the default username for ubuntu aws ec2 instance and that can be accessed with `secrets.SSH_SERVER_USER`

## 4. Save the AWS credentials to your local pc you can access it to do a first time setup
- sudo su to become a root user
- save the AWS private key gotten from aws to ~/.ssh/aws-test-server.pem
- create a file in ~/.ssh/config and add the following line of code so you can easily ssh into it 
- replace the 111.111.111.111 with the IP of your aws
- replace aws2 with whatever name you want to call this, i call mine aws-test-server, so i can just type `ssh aws-test-server` so i can just ssh into the server.
- and the IdentityFile should be the path to the private key you got from aws

```bash
  Host aws-test-server
  HostName 111.111.111.111
  User ubuntu
  Port 22
  IdentityFile ~/.ssh/aws-test-server.pem
```

## 5. SSh into the aws server
now run the code below to enter the ubuntu aws server
```bash
ssh aws-test-server`
```

## 6. Install all packages we would need

## 7 install and setup docker
- Update packages
```bash
sudo apt-get update
```

- Install prerequisites
```bash
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

- Add Docker's official GPG key
```bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

- Set up the repository
```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

- Install Docker Engine
```bash
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

- Start Docker (and optionally enable on boot)
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

- Add your user to the docker group so you use it without sudo
```bash
sudo usermod -aG docker $USER
```
- Apply changes without logout
```bash
newgrp docker
```

- Verify it works without sudo 
```bash
docker ps
```

- Login Dockerhub
```bash
docker login
```
visit docker url and use the code displayed to authenticate


# Continue edits here

# create ssh for github actions
create ssh key for github actions and copy the repo key into the env secrets, along with username and ip address


# then on the server
git clone repo into server

ssh-keygen -t ed25519 -f ~/.ssh/github_deploy_key -N ""

copy ~/.ssh/github_deploy_key into repo deploy key

add github into server config
cat > ~/.ssh/config <<EOF
Host github.comcat repo
  HostName github.com
  User git
  IdentityFile ~/.ssh/github_deploy_key
  IdentitiesOnly yes
EOF
chmod 600 ~/.ssh/config

# Personal GitHub
Host github-personal
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_personal
  IdentitiesOnly yes

# you connect with git clone git@github-personal:akinsiraifedayo/frontend

# install docker
# 1. Update packages
sudo apt-get update

# 2. Install prerequisites
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# 3. Add Docker's official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# 4. Set up the repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 5. Install Docker Engine
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# login dockerhub
docker login

visit docker url and use their code to authenticate


# 1. Add your user to the docker group
sudo usermod -aG docker $USER

# 2. Apply changes without logout
newgrp docker

# 3. Verify
docker ps  # Should work without sudo


# NEXT STEPS
configure nginx 
