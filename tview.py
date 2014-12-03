import sys

MAX_LINES = 100

if len(sys.argv) == 1:
	print "usage:  tview [file_name]"
	print "tab delimited view of the first 100 lines in a file."
	sys.exit(1)

# First pass:  determine size of columns, based on first N lines
file = sys.argv[1]
fd = open (file)
max_widths = []
line_count = 0
for line in fd:
	if line_count > MAX_LINES:
		break
	line = line.strip()
	parts = line.split("\t")

	# Init widths to 0
	if len(max_widths) == 0 and len(parts) > 2:
		for part in parts:
			max_widths.append(0)
	
	# Use actual fields to determine column widths
	if len(max_widths) > 0:
		for i in range(0, len(parts)):
			part = parts[i]
			current_len = len(part)
			if current_len > max_widths[i]:
				max_widths[i] = current_len
	line_count +=1
fd.close()

# Second pass:  output, based on column size
fd = open (file)
line_count = 0
for line in fd:
	if line_count > MAX_LINES:
		break
	line = line.strip()
	parts = line.split("\t")
	if len(parts) > 2:
		for i in range(0, len(parts)):
			part = parts[i]
			width = max_widths[i]
			print "%-*s\t" % (width, part),
		print
		if line_count == 0:
			for i in range(0, len(parts)):
				width = max_widths[i]
				divider = width * "-"
				print "%s\t" % (divider),
			print
		line_count +=1
fd.close()