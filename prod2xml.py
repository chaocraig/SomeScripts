from sys import stdout
import re
import csv



xml_header  = "<!-- XML for Solr input  -->\n" + \
              "<add>\n"
xml_footer  = "</add>\n"

xml_fields  = ["id", "salename", "lclassname", "mclassname", "sclassname", \
                "marketprice", "thisprice", "purpose", "suppliername"]

id_pre = "eitc_"

infile  = "prod_list_02.csv"
outfile = "prod_02.xml" 

total_record_num = 0

def strip_quotes(fields):
        line = []
        for field in fields:
		#print "Field: " + field + "\n"
                new_field = re.sub(r"[\s|\0-\x2D|\+|\-|\&|\^|\|\(|\)|\[|\]|\{|\}|\'|\<|\>]", " ", \
                            field, flags = re.MULTILINE)
		#print "New Field: " + new_field + "\n"
		#matchObj = re.search( r'^\s*\"(.*)\s*\"\s*$', new_field)
        	#print matchObj.group(1)
		#if (matchObj is not None):
                # 	line.append(matchObj.group(1))
		line.append(new_field.strip())
        return(line)

def parse_write(line):
         f_out.write("<doc>")
	 i = 0
         line_array = strip_quotes(line)
         for element in line_array:
		# print "  <field name=\"" + xml_fields[i] + "\">" + element + "</field>\n"
		if (i==0):
			element_str = id_pre + element
		else:
			element_str = element
		f_out.write("  <field name=\"" + xml_fields[i] + "\">" + element_str + "</field>\n")
        	i += 1
	 f_out.write("</doc>\n")
	 if (i==len(xml_fields)):
		return 1
	 else:
		return 0


f_out = open(outfile, 'w')
f_out.write(xml_header)

with open(infile, "r") as f_in:
    for line in f_in:
        prod = line.strip().split(',')
	if ( len(prod) == len(xml_fields) ):
		total_record_num += parse_write(prod)


f_out.write(xml_footer)
f_out.close()

print "Total record# = ", total_record_num

