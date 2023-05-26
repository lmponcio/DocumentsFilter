# DocumentsFilter

A script for identifying documents containing specific strings

## Learn to use it

DocumentsFilter can be used for many different purposes. One purpose I thought could be useful for is filtering resumes. Please see below a video where the script is used for screening a big amount of resumes.

[![Watch Video](https://img.youtube.com/vi/h8_KjkikC6U/0.jpg)](https://www.youtube.com/watch?v=h8_KjkikC6U)

## Important information
- DocumentsFilter checks [DOCX (**not DOC**)](https://www.howtogeek.com/304622/WHAT-IS-A-.DOCX-FILE-AND-HOW-IS-IT-DIFFERENT-FROM-A-.DOC-FILE-IN-MICROSOFT-WORD/) and PDF files. If files with other extensions are provided (DOC, JPEG, CSV, TXT, etc.) they will be ignored. This could change in future releases.
- The filters are not case-sensitive (if you write "Excel" or "excel" in Filters.txt it has the same effect). The script transforms both the filters and the documents content to lowercase, and checks if the  lower-cased filters are contained in the lower-cased documents content.
- DocumentsFilter is not 100% accurate - It's quite accurate, but not perfect. For more information check the libraries used for scanning the ".docx" files ([python-docx](https://github.com/python-openxml/python-docx)) and the ".pdf" files ([pypdf](https://github.com/py-pdf/pypdf)).
- Images are not checked, only text. In the future I might add optical character recognition so text in images is also checked, but for now it is only checking text elements.
- There is no AI involved. It is a script that goes through the text elements in documents and checks if the filter strings provided are present or absent. 

## Acknowledgments
DocumentsFilter is a Python code that uses external libraries to do its job. Special thanks to the mantainers of  [python-docx](https://github.com/python-openxml/python-docx), [pypdf](https://github.com/py-pdf/pypdf) and [openpyxl](https://foss.heptapod.net/openpyxl/openpyxl).
