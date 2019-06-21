# Getting Started
Welcome to ELEG 467/667!

In this course we are going to train you to be the best you can be at Pentesting and CTF's, from basic Steganography to Cryptography to being experts at binary exploitation. 

## Prerequisites
Please follow the below instructions BEFORE THE FIRST DAY. This will help us land with our feet already running for the first day. We don't have unlimited time and want to get the most out of our time together this summer. Please follow these instructions *exactly*.

#### Installing VMWare (Windows Install)
- Log into [UDeploy](https://udeploy.udel.edu/software/vmware-for-university-of-delaware/)
- Scroll to bottom and click the link that says *To download, please click here to authenticate*
- When logged in, choose VMWare Workstation 15
- On the right side click *Add to cart*.
- This will bring you to a page with a green download button and a serial number. **Copy the serial number** and then click download. It shouldn't take longer than 5 minutes.
- Run the installation file and continue with a normal installation.
- Before hitting finish, click the license button. Paste the license key you copied from earlier.
- Congrats! Let's move to step 2. 

#### Installing Kali Linux
- Download this [Kali Linux VM](https://www.offensive-security.com/kali-linux-vm-vmware-virtualbox-image-download/). I would choose the 64 bit version.
- Once downloaded, extract the zip file into a folder. Keep track of where you extracted it to.
- Launch VMWare Workstation or Fusion. 
- Click Open Virtual Machine
- Find the folder you extracted, open it and click the VM file inside.
- If a something pops up, click "I Copied it"
- Click the first line inside the terminal
- login as "root" and the password is "toor"
- Congrats! You have your own Kali Linux VM!

#### Installing pwntools on your Linux Machine 
- Open your Linux VM
- Once logged in, click the black terminal window on the left. 
- Copy these lines of code
```
apt-get update
pip install --upgrade pip
pip install --upgrade pwntools
```
- Paste these into the terminal and click enter
- After it runs, pwntools should be installed. 

#### Finishing
Now that you have everything installed, feel free to start getting your feet wet in CTF's! A good website to start at is [PicoCTF](https://2018game.picoctf.com/)
