These are scripts to install IPFS onto Raspberry Pi3 or Pi3+ microcomputers, AND any hardware (laptops, old computers etc) a Debian Linux OS can be installed on.

At some point these scripts can be combined into a single variant. For now the various versions found here target either the Raspberry Pi platform or all others. Almost any Linux OS could be used, however these scripts have only been tested on Debian and Raspberry Pi3 (RPi3 or RPi3+). I use the Debian Net Installer for all non RPi systems.

Besides the base platform, there are 2 different ways IPFS can be installed:
1. Using the standard Debian package manager (apt / apt-get) configured with the siderus repository
2. Using a "go" language (golang) approach to install the go language and ipfs-update to install IPFS.

Each have their merrits and issues. These scripts provide a "grandma just button" to get a base IPFS installtion up and running, after the base operating system is installed on the target hardware. I will create instructions that go thru the setup process for the Raspberry Pi3 (RPi3 or RPi3+). Instructions for the Debian OS installtion onto laptops and other hardware are more difficult due to the variation of hardware and BIOS variants. There is a multitude of documentation available online to install different Linux OS versions from distributors such as Debian, Mint, Ubuntu etc. I see no reason to duplicate those. There is much more work to be done to build on top of the base OS layer that is a priority.

I wouldn't say installing any OS is easy for grandma. Depending on the chosen OS some are easier than others. The main focus here is getting IPFS installed on a fresh OS installation, not what it takes to get the base OS installed.

Once IPFS is installed, which is what these scripts do with almost no human intervention, the next task to accomplish is getting content off from centralized media platforms and onto IPFS. That requires standards and conventions for pinning, metadata capture indexing. 

Currently there are 3 IPFS installtion scripts that automate the steps described on http://sitepins.net/guides/install-ipfs:
  	**go-ipfs** 	        Installer for golang based installtion for RPi3
	**install-ipfs** 	Installer for siderus / apt installation for RPi3
	**go-ipfs-amd64** 	Installer for 64 bit Linux OS (only tested with Debian) using golang
  
Once you have your base operating ststem installed, copy one of these installers to your target system and run it to install IPFS. These are bash shell scripts, and must be run as root or with a sudo prefix. No command line arguments are necessary. They will create an "ipfs" account you can login with, set the maximum space devoted to IPFS storage to 75% of available disk space, and create an init.log file in /home/ipfs/.ipfs/ with the IPFS node hash ID. 

There are variables defined at the top of the script you can set, but the defaults for these are probably fine. 

    WAIT=0                               # Set to 1 to pause after each step
    SYSD=1                               # Set to 1 to use systemd, 0 for @reboot & cron to run ipfs on startup
    DISTUP=0                             # Set to 1 to do a OS distribution upgrade
    GOVER=1.10.1                         # Go language version to install

The Go language seems to change versions regularly, and it may be necessary to change this if you see errors the version is unavailable. I am not aware of a method to install "the latest" version of Go, and if there were it may break the ipfs-update program if it isn't compatible with the latest Go language version.

The amd64 installer also has a setting for the method to start IPFS upon OS startup. The default is SYSD=1 to use systemd. If set to 0 the alternate method of using @reboot with cron is used.
 
