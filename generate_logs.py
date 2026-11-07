import random

def generate_apache_logs(filename="server_logs.txt", num_lines=10000):
    normal_ips = [f"192.168.1.{i}" for i in range(10, 50)]
    hacker_ip = "45.22.19.105" # Simulated Threat IP

    with open(filename, "w") as f:
        for _ in range(num_lines):
            # 15% traffic is from the hacker, 85% is normal user traffic
            ip = hacker_ip if random.random() < 0.15 else random.choice(normal_ips)
            f.write(f"{ip} - - [07/Nov/2026:08:55:00 +0530] \"GET /login HTTP/1.1\" 401 128\n")
            
    print(f"{num_lines} server logs generated successfully in {filename}!")

if __name__ == "__main__":
    generate_apache_logs()
