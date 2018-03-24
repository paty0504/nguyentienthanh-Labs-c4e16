import pyexcel
a_list_of_dictonaries = [
{
"title": "Hom nay troi dep",
"link": "http://google.com.vn"

},
{
"title": "Hom nay troi dep",
"link": "http://google.com.vn"

},
{
"title": "Hom nay troi dep",
"link": "http://google.com.vn"

},
]
pyexcel.save_as(records=a_list_of_dictonaries,dest_file_name="your_file.xls")
