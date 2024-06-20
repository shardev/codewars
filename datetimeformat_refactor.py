import math

def format_duration(seconds):
    if seconds == 0:
        return "now"

    smallestPart = ''
    outString = ''
    countParts = 0

    years = math.floor(seconds/(365 * 24 * 60 * 60))
    if years > 0:
        seconds -= years * (365 * 24 * 60 * 60)
        countParts += 1
    
    days = math.floor(seconds/(24 * 60 * 60))
    if days > 0:
        smallestPart = 'days'
        seconds -= days * (24 * 60 * 60)
        countParts += 1
    
    hours = math.floor(seconds/(60 * 60))
    if hours > 0:
        smallestPart = 'hours'
        seconds -= hours * (60 * 60)
        countParts += 1

    minutes = math.floor(seconds/60)
    if minutes > 0:
        smallestPart = 'minutes'
        seconds -= minutes * 60
        countParts += 1

    if seconds > 0:
        smallestPart = 'seconds'
        countParts += 1
    print(f"Years {years}, Days {days}, Hours {hours}, Minutes {minutes}, Seconds {seconds}; Smallest part {smallestPart}")

    if years > 0:
        outString += f"{years} year" if years == 1 else f"{years} years"
    
    if days > 0:
        if smallestPart == 'days' and countParts > 1:
            outString += f" and {days} day" if days == 1 else f" and {days} days"
        elif smallestPart == 'days' and countParts == 1:
            outString += f"{days} day" if days == 1 else f"{days} days"
        else:
            outString += f", {days} day" if days == 1 else f", {days} days"
    if hours > 0:
        if smallestPart == 'hours' and countParts > 1:
            outString += f" and {hours} hour" if hours == 1 else f" and {hours} hours"
        elif smallestPart == 'hours' and countParts == 1:
            outString += f"{hours} hour" if hours == 1 else f"{hours} hours"
        else:
            outString += f", {hours} hour" if hours == 1 else f", {hours} hours"
    if minutes > 0:
        if smallestPart == 'minutes' and countParts > 1:
            outString += f" and {minutes} minute" if minutes == 1 else f" and {minutes} minutes"
        elif smallestPart == 'minutes' and countParts == 1:
            outString += f"{minutes} minute" if minutes == 1 else f"{minutes} minutes"
        else:
            outString += f", {minutes} minute" if minutes == 1 else f", {minutes} minutes"
    if smallestPart == 'seconds' and countParts > 1:
        outString += f" and {seconds} second" if seconds == 1 else f" and {seconds} seconds"
    if smallestPart == 'seconds' and countParts == 1:
        outString += f"{seconds} second" if seconds == 1 else f"{seconds} seconds"
    
    return outString[2:] if outString[0] == ',' else outString
    
# print(format_duration(3662)) # "1 hour, 1 minute and 2 seconds"
print(format_duration(1)) # "1 second"
    
    