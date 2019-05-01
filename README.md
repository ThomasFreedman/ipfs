## The Easy Way to Install IPFS
These are scripts to install IPFS onto Raspberry Pi3 or Pi3+ microcomputers, AND any hardware (laptops, old computers etc) a Debian Linux OS can be installed on. Note that only 64 bit systems are supported.

Potentially almost any Linux OS could be used, however these scripts have only been tested on Debian and Raspberry Pi3 (RPi3 or RPi3+) as written. The Debian Net Installer was used for all non RPi systems.

There are 2 different methods used to install IPFS:
1. Using the standard Debian package manager (apt / apt-get) configured with the siderus repository
2. Using a "go" language (golang) approach to install the go language and ipfs-update to install IPFS

Each have their merrits and issues. The golang approach is slower, but provides the ability to obtain the latest IPFS version. 

These scripts provide a "grandma just button" to get a base IPFS installation up and running, after the base operating system is installed on the target hardware. Instructions that go thru the setup process for the Raspberry Pi3 (RPi3 or RPi3+) will soon follow. Instructions for the Debian OS installation onto laptops and other hardware are more difficult due to the variation of hardware and BIOSs systems use. There is a multitude of documentation available online to install different Linux OS versions from distributors such as Debian, Mint, Ubuntu etc. I see no reason to duplicate those. There is much more work to be done to build on top of the base OS layer that is a priority.

I wouldn't say installing any OS is easy for grandma. Depending on the chosen OS (and grandma), some are easier than others. The main focus here is getting IPFS installed on a fresh OS installation, not what it takes to get the base OS installed.

Once IPFS is installed, which is what these scripts do with almost no human intervention, the next task to accomplish is getting content off from centralized media platforms and onto IPFS. That requires standards and conventions for pinning, metadata capture and indexing. 

Currently there are 4 IPFS installation scripts that automate the steps described on http://sitepins.net/guides/install-ipfs:
1. **install-ipfs**	A new unified installer for all platforms (recommended)
2. **go-ipfs-amd64**	Installer for 64 bit Linux OS (only tested with Debian) using golang
3. **go-ipfs-rpi3**		Installer for golang based installation for RPi3
4. **siderus-ipfs-rpi3** Installer using siderus apt repository for RPi3
  
Once you have your base operating system installed, copy one of these scripts to your target system and run it to install IPFS. These are bash shell scripts, and must be run as root or with a sudo prefix. No command line arguments are necessary. They will create an "ipfs" account you can login with, set the maximum space devoted to IPFS storage to 75% of available disk space, and create an init.log file in /home/ipfs/.ipfs/ with the IPFS node hash ID. 

The Go language seems to change versions regularly, and it may be necessary to change the version with the -g option if you see a the default version is unavailable. I am not aware of a method to install "the latest" version of Go (but latest version of IPFS is possible using go), and if there were it may break the ipfs-update program if it isn't compatible with the latest Go language version.

To see all options for the unified installer enter:

    $>sudo ./install-ipfs [-h | -help]

## Testing Performed
Testing has been done on 2 different hardware platforms:
1. Raspberry Pi model 3
2. A VPS host with Debian 9

And 3 different operating system variations:
1. Raspbian full desktop installed with NOOBS 3.0
2. Raspbian Lite (headless) installed directly onto sd card with dd
3. Debian 9 (Stretch) installed via hosting service control panel

The other primary variation was the ipfs source, either the siderus repository or golang update-ipfs program from googleapis.com. This yielded 6 distinct tests to verify script operation. Option permutations were not explicitly tested, but were verified prior to the live system installation tests. Some bugs may surface as a result of this methodology. 

The focus of the testing was to verify a functional IPFS node installation, installed with the install-ipfs script using no options (all defaults, siderus apt repo) and with the -g option. This verifies the installation using the siderus apt repository and the golang ipfs-update approach (googleapis.com). 

### Raspbian testing on Raspberry Pi3
Test1 - NOOBS, rpi stretch with full desktop, installation using all default options
- siderus apt repo

Test2 - NOOBS, rpi stretch with full desktop, installation using -g option:
- golang version 1.10.1 (-g without a version)

Test3 - Raspbian Lite, rpi stretch with full desktop, installation using all default options
- siderus apt repo

Test4 - Raspbian Lite, rpi stretch with full desktop, installation using -g option:
- golang version 1.10.1 (-g without a version)

### Debian testing on VPS
Test5 - Debian Vultr VPS, stretch server, installation using all default options
- siderus apt repo

Test6 - Debian Vultr VPS, stretch server, installation using -g option:
- golang version 1.10.1 (-g without a version)

I also verified the node's web interface (see below) was accessible using ssh tunneling, however the IPFS configuration must be changed, and requires the port info of the ssh tunnel to update the ipfs config file. This makes the webui through ssh tunneling less dynamic, as it ties IPFS node config to the web client host.


## Accessing the Web Interface (/webui)
If you are not using a headless (i.e. a non-graphical desktop) you should be able to access the web interface at http://localhost:5001/webui. On headless servers access it through an "ssh tunnel" by following this procedure:

1. Make sure you have configured your IPFS node for ssh access and you can login via ssh. 
2. Login with ssh this way  to create the tunnel:
   `ssh -L <port>:localhost:5001 ipfs@<IPFS node address>`
  You can use any high port value above 1024 not being used, such as 50001. This is a port on the client (broswer) machine.
3. This will log you into the IPFS server node with a tunnel. Then run these 2 commands on the IPFS server:
```    
    $ ipfs config --json API.HTTPHeaders.Access-Control-Allow-Origin '["http://127.0.0.1:<port>", "http://127.0.0.1:5001", "https://webui.ipfs.io"]'
    $ ipfs config --json API.HTTPHeaders.Access-Control-Allow-Methods '["PUT", "GET", "POST"]'
```
After changing the configuration you will need to restart the ipfs daemon, or reboot the node and then log back in with ssh
to re-establish the ssh tunnel. 

If you used the default systemd autostart method, you can probably avoid the reboot and simply restart the daemon with:
`sudo systemctl restart ipfs`. Now you can point your web browser to this URL to access the node's web interface:
`http://127.0.0.1:<port>/webui`

