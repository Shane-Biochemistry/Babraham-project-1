import pysam
import csv
samfile = pysam.AlignmentFile("/mnt/c/Users/UP831/Downloads/test.bam","rb")

i = 0
with open("seq_metrics.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Length", "5_prime_softclip", "3_prime_softclip", "insertions", "deletions", "splices"])
    for read in samfile:
        i = i+1
        read_len = read.infer_query_length()
        tl = read.cigartuples
        soft5 = 0
        soft3 = 0
        insertions = 0
        deletions = 0
        splices = 0
        if tl[0][0] == 4:
            soft5 = tl[0][1]
        if tl[-1][1] == 4:
            soft3 = tl[-1][1]
        for t in tl:
            if t[0] ==1:
                 insertions = insertions + 1
            if t[0] ==2:
                deletions = deletions + 1
            if t[0] ==3:
                splices = splices + 1
        read_output = [read_len, soft5, soft3, insertions, deletions, splices]

        writer.writerow (read_output)
