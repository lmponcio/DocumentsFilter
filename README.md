# DocumentsFilter

A script for identifying documents containing specific strings

## Learn to use it

[![Watch Video](https://img.youtube.com/vi/placeHolderVideoId/0.jpg)](https://www.youtube.com/watch?v=placeHolderVideoId)

## Important information
- The only document formats checked are [DOCX (**not DOC**)](https://www.howtogeek.com/304622/WHAT-IS-A-.DOCX-FILE-AND-HOW-IS-IT-DIFFERENT-FROM-A-.DOC-FILE-IN-MICROSOFT-WORD/) and PDF. If files to folder contains files with other extensions (DOC, JPEG, CSV, TXT, etc.) they will be ignored. This could change in future releases.
- The filters are not case-sensitive (if you write "Excel" or "excel" in Filters.txt it has the same effect). The script transforms both the filters and the documents content to lowercase, and checks if the  lower-cased filters are contained in the lower-cased documents content.
- DocumentsFilter is not 100% accurate - It's quite accurate, but not perfect. For more information check the libraries used for scanning the ".docx" files ([python-docx](https://github.com/python-openxml/python-docx)) and the ".pdf" files ([pypdf](https://github.com/py-pdf/pypdf)).
- Images are not checked, only text. In the future we might add optical character recognition so text in images is also checked, but for now it is only checking text elements.
- There is no AI involved. It is a simple script that goes through the text elements in documents and checks if the filter strings provided are present or absent. 

## Acknowledgments
DocumentsFilter is a small Python code that uses external libraries to do its job. Special thanks to the mantainers of  [python-docx](https://github.com/python-openxml/python-docx), [pypdf](https://github.com/py-pdf/pypdf) and [openpyxl](https://foss.heptapod.net/openpyxl/openpyxl).
