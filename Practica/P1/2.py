print("Segundos: ")
total_time_seconds = int(input())

hours = int(total_time_seconds / 3600)
rem_seconds = total_time_seconds % 360

minutes = int(rem_seconds / 60)

seconds = rem_seconds % 60
print(f"{hours} hora(s), {minutes} minutos(s), {seconds} segundo(s)")
