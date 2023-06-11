import subprocess, time, multiprocessing, psutil

def ping(nums):
    alive = []
    for i in range(nums[0], nums[1]+1, 1):
        check = subprocess.Popen(['ping', f'192.168.1.{i}', '-c', '1'], stdout=subprocess.PIPE)
        result = check.communicate()
        if b'1 received' in result[0]:
            alive.append(f'192.168.1.{i}')
    return alive

def ips(ip_list):
    found_ips = []
    for x in ip_list:
        if x != '':
            for y in x:
                found_ips.append(y)
    return found_ips

def num_fill(cores):
    num_list = []
    c = 0
    num_per_block = 256//cores
    while c <= 254:
        if c == 0:
            num_list.append((c, c + num_per_block))
            c = c + num_per_block
        elif (c + num_per_block) >= 256:
            num_list.append((c + 1, 254))
            c = 256
        else:
            num_list.append((c + 1, c + num_per_block))
            c = c + num_per_block

    return num_list

def core_scan(numbers):
    print('\nStarting core scans...')
    start_time = time.perf_counter()
    with multiprocessing.Pool() as pool:
        results = pool.map(ping, numbers)
    end_time = time.perf_counter()
    print('\nCore scans completed...')

    return ips(results), (end_time - start_time)

if __name__ == '__main__':
    cores = psutil.cpu_count()
    numbers = num_fill(cores)

    print(f'\nNumber of cores: {cores}')
    core_scan_results = core_scan(numbers)
    print('\nAlive addresses:')
    for z in core_scan_results[0]:
        print(f'\t{z}')
    print(f'\nTotal time for scans: {core_scan_results[1]}')

