doctor_hto_cop = 5 # cop per 1 view
doctor_hto_hrn = doctor_hto_cop / 100 # hryvnyas per 1 view
total_channel_views = 1000
profit_hrn = total_channel_views * doctor_hto_hrn
print("Total profit: ", profit_hrn, "hrn")