from mrjob.job import MRJob
from mrjob.step import MRStep

class MRDDosDetector(MRJob):
    """
    A Hadoop MapReduce job to analyze massive server logs
    and identify potential DDoS attacks or brute-force threats.
    """

    def steps(self):
        return [
            MRStep(mapper=self.mapper_extract_ip,
                   reducer=self.reducer_count_requests),
            MRStep(reducer=self.reducer_find_hacker)
        ]

    # PHASE 1: MAP - Extract IP addresses from the log lines
    def mapper_extract_ip(self, _, line):
        ip = line.split(" ")[0]
        yield (ip, 1)

    # PHASE 2: REDUCE - Aggregate the request counts per IP
    def reducer_count_requests(self, ip, counts):
        yield None, (sum(counts), ip)

    # PHASE 3: SHUFFLE & REDUCE - Sort to find the highest traffic source (Threat)
    def reducer_find_hacker(self, _, count_ip_pairs):
        top_attacker = max(count_ip_pairs)
        yield "PRIMARY THREAT DETECTED:", top_attacker

if __name__ == '__main__':
    MRDDosDetector.run()
