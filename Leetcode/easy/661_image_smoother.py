class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        row_len=len(img)
        col_len=len(img[0])
        new_list=[[0]*col_len for _ in range(row_len)]
        for i in range(row_len):
            for j in range(col_len):
                box_num=0
                sum=0
                for m in range(max(0,i-1),min(i+1,row_len-1)+1):
                    for n in range(max(0,j-1),min(j+1,col_len-1)+1):
                        box_num+=1.0
                        sum=sum+img[m][n]
                avg=sum/box_num
                new_list[i][j]=int(avg)
        return new_list