# 🛡️ MapReduce DDoS Detector

An Apache Hadoop MapReduce project written in Python using `mrjob`. This tool acts as a cybersecurity log analyzer, parsing massive web server access logs to identify anomalous traffic spikes and isolate IP addresses associated with potential Distributed Denial of Service (DDoS) or brute-force attacks.

## ⚙️ How It Works (Hadoop Architecture)
1. **Mapper Phase:** Scans the raw unstructured log files and extracts the source IP address from each request.
2. **Shuffle & Sort:** Hadoop groups all identical IPs together across the cluster network.
3. **Reducer Phase 1:** Aggregates the total number of HTTP requests made by each individual IP.
4. **Reducer Phase 2:** Sorts the aggregated data to identify and isolate the single IP with the highest traffic volume (The Threat).

## 🚀 How to Run Locally

**1. Install Dependencies**
Ensure you have Python installed, then install the MapReduce library:
`pip install mrjob`

**2. Generate Big Data Logs**
Run the log generator to create a fake `server_logs.txt` file simulating 10,000 HTTP requests:
`python generate_logs.py`

**3. Execute the MapReduce Job**
Run the threat detection algorithm against the log file:
`python ddos_detector.py server_logs.txt`

## 👨‍💻 Developer
Developed by **Abhay Mirashi**
Bachelor of Computer Applications (BCA)
Specializing in Artificial Intelligence, Machine Learning, and Cybersecurity.

