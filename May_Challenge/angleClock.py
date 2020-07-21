class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        
        # total 360 degrees
        # min hand moves 360 for 60 mins = 360/60=6
        # hr hand moves 30 (difference of small pipe between two nos )degree for 1 hr
        # which is 5* minhand 6 = 30 degree for 1 hr
        # take base as 12 which is 0th degree
        if hour==12:
            hour = 0
        minDeg = minutes * 6
        hrDeg = hour * 30.0 + minutes * 0.5
        diff = abs(minDeg - hrDeg)
        if diff > 180:
            diff = 360- diff
        return diff
