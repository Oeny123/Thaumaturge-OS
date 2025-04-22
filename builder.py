import subprocess
import os
import shutil

BUILDIR = "Kapemeyt"

subprocess.run(['mkdir', BUILDIR]) #Make New Directory
os.chdir(BUILDIR) #change directoy

subprocess.run(['bash','../lbconfig']) # runs the bash file lbconfig

logs = True
brave = True
docker = True


# Brave
if brave:
    brave_source = "../Confs/hooks/9040-brave-repo.chroot"
    brave_destination = "./config/hooks/normal/"
    shutil.copy(brave_source, brave_destination)

#Docker
if docker:
    docker_source = "../Confs/hooks/9090-docker-repo.chroot"
    docker_destination = "./config/hooks/normal/"
    shutil.copy2(docker_source, docker_destination)

#hooks
initial_hook_source = "../Confs/hooks/9080-remove-initail.chroot"
initial_hook_destination = "./config/hooks/normal"
shutil.copy(initial_hook_source, initial_hook_destination)

#Bootloaders
bootloader_source = "../Confs/bootloaders/"
bootloafer_destination = "./config/bootloaders/"

for list_dir in os.listdir(bootloader_source): # Copies the BootLoaders

    source = os.path.join(bootloader_source, list_dir)
    destination  = os.path.join(bootloafer_destination, list_dir)

    shutil.copytree(source, destination) 

#Grub
grub_source = "../Confs/grub/grub"
grub_destination = "./config/includes.chroot/etc/default/"
os.makedirs(grub_destination)
shutil.copy2(grub_source, grub_destination)

grub_image_source = "../Confs/grub/desktop-grub.png"
grub_image_destination = "./config/includes.chroot/usr/share/images/desktop-base/"
os.makedirs(grub_image_destination)
shutil.copy(grub_image_source, grub_image_destination)


#Calamares
calamares_source = "../Confs/calinst/calamares"
calamares_destination = "./config/includes.chroot/etc/calamares"
shutil.copytree(calamares_source, calamares_destination)

icon_source = "../Confs/calinst/install-tos.png"
icon_destination = "./config/includes.chroot/usr/share/pixmaps"
os.makedirs(icon_destination)
shutil.copy(icon_source, icon_destination)

dot_desktop_source = "../Confs/calinst/install-debian.desktop"
dot_desktop_destination = "./config/includes.chroot/usr/share/applications"
os.makedirs(dot_desktop_destination)
shutil.copy(dot_desktop_source, dot_desktop_destination)

#Hostname
hostname_source = "../Confs/hostname"
hostname_destination = "./config/includes.chroot/etc/"
shutil.copy(hostname_source, hostname_destination)

hosts_source = "../Confs/hosts"
hosts_destination = "./config/includes.chroot/etc/"
shutil.copy(hosts_source, hosts_destination)

#Skel
skel_source = "../Confs/skel/"
skel_destination = "./config/includes.chroot/etc/skel"
shutil.copytree(skel_source, skel_destination, False, None)


#gnome-shell
gs_sourse = "../Confs/gnome-shell/"
gs_destination = "./config/includes.chroot/usr/share/gnome-shell"
shutil.copytree(gs_sourse,gs_destination,False,None)


#Plymouth
plymouth_source = "../Confs/plymouth/"
plymouth_destination = "./config/includes.chroot/usr/share/plymouth/themes/moonlight/"
os.makedirs(plymouth_destination)
for list_dir in os.listdir(plymouth_source):

    source = os.path.join(plymouth_source, list_dir)

    if source == "../Confs/plymouth/plymouthd.defaults":
        shutil.copy(source, "./config/includes.chroot/usr/share/plymouth/")
        continue

    source = os.path.join(plymouth_source, list_dir)
    shutil.copy2(source, plymouth_destination)

#gdm3 login logo
gdm_logo_source = "../Confs/gdm/logo.png"
gdm_logo_destination = "./config/includes.chroot/usr/share/images/thaumaturge/"
if not os.path.exists(gdm_logo_destination):
    os.makedirs(gdm_logo_destination)
shutil.copy(gdm_logo_source, gdm_logo_destination)

gdm_config_source = "../Confs/gdm/greeter.dconf-defaults"
gdm_config_destination = "./config/includes.chroot/etc/gdm3/"
if not os.path.exists(gdm_config_destination):
    os.makedirs(gdm_config_destination)
shutil.copy(gdm_config_source, gdm_config_destination)


#Wallpaper
bg_source = "../Confs/images/"
bg_destination = "./config/includes.chroot/usr/share/desktop-base/emerald-theme/wallpaper/contents/images"
os.makedirs(bg_destination)
for list_dir in os.listdir(bg_source):

    source = os.path.join(bg_source,list_dir)
    shutil.copy2(source,bg_destination)


#neofetch
neofetch_source = "../Confs/bin/neofetch"
neofetch_destination = "./config/includes.chroot/bin/"
if not os.path.exists(neofetch_destination):
    os.makedirs(neofetch_destination)
shutil.copy(neofetch_source, neofetch_destination)

subprocess.run(['lb','build']) # start build process
    
