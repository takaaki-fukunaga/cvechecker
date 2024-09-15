# cvechecker
- This command get CVE information from NVD database. 

## Python
### Set CVE-ID Directly
1. Download [get-cve.py](python/get-cve.py).
1. Run the script as below.
   ```sh
   python3.8 get-cve.py <CVEID>
   ```
   - You can get CVSSv3 score.
     ```
     $ python3.8 get-cve.py CVE-2021-42781
     CVE-2021-42781,5.3
     ```
   - If you cannot get the score, the score will be shown as "0.0".
     ```
     $ python3.8 get-cve.py CVE-2024-36006
     CVE-2024-36006,0.0
     ```
### Read a File Contains CVE-IDs
1. Download [get-cve.py](python/get-cve.py).
1. Create a file as below (e.g., cve-id.txt).
   ```
   CVE-2023-52760
   CVE-2023-52887
   CVE-2024-25741
   (snip)
   ```
1. Create a bash file as below (e.g., check-cve.sh).
   ```sh
   while read line
   do
       python3.8 get-cve.py $line
       sleep 10
   done < $1
   ```
   ```sh
   chmod +x check-cve.sh
   ```
1. Save the files on the same directry.
   ```
   cve-check/
   ├── check-cve.sh
   ├── cve-id.txt
   └── get-cve.py
   ```
1. Run the bash file.
   ```sh
   ./check-cve.sh cve-id.txt
   ```

## Link
- Vulnerability APIs
  - https://nvd.nist.gov/developers/vulnerabilities
