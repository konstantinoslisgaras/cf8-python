class MyTime:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    
    def increment(self, seconds):
        self.seconds += seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
    
    def add_time(self, other):
        total_seconds = self.to_seconds() + other.to_seconds()
        result = MyTime()
        result.increment(total_seconds)
        return result
    
    def sub_time(self, other):
        total_seconds = self.to_seconds() - other.to_seconds()
        result = MyTime()
        result.increment(total_seconds)
        return result
    
    def __add__(self, other):
        return self.add_time(other)
    
    def __sub__(self, other):
        return self.sub_time(other)
    
    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
        
def main():
    time1 = MyTime(1, 30, 45)
    time2 = MyTime(2, 45, 10)

    print("Time 1:", time1)
    print("Time 2:", time2)

    time1.increment(90)
    print("Time 1:", time1)

    time3 = time1.add_time(time2)
    print("Time 3:", time3)

    time4 = time1 + time2
    print("Time 4:", time4)

    time5 = time4 - time2
    print("Time 5:", time5)

if __name__ == "__main__":
    main()