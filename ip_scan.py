import subprocess, time, multiprocessing

def ping(num):
    alive_ip = ''
    check = subprocess.Popen(['ping', f'192.168.1.{num}', '-c', '1'], stdout=subprocess.PIPE)
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

def core_scan():
    print('\nStarting core scans...')
    start_time = time.perf_counter()
    with multiprocessing.Pool() as pool:
        results = pool.map(ping, (num for num in range(0, 255)))
    end_time = time.perf_counter()
    print('\nCore scans completed...')
    return ips(results), (end_time - start_time)

if __name__ == '__main__':
    core_scan_results = core_scan()
    print('\nAlive addresses:')
    for z in core_scan_results[0]:
        print(f'\t{z}')
    print(f'\nTotal time for scans: {core_scan_results[1]}')

