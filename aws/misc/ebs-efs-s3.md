## EBS vs EFS vs S3

These are different tools with different semantics.

## Quick comparison

| Service | Type | Best for | Not great for |
| --- | --- | --- | --- |
| **EBS** | block storage | EC2 disks, for example DB and data volumes | multi-instance sharing |
| **EFS** | network file system, NFS | shared POSIX filesystem | cheap bulk object storage |
| **S3** | object storage | files, media, backups, logs | POSIX filesystem semantics |

## Rules of thumb

- If you need a disk for EC2 → **EBS**
- If multiple instances need shared files → **EFS**
- If it’s blobs/objects → **S3**

## Cost trade-offs

- EFS can be expensive for heavy throughput patterns.
- S3 is cheap storage but egress + requests can add up.

