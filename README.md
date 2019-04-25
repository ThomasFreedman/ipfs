These are scripts to install IPFS onto Raspberry Pi3 or Pi3+ microcomputers, AND any hardware (laptops, old computers etc) a Debian Linux OS can be installed on.

At some point these scripts can be combined into a single variant. For now the various versions found here target either the Raspberry Pi platform or all others. Almost any Linux OS could be used, however these scripts have only been tested on Debian and Raspberry Pi3 (RPi3 or RPi3+). I use the Debian Net Installer for all non RPi systems.

Besides the base platform, there are 2 different ways IPFS can be installed:
1. Using the standard Debian package manager (apt / apt-get) configured with the siderus repository
2. Using a "go" language (golang) approach to install the go language and ipfs-update to install IPFS.

Each have their merrits and issues. These scripts provide a "grandma just button" to get a base IPFS installtion up and running, after the base operating system is installed on the target hardware. I will create instructions that go thru the setup process for the Raspberry Pi3 (RPi3 or RPi3+). Instructions for the Debian OS installtion onto laptops and other hardware are more difficult due to the variation of hardware and BIOS variants. There is a multitude of documentation available online to install different Linux OS versions from distributors such as Debian, Mint, Ubuntu etc. I see no reason to duplicate those. There is much more work to be done to build on top of the base OS layer that is a priority.

I wouldn't say installing any OS is easy for grandma. Depending on the chosen OS some are easier than others. The main focus here is getting IPFS installed on a fresh OS installation, not what it takes to get the base OS installed.

Once IPFS is installed, which is what these scripts do with almost no human intervention, the next task to accomplish is getting content off from centralized media platforms and onto IPFS. That requires standards and conventions for pinning, metadata capture indexing. 

Currently there are 3 IPFS installtion scripts:
  **go-ipfs** 	        Installer for golang based installtion for RPi3
	**install-ipfs** 	    Installer for siderus / apt installation for RPi3
	**go-ipfs-amd64** 	  Installer for 64 bit Linux OS (only tested with Debian) using golang
  
Once you have your base operating ststem installed, copy one of these installers to your target system and run it to install IPFS. These are bash shell scripts, and must be run as root or with a sudo prefix. No command line arguments are necessary. They will create an "ipfs" account you can login with, set the maximum space devoted to IPFS storage to 75% of available disk space, and create an init.log file in /home/ipfs/.ipfs/ with the IPFS node hash ID. 

The defaults used are defined at the top of the script, such as whether to pause after each step during installation (WAIT=1) or whether to perform a distribution upgrade (DIST=1). 
