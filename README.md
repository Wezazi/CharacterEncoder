I created this script because xxd don't allow more than one flag:  
printf '&lt;string>' | iconv -f UTF-8 -t UTF-16LE | xxd -b -p  

Create Virtual Environment:    
python -m venv venv  

Activate Virtual Environment:  

Windows: venv\Scripts\activate  
Linux:  source venv/bin/activate

How to run:  
python encode.py  

pip install regex  
python verbose.py
