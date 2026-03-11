STANDARD_WIDTH = 40

def construct_frame(section):
    frame = {}
    line_counter = 2
    frame[1] = '_'*42
    border = "|"
    section = section.split("#")
    def liner(line, line_counter):
        formatted_line = str("")
        leftover = None
        if line.startswith('=='):
            header_centre =  " "*((STANDARD_WIDTH - len(line))//2) 
            formatted_line = header_centre + line + header_centre 

        else:
            
            formatted_line = line
            if len(line) > 38:
                formatted_line = line[:39]
                leftover = line[39:]
            
        frame_line = border + formatted_line
        if len(frame_line) < 41:
            difference = 41 - len(frame_line)
            frame_line += " "*difference
        frame_line += border
        line_counter += 1
              
        frame[line_counter] = frame_line
    
        
        if leftover != None:
            leftover = "    " + leftover
            return liner(leftover, line_counter)
            
        return (line_counter)
        
        
            
    for line in section:
        line_counter = liner(line, line_counter)

    frame[line_counter + 1] = frame[1]

    return frame

def print_frame(frame):
    for item in frame:
        print(frame[item])


def add_frame_adj(frame, section):
    added_frame = construct_frame(section)
    for line in added_frame:
        if line not in frame:
            frame[line] = " "*42
        frame[line] += added_frame[line]






    
TEST_TEXT = "===Suspendisse aliquam erat eget===. diam vestibulum malesuada. Donec volutpat maximus turpis, eu tempus massa lobortis sit amet. Integer cursus ante at nunc accumsan mattis vitae nec mi. Donec eleifend arcu vitae urna convallis, eu euismod neque ornare. Curabitur id sem nisi. Sed tristique nunc consectetur, consectetur sapien eu, sodales sapien. Donec dignissim eget mi at auctor. Morbi accumsan justo vel velit posuere, eget placerat tellus imperdiet. In quis mollis velit, sit amet pellentesque magna. Suspendisse malesuada ante odio, non consequat ipsum luctus id. Maecenas pellentesque congue mauris, eu commodo ligula malesuada sed. Aliquam ornare nisi eu elit ornare, nec rhoncus enim elementum. Nam vitae leo luctus, vestibulum erat et, rutrum massa. Aenean semper, neque vel commodo facilisis, nulla diam pulvinar odio, nec interdum ex nisl a sapien. "
def test_split(testtext):
    return testtext.replace('.','#')
    #return testtext.split(".")

def frame_test():
    section = test_split(TEST_TEXT)
    print(section)
    frame = construct_frame(section)
    print_frame(frame)

