import argparse 
import cv2
import numpy as np


# python main.py -v video1 video2 video3  -c rowxcolumn -r True
# -v list of videos
# -c Row x Column
# -r To resize or not maintain original
# Example 
# python main.py -v /home/n200/Documents/codes/ITRI/edgematrix/out_EH_PIH_mbv2-c0.avi /home/n200/Documents /codes/ITRI/edgematrix/out_EH_PIH_mbv2-c0.avi /home/n200/Documents/codes/ITRI/edgematrix/out_EH_PIH_mbv2-c0.avi -c 2x2 -r True

parser = argparse.ArgumentParser()
parser.add_argument("--videos","-v",metavar='N', type=str, nargs='+',help='Videos paths. All videos should have same video legth and shape',required=False)
parser.add_argument("--conf","-c",type=str,help='RowxColumn e.g. 3x4')
parser.add_argument("--resize","-r",type=bool,help='Resize output frame',required=False)
args = parser.parse_args()

row,column = args.conf.split("x")
row = int(row)
column = int(column)

inputs = [x for x in args.videos]
caps = [cv2.VideoCapture(inp) for inp in inputs]


width = int(caps[0].get(3))
height = int(caps[0].get(4))


dim  = ()

if args.resize == None:
    dim = (width*column,height*row)
else:
    dim = (width,height)

out = cv2.VideoWriter(f"comb_video.avi",cv2.VideoWriter_fourcc('M','J','P','G'), 30, dim)

black_img = np.zeros((height,width,3),np.uint8)

num_slots = row * column
slots = np.linspace(0,num_slots-1,num_slots).astype(int)

arranged_slots = np.reshape(slots,(row,column)).tolist()
ret = None
while True:
    images  = []
    for cap in caps:
        ret,frame= cap.read()
        if not ret:
            break
        else:
            images.append(frame)
        
    if not ret:
        break

    while len(images)!=num_slots:
        images.append(black_img)
    
    to_concat = [] 
    for r in range(row):
        col = []
        for c in range(column):
            col.append(images[arranged_slots[r][c]])
        to_concat.append(col)

    rows_images = []
    for r in range(row):
        rows_images.append(np.concatenate(to_concat[r],axis=1)) 

    img = np.concatenate(rows_images,axis=0)
    resized = img
    if not args.resize == None:
        resized = cv2.resize(resized, (width,height), interpolation = cv2.INTER_AREA)
    
    cv2.imshow("Combined Video",resized)
    out.write(resized)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
print("Closing all windows")
cv2.destroyAllWindows()