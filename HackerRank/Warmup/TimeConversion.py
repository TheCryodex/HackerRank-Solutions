def timeConversion(s):
    hrs, minutes, secs = s.split(":")
    secs = secs[:2]
    am="AM"
    pm="PM"

    if am in s:
        if hrs=="12" and minutes=="00" and secs=="00":
            hrs="00"
            return(hrs+":"+minutes+":"+secs)
        else:
            return(s[:8])
    if pm in s:
        if hrs=="12":
            return(s[:8])
        else:
            hrs=int(hrs)+12
            return(str(hrs)+":"+minutes+":"+secs)