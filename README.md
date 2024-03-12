Source : AutoNuke_no_post 
zsfdakq5ubv3qxbdglbdmaratvixdchbwyrtxabofvyurdyco66av5qd.onion/p/AutoNuke_no_post



sudo masscan --rate=2000 --interface eth0 -p80,443,8443,10443,22,3389,3306 -Pn ip.lst -oJ tmp/test.log


grep -oE \"\\b([0-9]{1,3}\.){3}[0-9]{1,3}\\b\" tmp/test.log > tmp/unsorted.txt
sort tmp/unsorted.txt | uniq > tmp/abc_targets.txt

echo "" > tmp/abc_targets.txt


cat tmp/abc_targetss.txt | httpx -random-agent -nf -rl 5000 -t 1000 -p 

22,3389,3306,80,443,7547,8080,8089,4567,8008,8443,8081,2087,2083,2082,5985,2086,8000,8888,1024,21,81,8880,9080,5000,49152,9000,3128,7170,8085,8090,5001,8001,9999,10000,10443,8083,9090,3000,88,5357,9100,7777,82,52869,9443,4443,8800,9306,8181,444,7443,9001,2096,8086,5222,8010,1234,8009,8200,2095,10001,9002,83,6000,20000,9009,50000,5005,6443,9200,32400,2222,5555,3001,8069,8099,8889,6001,1900,8060,9998,5006,7001,84,5986,8123,888,25,12345,5800,631,10250,8098,7548,2000,2121,8112,3702,2077,8087,5010,8126,23,161,6667,6697 -o tmp/abc_targets2.txt

nuclei -l tmp/abc_targets2.txt -severity critical,high -o targets/1.nuked

cat targets/1.nuked >> ./'
