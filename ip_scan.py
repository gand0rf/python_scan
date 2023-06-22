import subprocess, time, multiprocessing, psutil

def ping(two_args):
    alive_ip = ''
    card, num = two_args.split('_')
    check = subprocess.Popen(['ping', '-c', '1', '-I', f'{card}', f'192.168.1.{num}'], stdout=subprocess.PIPE)
    result = check.communicate()
    if b'1 received' in result[0]:
        alive_ip = f'192.168.1.{num}'
    return alive_ip

def ips(ip_list):
    found_ips = []
    for ip in ip_list:
        if ip != '':
            found_ips.append(ip)
    return found_ips

def core_scan(card):
    print('\nStarting core scans...')
    args = []
    start_time = time.perf_counter()
    for num in range(0,255):
        args.append(card+'_'+str(num))
    with multiprocessing.Pool(processes=8) as pool:
        results = pool.map(ping, args)
    end_time = time.perf_counter()
    print('\nCore scans completed...')
    return ips(results), (end_time - start_time)

def interface():
    net_interfaces = psutil.net_if_addrs()
    net_list = list(net_interfaces.keys())
    for network in range(0, len(net_list)):
        print(f'{network}: {net_list[network]}')
    net_selection = int(input("Enter number for network interface to use: "))
    return net_list[net_selection] 

if __name__ == '__main__':
    card = interface()
    core_scan_results = core_scan(card)
    print('\nAlive addresses:')
    for z in core_scan_results[0]:
        print(f'\t{z}')
    print(f'\nTotal time for scans: {core_scan_results[1]}')

