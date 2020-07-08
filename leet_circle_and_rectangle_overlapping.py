class Solution:
    def checkOverlap(self, radius: int, x_cen: int, y_cen: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x1<=x_cen<=x2 and y1<=y_cen<=y2:
            return True
        
        if x_cen<=x1:
            x=x1
        elif x_cen>=x2:
            x=x2
        else:
            x=x_cen
        
        if y_cen<=y1:
            y=y1
        elif y_cen>=y2:
            y=y2
        else:
            y=y_cen
        dist = ((x_cen-x)**2+(y_cen-y)**2)**0.5
        return dist<=radius