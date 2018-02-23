# ssdck
Estimates SSD longevity using smartmontools and a database of manufacturer provided read/write cycle statistics.

#### Proposal:
The goal of this project is to provide a tool that will make it easier for datacenter technicians and systems administrators to grade used SSDs based on remaining longevity. Grading SSDs based on wear-level can be used to ensure that heavily worn drives are not cycled back into use. Parseable output from this program could potentially be used to generate usage reports and/or pre-emptively replace heavily-worn drives.


#### Potential Features:
* Easily maintainable SSD information database, containing information such as Drive model, Drive capacity, Mean Time before Failure (MTBF), Mean Writes before Failure (MWBF), designated error capacity threshold.
* Auditing trail for user-issued secure erase commands
* SMART info collection upon drive failure. Potentially useful looking @ trends that indicate imminent failure?
* Automatic inventory updates. Drives added to inventory list when secure-erased. Drives removed from inventory when HOST drive-scan finds matching SN.
