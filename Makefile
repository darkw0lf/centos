obj-m += monmodule.o
all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules
clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
install:
	cp ./monmodule.ko* /lib/modules/$(shell uname -r)/kernel/drivers/misc
uninstall:
	rm -i /lib/modules/$(shell uname -r)/kernel/drivers/misc/monmodule.ko*
	depmod -a
