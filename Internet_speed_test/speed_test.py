import speedtest


def sizes(n_bytes):
    suffixes = ["Bps", "Kbps", "Mbps", "Gbps"]
    i = 0
    while n_bytes >= 1024 and i < len(suffixes) - 1:
        n_bytes /= 1024
        i += 1
    f = ("%.2f" % n_bytes).rstrip("0").rstrip(".")
    return "%s %s" % (f, suffixes[i])


st = speedtest.Speedtest()

ds = st.download()
us = st.upload()

print("--------- Internet Speed Test ---------")
print("Download Speed:", sizes(ds))
print("Upload Speed: ", sizes(us))


