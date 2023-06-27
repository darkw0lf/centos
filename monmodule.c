// Nom : monmodule.c
// Sujet: Module de noyau Linux
// Formation
#include <linux/module.h>
#include <linux/kernel.h>
MODULE_LICENSE("GPL");
MODULE_AUTHOR("Stagiaire");
MODULE_DESCRIPTION("Module de noyau Linux");
MODULE_VERSION("Version 1");
int init_module(void)  
{  
	printk(KERN_INFO "[Hello world] - La fonction init_module() est 
appelée.\n"); 
	return 0;  
}  
void cleanup_module(void)  
{  
	printk(KERN_INFO "[Hello world] - La fonction cleanup_module() 
est appelée.\n");  
}
