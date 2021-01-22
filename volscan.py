import port_scan



targets_ipAddress = str(input("[+] Enter Target To Scan For Vulnerable Port's: "))
target_port_scan_ammount = int(input("[+] How Many Ports Do You Want To Scan?: "))



port_scan.main(targets_ipAddress,target_port_scan_ammount)




with open('vulbanners.txt',"r") as file:
    count = 0
    for banner in port_scan.banners_list:
        file.seek(0)
        for line in file.readlines():
            if (line.strip() in banner):
                print(f"[!! VULNERABLE BANNER !!] {banner} On Port {port_scan.open_ports[count]}")
        count += 1