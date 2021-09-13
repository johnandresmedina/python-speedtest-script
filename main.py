import speedtest

ONE_MB = 1000000
servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1

s = speedtest.Speedtest()
#s.get_servers(servers)
s.get_best_server()
s.download(threads=threads)
s.upload(threads=threads)
# s.results.share()

results_dict = s.results.dict()

rounded_download_speed = round(results_dict['download'] / ONE_MB)
rounded_upload_speed = round(results_dict['upload'] / ONE_MB)

print(f"Download: {rounded_download_speed} Mbps.")
print(f"Upload: {rounded_upload_speed} Mbps.")