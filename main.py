if 1 == 1:
  def replace_line(filename, line_number, text):
      with open(filename) as file:
        lines = file.readlines()
      if (line_number <= len(lines)):
        lines[line_number - 1] = text + "\n"
        with open(filename, "w") as file:
          for line in lines:
            file.write(line)
      else:
        print("Line", line_number, "not in file.")
        print("File has", len(lines), "lines.")
    def read_line(fname, lnum):
      try:
        file = open(fname, "r")
        lines = file.readlines()
        file.close()
      except:
        return("Error reading line!") 
      total_lines = len(lines)
      if (lnum > total_lines):
        return(str(total_lines) + " file lines.")
        return("Can't read line " + str(lnum) + "!")
      else:
        line = lines[lnum - 1].rstrip('\n')
        return(line)
