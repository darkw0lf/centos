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
printk(KERN_INFO "Le module est chargé.\n");
return(0);
}
void cleanup_module(void)
{
printk(KERN_INFO "Le module est déchargé.\n");
}
