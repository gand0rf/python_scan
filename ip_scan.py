import time, psutil, subprocess
from multiprocessing.pool import ThreadPool

def ping(card, num):
    alive_ip = ''
    check = subprocess.Popen(['ping', '-c', '1', '-I', f'{card}', f'192.168.1.{num}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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

def thread_scan(card):
    print('\nStarting thread scan...')
    args = []
    for num in range(0,255):
        args.append((card, str(num)))
    start_time = time.perf_counter()
    with ThreadPool() as pool:
        results = pool.starmap_async(ping, args)
        results.wait()
        pool.close()
        pool.join()
    end_time = time.perf_counter()
    print('\nThread scans completed...')
    return ips(results.get()), (end_time - start_time)

def interface():
    net_interfaces = psutil.net_if_addrs()
    net_list = list(net_interfaces.keys())
    for network in range(0, len(net_list)):
        if net_list[network] != 'lo':
            print(f'{network}: {net_list[network]}')
    net_selection = int(input("\nEnter number for network interface to use: "))
    return net_list[net_selection] 

if __name__ == '__main__':
    print('\n')
    card = interface()
    thread_scan_results = thread_scan(card)
    if len(thread_scan_results[0]) > 0:
        print('\nFound addresses:\n')
        for z in thread_scan_results[0]:
            print(f'{z}')
    else:
        print('\nNo ip addresses found...')
    print(f'\nTotal time for thread scans: {thread_scan_results[1]}\n')
