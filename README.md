## cleaning tool for file systems

## dependencies

python3 installed

#### usage

parameters    

specify location

-p c:\\some location (use absolute location)


removes space in file and folder names with _ or trim spaces

-s [_, "" default]
    
    
removes the specified file types in this sceanario .zip and .VTT

-d .zip .vtt .png

so example command

```bash
python clean.py -d .vtt -p c:\\ee\ee\\ -s _
```
