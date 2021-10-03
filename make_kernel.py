import subprocess,os,time,sys
from pyfiglet import Figlet
from sys import path
from colorama import Fore,Back,Style
import colorama
colorama.init(autoreset=True)
class kernel_arguments:
    
    def kernelversion(self):
        
        self.kernelversion=os.system('echo -e "\033[1;33m" This is Your Kernel VErsion $(make kernelversion)')
        
        

    def check_protonclang_path(self):
        self.path=input(Fore.BLUE+"Enter the proton clang directory:")
        print(self.path)
        if os.path.exists(self.path)==True:
            print(Fore.YELLOW+"Proton clang dir found")
        else:
            print(Fore.RED+"please give exact file path ")
    
    def check_binaries(self):
        binaries=self.path + '/' 
        print(binaries)
        
        r = ['clang','aarch64-linux-gnu-ld','arm-linux-gnueabi-ld','ld.lld','llvm-ar','llvm-nm','llvm-objcopy','llvm-objdump']
        for i in r:
            if os.path.exists(binaries + i)==True:
                print(Fore.YELLOW+ i + " found")
            else:
                print(Fore.RED+ i + " not found")
    def make_env(self):
        
        

        self.PATH=os.environ['PATH']
        os.environ['PATH']='/home/madriyana/android/toolchains/proton-clang-master/bin:'+ self.PATH
        print(os.environ['PATH'])
        
    def Kernel_compilation(self):
        from colorama import Fore,Back,Style
        self.KCONFIG_INITIAL=input(Fore.BLUE+"please give the name of the KCONFIG: ")
        print(self.KERNEL_DIR)
        self.KCONFIG=self.KERNEL_DIR + '/arch/arm64/configs/' + self.KCONFIG_INITIAL
        print(self.KCONFIG)
        KCONFIG_DST=self.KERNEL_DIR + '/arch/arm64/configs/custom_defconifg'
        
        while True:
            print ( Fore.YELLOW+" Select the option\n"
                " 1. Make kernel from Starting\n"
                " 2. Make kernel from previous run\n"
                " 3. Exit from compiling")
            self.option =  input("Enter The option: ")
            if self.option=="1":
                os.system("rm -rf out")
                os.system('make O=out ARCH=arm64 CC=clang ' + self.KCONFIG_INITIAL )
                menuconfig_selection=input(Fore.BLUE+"Edit the Config Press Y/n:")
                if menuconfig_selection=="Y" or "y":
                    os.system("make menuconfig ARCH=arm64 CC=clang")
                else:
                    passsubprocess.check_output("banner Welcome to Kernel BUild",shell=True).strip()
                os.system('make -j$(nproc --all) O=out ARCH=arm64 CC=clang LD=ld.lld AR=llvm-ar NM=llvm-nm OBJCOPY=llvm-objcopy OBJDUMP=llvm-objdump STRIP=llvm-strip CROSS_COMPILE=aarch64-linux-gnu- CROSS_COMPILE_ARM32=arm-linux-gnueabi- Image.gz-dtb ||make -j$(nproc --all) O=out ARCH=arm64 CC=clang LD=ld.lld AR=llvm-ar NM=llvm-nm OBJCOPY=llvm-objcopy OBJDUMP=llvm-objdump STRIP=llvm-strip CROSS_COMPILE=aarch64-linux-gnu- CROSS_COMPILE_ARM32=arm-linux-gnueabi- Image.gz ||make -j$(nproc --all) O=out ARCH=arm64 CC=clang LD=ld.lld AR=llvm-ar NM=llvm-nm OBJCOPY=llvm-objcopy OBJDUMP=llvm-objdump STRIP=llvm-strip CROSS_COMPILE=aarch64-linux-gnu- CROSS_COMPILE_ARM32=arm-linux-gnueabi- Image.gz dtbo.img')
                save_defconfig=input("Save the defconfig as custom_defconfig Y/n")
                if save_defconfig=="Y" or "y":
                    os.system("cp  out/.config arch/arm64/configs/custom-defconfig")
                else:
                    pass
            elif  self.option=="2":
                os.system('make -j$(nproc --all) O=out ARCH=arm64 CC=clang LD=ld.lld AR=llvm-ar NM=llvm-nm OBJCOPY=llvm-objcopy OBJDUMP=llvm-objdump STRIP=llvm-strip CROSS_COMPILE=aarch64-linux-gnu- CROSS_COMPILE_ARM32=arm-linux-gnueabi- Image.gz-dtb ||make -j$(nproc --all) O=out ARCH=arm64 CC=clang LD=ld.lld AR=llvm-ar NM=llvm-nm OBJCOPY=llvm-objcopy OBJDUMP=llvm-objdump STRIP=llvm-strip CROSS_COMPILE=aarch64-linux-gnu- CROSS_COMPILE_ARM32=arm-linux-gnueabi- Image.gz ||make -j$(nproc --all) O=out ARCH=arm64 CC=clang LD=ld.lld AR=llvm-ar NM=llvm-nm OBJCOPY=llvm-objcopy OBJDUMP=llvm-objdump STRIP=llvm-strip CROSS_COMPILE=aarch64-linux-gnu- CROSS_COMPILE_ARM32=arm-linux-gnueabi- Image.gz dtbo.img')
            
            elif self.option=="3":
                sys.exit(0)
            else:
                print(Fore.RED+"Invalid option")

custom_fig=Figlet(font='graffiti')
print(custom_fig.renderText('Welcome TO Kernel Build'))
print(Fore.BLUE+'1. Setup The Environment\n'
          '2. Go to Build Kernel')
selection=input(Fore.YELLOW+'Selcet The option: ')
if selection=="1":
    print(Fore.BLUE+"Downloading THe file ....")
    os.system('wget https://github.com/kdrag0n/proton-clang/archive/refs/tags/20210522.tar.gz -o ~/proton-clang.tar.gz' )
    print(Fore.RED+"Extarcting the FIle")
    os.system('tar -xvzf ~/proton-clang.tar.gz && cd proton-clang-master && echo $PWD this is your proton-clang Directory')
    print(Fore.YELLOW+"Extraction Compeleted")
elif selection=="2":
    print(Fore.RED+"Welcome To Kernel Build")
c1=kernel_arguments()
c1.kernelversion()
c1.check_protonclang_path()
time.sleep(2)
c1.check_binaries()
time.sleep(2)
c1.make_env()
time.sleep(2)
print("Starting Make kernel.....")
time.sleep(2)

c1.Kernel_compilation()
    

    



        







