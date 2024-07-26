# cvechecker
- This command get CVE information from NVD database. 

## Python
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
