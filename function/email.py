email_id="hari@gmail.com"

at_index_pos=email_id.index("@")

user_name=email_id[:at_index_pos]

print(user_name)

domain=email_id[at_index_pos:]

print(domain)